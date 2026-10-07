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

## 4. Criar o banco de dados

Um único comando monta um banco funcional do zero:

```bash
export ADMIN_PASSWORD="sua-senha-forte-aqui"
python scripts/init_db.py
```

Ele aplica o esquema base, as tabelas de tradução e as migrações, popula o
questionário a partir de `dataset/` e cria a conta `admin` com a senha de
`$ADMIN_PASSWORD`. Sem essa variável o banco é criado da mesma forma e você
registra o primeiro usuário pela interface web.

O script é **idempotente** — rodar de novo acrescenta o que faltar e preserva
os dados existentes, então use-o também depois de atualizar o repositório com
novas migrações. `--recreate` apaga o banco antes e pede confirmação; isso
destrói todos os usuários, clientes e avaliações.

O arquivo do banco é `soc_cmm_bilingual.db`, ao lado do código da aplicação, ou
onde `DB_PATH` apontar.

> **Cobertura do questionário:** o conjunto de dados distribuído define as 97
> questões, mas opções de resposta para apenas 11 delas, então as demais ainda
> não podem ser pontuadas. O script avisa sobre isso ao rodar. Veja
> `sql/README.md`.

> Atualizando um banco anterior à autenticação? Use
> `python scripts/migrate_to_auth.py`, que acrescenta as tabelas `users` a um
> banco já existente.

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
