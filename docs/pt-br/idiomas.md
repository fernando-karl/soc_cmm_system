# Sistema de Idiomas (EN/PT-BR)

- Seletor visível na barra superior (🇺🇸/🇧🇷)
- Detecção por `?lang=en|pt_br` ou cookie `language` (padrão: en)
- Rota: `/change-language/{language}` (persiste por 1 ano via cookie)
- Templates duplicados por idioma (ex.: `index.html` e `index_pt_br.html`)
- Testes automatizados garantem alternância e persistência

Para detalhes, veja `LANGUAGE_SYSTEM_SUMMARY.md`.