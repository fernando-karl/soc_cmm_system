# Instalação

## Pré-requisitos
- Python 3.11+
- pip

## Passos
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicie a aplicação:
   ```bash
   python main.py
   ```
3. Acesse em `http://localhost:8400`.

## Variáveis de Ambiente (produção)
- `SECRET_KEY`: chave segura para assinatura de tokens JWT

## Docker
- Subir com Docker Compose:
  ```bash
  docker-compose up -d
  ```

- Dockerfile básico já incluso no projeto.