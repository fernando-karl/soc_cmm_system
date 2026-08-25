# Contribuindo

Obrigado por considerar contribuir com o SOC CMM Assessment System.

> **Licença:** Este projeto é **CC BY-SA 4.0**. Contribuições são aceitas
> sob a mesma licença. Leia [`LICENSE`](../../LICENSE) e
> [`NOTICE`](../../NOTICE). O software deriva do framework SOC-CMM® de
> Rob van Os (<https://www.soc-cmm.com>) e **não é afiliado** a
> soc-cmm.com.

Versão em inglês: [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).

## Ambiente de desenvolvimento

1. Faça fork e clone do repositório
2. Crie um virtualenv e instale: `pip install -r requirements.txt`
3. Copie `.env.example` para `.env` e defina `SECRET_KEY` e `ADMIN_PASSWORD`
4. Bootstrap de auth: `python scripts/migrate_to_auth.py`
5. Execute: `python main.py` (porta padrão `8400`)

**Não** faça commit de `.env`, `*.db` ou dados reais de avaliação.

## Pull requests

- Abra uma issue antes de mudanças grandes
- Mantenha PRs focados; uma mudança lógica por PR
- Atualize `docs/en/` e `docs/pt-br/` juntos quando o comportamento mudar
- Siga o estilo existente (FastAPI + templates Jinja2)
- Atualize testes `test_*.py` ao alterar auth ou API

## Contato

- Email do mantenedor: fernando.karl@gmail.com
- Issues: <https://github.com/fernando-karl/soc_cmm_system/issues>
