# Autenticação

O sistema utiliza autenticação de usuários com tokens JWT e cookies HTTP-only.

## Recursos
- Registro e login de usuários
- Tokens JWT (expiração de 30min)
- Hash de senha (bcrypt)
- Escopo por usuário: cada usuário vê apenas seus clientes/avaliações

## Instalação e Migração
1. Instale dependências: `pip install -r requirements.txt`
2. Rode a migração: `python migrate_to_auth.py`
   - Cria tabelas de usuários e índices
   - Faz backup do banco atual
   - Cria usuário admin padrão (admin/(use-ADMIN_PASSWORD))
3. Inicie a aplicação: `python main.py`

Altere a senha padrão após o primeiro login.

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