# Instalação

Este guia descreve a instalação local (modo desenvolvimento) e produção do
SOC CMM Assessment System.

## Pré-requisitos

- Python **3.11** ou superior
- `pip`
- Opcional: Docker e Docker Compose (para o fluxo containerizado)
- Opcional: `git` (para clonar o repositório)

## 1. Obter o código

```bash
git clone https://github.com/fernando-karl/soc_cmm_system.git
cd soc_cmm_system
```

## 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

> **Dica:** use um ambiente virtual (`python -m venv .venv && source .venv/bin/activate`) para isolar as dependências.

## 3. Configurar variáveis de ambiente

Copie o arquivo de exemplo e edite:

```bash
cp .env.example .env
```

| Variável                      | Obrigatória | Descrição                                                                                                  |
| ----------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------- |
| `SECRET_KEY`                  | **Sim**     | Chave usada para assinar os tokens JWT. A aplicação **não inicia** sem ela.                                |
| `ADMIN_PASSWORD`              | **Sim**¹    | Senha do usuário `admin` criado pela migração inicial.                                                      |
| `ALLOWED_ORIGINS`             | Não         | Lista CSV de origens CORS permitidas. Padrão: `http://localhost:8400`. Use `*` apenas em redes confiáveis. |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Não         | Tempo de vida do token JWT em minutos (padrão: `30`).                                                      |
| `HOST`                        | Não         | Interface de rede em que o servidor escuta (padrão: `0.0.0.0`).                                            |
| `PORT`                        | Não         | Porta TCP do servidor (padrão: `8400`).                                                                    |
| `ADMIN_EMAIL`                 | Não         | E-mail do usuário admin inicial (padrão: `admin@soc-cmm.local`).                                            |

¹ Necessária apenas para a migração inicial. Após o primeiro login, troque a
senha pela interface e remova a variável do ambiente.

Gere uma `SECRET_KEY` forte com:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

## 4. Inicializar o banco de dados

A primeira execução exige criar as tabelas de autenticação e o usuário admin
inicial:

```bash
export ADMIN_PASSWORD="sua-senha-forte-aqui"
python migrate_to_auth.py
```

O script cria as tabelas `users` necessárias, faz backup do banco existente e
cadastra o usuário `admin` com a senha vinda de `$ADMIN_PASSWORD`.

> Caso já exista um banco populado em outro nome, edite a variável `db_path` em
> `migrate_to_auth.py` ou renomeie o arquivo para
> `soc_cmm_translated.db`.

## 5. Iniciar a aplicação

```bash
python main.py
```

Acesse em <http://localhost:8400>. Para mudar a porta:

```bash
PORT=9000 python main.py
```

## Docker (alternativa)

Veja [`docker.md`](./docker.md) para o fluxo containerizado.

## Verificação

- A página inicial carrega em `http://localhost:${PORT:-8400}`.
- A documentação interativa da API fica em `/docs` (Swagger) e `/redoc`.
- Faça login com `admin` + `$ADMIN_PASSWORD` e troque a senha imediatamente.

## Solução de problemas

Consulte [`solucao_de_problemas.md`](./solucao_de_problemas.md) caso encontre
erros durante a instalação ou execução.
