"""Session and CORS settings must follow their environment variables.

Three defaults used to be hardcoded in the login route, where no environment
variable could reach them: a 24-hour token, a 24-hour cookie and
`secure=False`. The CORS default named a port the application does not serve
on. These check the knobs are wired to the behaviour.
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest
from jose import jwt

from auth import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY

REPO_ROOT = Path(__file__).resolve().parents[1]

# The settings are read when `main` is imported, so each case needs its own
# interpreter. This probe reports what the module ended up configured with.
PROBE = """
import json, main
print(json.dumps({
    "port": main.APP_PORT,
    "allowed_origins": main.allowed_origins,
    "allow_credentials": main.allow_credentials,
    "cookie_secure": main.COOKIE_SECURE,
    "cookie_samesite": main.COOKIE_SAMESITE,
}))
"""


def probe(**env):
    """Import the application with the given environment and report settings."""
    result = subprocess.run(
        [sys.executable, "-c", PROBE],
        cwd=REPO_ROOT,
        env={
            "PATH": "/usr/bin:/bin:/usr/local/bin",
            "SECRET_KEY": "test-only-secret-key-not-for-production",
            **env,
        },
        capture_output=True, text=True, timeout=120,
    )
    assert result.returncode == 0, f"importing main failed:\n{result.stderr}"
    return json.loads(result.stdout.strip().splitlines()[-1])


def test_cors_default_names_the_port_the_application_serves_on():
    """A default of :8000 while uvicorn binds :8400 blocks every browser call."""
    settings = probe()
    assert settings["port"] == 8400
    assert settings["allowed_origins"] == ["http://localhost:8400"]


def test_cors_default_follows_a_custom_port():
    settings = probe(PORT="9000")
    assert settings["port"] == 9000
    assert settings["allowed_origins"] == ["http://localhost:9000"]


def test_allowed_origins_overrides_the_default():
    settings = probe(ALLOWED_ORIGINS="https://soc.example.com, https://alt.example.com")
    assert settings["allowed_origins"] == [
        "https://soc.example.com", "https://alt.example.com"]
    assert settings["allow_credentials"] is True


def test_wildcard_origins_disable_credentialed_cors():
    """`allow_origins=["*"]` and `allow_credentials=True` are incompatible."""
    settings = probe(ALLOWED_ORIGINS="*")
    assert settings["allowed_origins"] == ["*"]
    assert settings["allow_credentials"] is False


def test_cookie_is_not_secure_by_default_on_plain_http():
    """The default is http://localhost, where a secure cookie is never sent."""
    assert probe()["cookie_secure"] is False


def test_cookie_is_secure_when_every_origin_is_https():
    assert probe(ALLOWED_ORIGINS="https://soc.example.com")["cookie_secure"] is True


def test_a_single_plain_http_origin_keeps_the_cookie_insecure():
    settings = probe(
        ALLOWED_ORIGINS="https://soc.example.com,http://localhost:8400")
    assert settings["cookie_secure"] is False


@pytest.mark.parametrize("value,expected", [
    ("true", True), ("1", True), ("yes", True), ("on", True), ("TRUE", True),
    ("false", False), ("0", False), ("no", False), ("", False),
])
def test_cookie_secure_can_be_set_explicitly(value, expected):
    """Deployments behind a TLS-terminating proxy need to force this on."""
    settings = probe(COOKIE_SECURE=value, ALLOWED_ORIGINS="http://localhost:8400")
    assert settings["cookie_secure"] is expected


def test_cookie_samesite_is_configurable():
    assert probe()["cookie_samesite"] == "lax"
    assert probe(COOKIE_SAMESITE="strict")["cookie_samesite"] == "strict"


def test_login_cookie_expires_with_the_token(client, alice):
    """Token and cookie must share one lifetime, taken from the environment.

    A cookie outliving its token logs the user out with no way to notice; a
    token outliving its cookie leaves a valid credential behind.
    """
    response = client.post("/api/auth/login", json={
        "username": alice["username"], "password": alice["password"]})
    assert response.status_code == 200, response.text

    expected = ACCESS_TOKEN_EXPIRE_MINUTES * 60
    cookie = next(v for k, v in response.headers.items() if k.lower() == "set-cookie")
    attributes = {
        part.split("=", 1)[0].strip().lower():
            part.split("=", 1)[1].strip() if "=" in part else ""
        for part in cookie.split(";")
    }
    assert int(attributes["max-age"]) == expected
    assert "httponly" in attributes
    assert attributes["samesite"].lower() == "lax"

    claims = jwt.decode(response.json()["access_token"], SECRET_KEY,
                        algorithms=[ALGORITHM])
    lifetime = claims["exp"] - int(__import__("time").time())
    assert abs(lifetime - expected) <= 60, (
        f"token lives {lifetime}s but the cookie lives {expected}s")

    client.cookies.clear()


def test_the_default_session_lifetime_is_not_a_full_day():
    """24 hours was the hardcoded value this replaced; it is too long for a
    credential sitting in a browser cookie."""
    assert 0 < ACCESS_TOKEN_EXPIRE_MINUTES <= 12 * 60
