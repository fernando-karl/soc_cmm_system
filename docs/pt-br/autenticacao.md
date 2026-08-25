# Autenticação

O sistema utiliza autenticação de usuários com tokens JWT e cookies HTTP-only.

## Recursos
- Registro e login de usuários
- Tokens JWT (expiração de 30min)
- Hash de senha (bcrypt)
- Escopo por usuário: cada usuário vê apenas seus clientes/avaliações

## Instalação e Migração
1. Instale dependências: `pip install -r requirements.txt`
2. Configure o ambiente: `cp .env.example .env` e defina **`SECRET_KEY`** e
   **`ADMIN_PASSWORD`** (a aplicação não inicia sem `SECRET_KEY` e a migração
   aborta sem `ADMIN_PASSWORD`).
3. Rode a migração: `python scripts/migrate_to_auth.py`
   - Cria tabelas de usuários e índices
   - Faz backup do banco atual
   - Cria usuário `admin` com a senha definida em `$ADMIN_PASSWORD`
4. Inicie a aplicação: `python main.py`

Altere a senha do admin após o primeiro login e remova `ADMIN_PASSWORD` do
ambiente.

## API
Inclua o token JWT no header:
```
Authorization: Bearer <seu-token>
```

## Variáveis de Ambiente
- `SECRET_KEY`: chave secreta para assinar tokens

## Dicas de Segurança
- Senhas com 8+ caracteres, armazenadas como hash
- Cookies HTTP-only
- Controle de acesso por usuário e por rotas

## Problemas Comuns
- Limpe cookies do navegador
- Verifique `SECRET_KEY`
- Confirme a existência da tabela `users`
- Cheque logs para erros de JWT