#!/usr/bin/env python3
"""Capture the screenshots used in the README and release posts.

Screenshots go stale: 2.0.x images showed 622 questions and a scoring floor
that no longer exists. This regenerates them from a running instance so a
release can refresh them in one command instead of by hand.

    python scripts/capture_screenshots.py --base-url http://localhost:8400 \
        --out docs/screenshots --username admin --password "$ADMIN_PASSWORD"

The pages load Chart.js, Font Awesome and flag-icons from CDNs. Pass
`--vendor DIR` to serve them from a local directory instead, which is required
on a machine with no CDN access — without Chart.js the radar renders blank.
DIR must contain:

    chart.js/dist/chart.umd.js
    fontawesome-free/css/all.min.css   (plus webfonts/)
    flag-icons/css/flag-icons.min.css  (plus flags/)

each laid out as the published npm package.
"""
import argparse
import sys
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("playwright is required: pip install playwright")

# The summary donut and the radar are both `.card` elements containing a
# canvas, and the donut comes first, so the radar has to be addressed by its
# own canvas id and the enclosing card taken from there.
# `contains(@class,"card")` would also match `card-body`, which is the nearer
# ancestor and excludes the card header — match the class as a whole token.
RADAR_CARD = (
    'xpath=//canvas[@id="radarChart"]/ancestor::div['
    'contains(concat(" ", normalize-space(@class), " "), " card ")][1]'
)

# The questionnaire lands on an aspect picker. What is worth showing is the
# questions themselves, each with the maturity wording the workbook gives for
# that specific question — so open the first aspect before capturing.
OPEN_FIRST_ASPECT = """
const card = document.querySelector('[onclick^="selectAspect"]');
if (card) { card.click(); }
"""

# (filename, path, language, viewport, selector, caption, action)
#
# `selector` frames one element instead of the viewport: the radar sits well
# below the fold, so a plain shot of /results shows the summary donut and none
# of the chart it is named for. `action` is JavaScript run after load, for
# pages whose landing state is not the interesting one.
SHOTS = [
    ("results-radar.png", "/results/{assessment}", "en", (1040, 1250),
     RADAR_CARD, "Results: the radar chart across the five domains", None),
    ("results-domains.png", "/results/{assessment}", "en", (1280, 1100),
     None, "Results: overall maturity and per-domain scores", None),
    ("questionnaire.png", "/assessment/{assessment}", "en", (1280, 1150),
     None, "Questionnaire: questions with their maturity levels", OPEN_FIRST_ASPECT),
    ("questionnaire-pt-br.png", "/assessment/{assessment}", "pt_br", (1280, 1150),
     None, "The same questionnaire in Brazilian Portuguese", OPEN_FIRST_ASPECT),
    ("results-radar-pt-br.png", "/results/{assessment}", "pt_br", (1040, 1250),
     RADAR_CARD, "Radar chart in Brazilian Portuguese", None),
    ("customers.png", "/customers", "en", (1280, 900),
     None, "Customer list with assessment history", None),
    ("mobile-results.png", "/results/{assessment}", "en", (414, 896),
     None, "Results on a phone-width viewport", None),
]

# CDN URL prefix -> path inside the vendor directory.
VENDOR_ROUTES = [
    ("https://cdn.jsdelivr.net/npm/chart.js", "chart.js/dist/chart.umd.js", "application/javascript"),
    ("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/", "fontawesome-free/", None),
    ("https://cdnjs.cloudflare.com/ajax/libs/flag-icons/", "flag-icons/", None),
]

CONTENT_TYPES = {".css": "text/css", ".js": "application/javascript",
                 ".woff2": "font/woff2", ".woff": "font/woff", ".ttf": "font/ttf",
                 ".svg": "image/svg+xml", ".png": "image/png"}


def install_vendor_routes(context, vendor: Path) -> None:
    """Serve CDN assets from `vendor` so pages render without network access."""
    def handler(route):
        url = route.request.url
        for prefix, target, forced_type in VENDOR_ROUTES:
            if not url.startswith(prefix):
                continue
            if target.endswith("/"):
                # Map the tail of the CDN path onto the package layout, e.g.
                # .../font-awesome/6.0.0/css/all.min.css -> css/all.min.css
                tail = url[len(prefix):].split("?")[0]
                parts = tail.split("/")
                tail = "/".join(parts[1:]) if parts and parts[0][0].isdigit() else tail
                path = vendor / target / tail
            else:
                path = vendor / target
            if path.is_file():
                suffix = path.suffix.lower()
                route.fulfill(status=200, body=path.read_bytes(),
                              content_type=forced_type or CONTENT_TYPES.get(suffix, "application/octet-stream"))
                return
            print(f"    [vendor] MISSING {path}", file=sys.stderr)
            route.abort()
            return
        route.continue_()

    context.route("https://cdn.jsdelivr.net/**", handler)
    context.route("https://cdnjs.cloudflare.com/**", handler)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--base-url", default="http://localhost:8400")
    ap.add_argument("--out", default="docs/screenshots")
    ap.add_argument("--username", default="admin")
    ap.add_argument("--password", required=True)
    ap.add_argument("--assessment", type=int, default=None,
                    help="assessment id to show (default: the highest one)")
    ap.add_argument("--vendor", default=None,
                    help="directory of local CDN assets (see module docstring)")
    ap.add_argument("--browser", default=None,
                    help="path to a Chromium binary, when the bundled one is "
                         "absent or a different build (e.g. a preinstalled "
                         "/opt/pw-browsers/chromium-*/chrome-linux/chrome)")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        launch = {"executable_path": args.browser} if args.browser else {}
        browser = p.chromium.launch(**launch)
        context = browser.new_context(viewport={"width": 1440, "height": 1000},
                                      device_scale_factor=2)
        if args.vendor:
            install_vendor_routes(context, Path(args.vendor))

        page = context.new_page()
        response = page.request.post(f"{args.base_url}/api/auth/login",
                                     data={"username": args.username,
                                           "password": args.password})
        if not response.ok:
            return _fail(f"login failed: {response.status} {response.text()}")

        assessment = args.assessment
        if assessment is None:
            r = page.request.get(f"{args.base_url}/api/customers")
            customers = r.json().get("customers", [])
            if not customers:
                return _fail("no customers — seed some data before capturing")
            ids = []
            for c in customers:
                ar = page.request.get(f"{args.base_url}/api/customers/{c['id']}/assessments")
                ids += [a["id"] for a in ar.json().get("assessments", [])]
            if not ids:
                return _fail("no assessments — seed some data before capturing")
            assessment = max(ids)
        print(f"  using assessment {assessment}")

        for name, path, language, viewport, selector, caption, action in SHOTS:
            page.set_viewport_size({"width": viewport[0], "height": viewport[1]})
            context.add_cookies([{"name": "language", "value": language,
                                  "url": args.base_url}])
            url = args.base_url + path.format(assessment=assessment)
            page.goto(url, wait_until="networkidle")
            # Charts are drawn after the scores request resolves.
            page.wait_for_timeout(2500)
            if action:
                page.evaluate(action)
                page.wait_for_timeout(1500)
            target = out / name
            shot = page
            if selector:
                element = page.query_selector(selector)
                if element is None:
                    return _fail(f"{name}: no element matched {selector!r}")
                element.scroll_into_view_if_needed()
                page.wait_for_timeout(600)
                shot = element
            shot.screenshot(path=str(target))
            where = selector or "viewport"
            print(f"  {name:28} {viewport[0]}x{viewport[1]:<5} {caption}")

        browser.close()
    print(f"\nwrote {len(SHOTS)} screenshots to {out}")
    return 0


def _fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
