# Solução de Problemas

## A aplicação não inicia (`SECRET_KEY environment variable is required`)

A `SECRET_KEY` precisa estar definida no ambiente. Defina-a antes de iniciar:

```bash
export SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
python main.py
```

Para Docker, defina no `.env` carregado pelo `docker-compose.yml`.

## A migração falha com `ADMIN_PASSWORD environment variable is required`

A criação do usuário admin inicial exige `ADMIN_PASSWORD`:

```bash
export ADMIN_PASSWORD="senha-forte"
python migrate_to_auth.py
```

## Conflito de porta

A porta padrão é `8400`. Para mudar:

```bash
PORT=9000 python main.py
```

Em Docker: `PORT=9000 docker compose up -d`.

## Erros de banco de dados

- Verifique se o arquivo `soc_cmm_translated.db` existe e tem permissão de
  escrita.
- Confirme que a tabela `users` foi criada (rode `migrate_to_auth.py`).
- Em ambiente local de testes, é possível apagar o `.db` e recriar a base
  rodando os scripts de população (`run_populate_database_fixed.py`).

## Problemas de autenticação

- Limpe os cookies do navegador (token expirado ou cookie antigo).
- Confirme que `SECRET_KEY` é a mesma usada para emitir o token (após troca,
  todos os usuários precisam fazer login novamente).
- Cheque os logs do servidor para erros de JWT.

## Erros de CORS no navegador

A origem de onde a requisição parte precisa estar em `ALLOWED_ORIGINS`:

```bash
export ALLOWED_ORIGINS="https://app.exemplo.com,https://admin.exemplo.com"
```

Use `*` apenas em redes confiáveis e desabilite credenciais
(`allow_credentials=False` é aplicado automaticamente quando `*` é o único
valor).

## Dependências

```bash
pip install -r requirements.txt
```

Se ocorrer erro de versão, garanta Python 3.11+ (`python --version`).

## Logs

- Console do servidor (uvicorn) — mostra requisições, erros e stack traces.
- Console do navegador (DevTools) — mostra erros de JS e CORS.
- Em Docker: `docker compose logs -f soc-cmm`.
