# Language system (EN/PT-BR)

- Language switcher visible in the top bar (🇺🇸 / 🇧🇷)
- Language detection via `?lang=en|pt_br` or the `language` cookie
  (default: `en`)
- Route: `/change-language/{language}` (persists for 1 year via cookie)
- Templates duplicated by language (e.g. `index.html` and
  `index_pt_br.html`)
- Automated tests cover language switching and persistence

For implementation details, see `LANGUAGE_SYSTEM_SUMMARY.md` at the
repository root.
