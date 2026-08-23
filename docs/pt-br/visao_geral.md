# Visão Geral

O **SOC CMM Assessment System** é uma aplicação web para conduzir avaliações
de maturidade de SOC (Security Operations Center) com base no framework
**SOC-CMM®** publicado por **Rob van Os** (<https://www.soc-cmm.com>).

## Capacidades principais

- Cadastro e gestão de clientes (organizações avaliadas).
- Criação de avaliações por cliente, com salvamento incremental.
- Questionário guiado pelos seis domínios do SOC-CMM® (Business, People,
  Process, Technology, Services, Results) e seus aspectos (baseado no
  SOC-CMM® 2.3.3 basic).
- Cálculo automático de pontuações na escala de maturidade do SOC-CMM®
  (0–5: Inexistente → Otimizando), conforme as opções de resposta do
  questionário.
- Visualização em gráfico **radar**, com comparação histórica entre
  avaliações do mesmo cliente.
- Autenticação por usuário (JWT + cookie HTTP-only) e isolamento total de
  dados por conta.
- Recursos administrativos: dashboard, gestão de usuários, exclusão e
  promoção a admin.
- Interface bilíngue **EN / PT-BR** com troca em tempo real.
- Integração com **MCP (Model Context Protocol)** para uso por modelos de IA.
- API REST documentada em `/docs` (Swagger) e `/redoc`.

## Stack

- **Backend:** FastAPI (Python 3.11+), SQLite, Jinja2.
- **Auth:** JWT (`python-jose`), bcrypt (`passlib`).
- **Frontend:** HTML/CSS/JS, Chart.js, Font Awesome.
- **Containerização:** Docker + Docker Compose.

## Porta padrão

`8400`. Configurável via variável de ambiente `PORT`. Acesse
<http://localhost:8400>.

## Licença e atribuição

O projeto deriva do framework SOC-CMM® (CC BY-SA 4.0) e, portanto, é
distribuído sob a mesma licença **Creative Commons Attribution-ShareAlike
4.0 International (CC BY-SA 4.0)**. Detalhes em `LICENSE` e `NOTICE` na
raiz do repositório. Este projeto **não é afiliado, endossado ou
patrocinado** por Rob van Os ou soc-cmm.com.

Contato do mantenedor: fernando.karl@gmail.com ·
[GitHub Issues](https://github.com/fernando-karl/soc_cmm_system/issues).

## Próximos passos

- [Instalação](./instalacao.md)
- [Uso](./uso.md)
- [Autenticação](./autenticacao.md)
- [API](./api.md)
- [Docker](./docker.md)
- [Solução de problemas](./solucao_de_problemas.md)
