# Solução de Problemas

## Erros de Banco
- Delete o arquivo `soc_cmm.db` (apenas para uso local de testes)
- Recrie a base rodando os scripts de população

## Conflito de Porta
- Ajuste a porta em `main.py` (padrão: 8400)

## Dependências
- `pip install -r requirements.txt`

## Autenticação
- Limpe os cookies
- Verifique `SECRET_KEY`
- Confirme a existência da tabela `users`

## Logs
- Confira o console do servidor e do navegador