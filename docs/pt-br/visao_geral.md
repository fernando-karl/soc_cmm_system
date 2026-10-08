# Visão Geral

O **SOC CMM Assessment System** é uma aplicação web para conduzir avaliações
de maturidade de SOC (Security Operations Center) com base no framework
**SOC-CMM®** publicado por **Rob van Os** (<https://www.soc-cmm.com>).

## Capacidades principais

- Cadastro e gestão de clientes (organizações avaliadas).
- Criação de avaliações por cliente, com salvamento incremental.
- Questionário guiado pelos cinco domínios pontuados do SOC-CMM® (Business,
  People, Process, Technology, Services) e seus 27 aspectos — 622 questões do
  SOC-CMM® 2.4.2 advanced. `Results` é a seção de saída da planilha, não um
  domínio pontuado.
- Cálculo automático a partir de cinco níveis de maturidade por questão. O
  método é uma média simples e difere da planilha oficial — veja a seção Pontuação
  abaixo.
- Visualização em gráfico **radar**, com comparação histórica entre
  avaliações do mesmo cliente.
- Autenticação por usuário (JWT + cookie HTTP-only) e isolamento total de
  dados por conta.
- Recursos administrativos: dashboard, gestão de usuários, exclusão e
  promoção a admin.
- Interface bilíngue **EN / PT-BR** com troca em tempo real.
- Integração com **MCP (Model Context Protocol)** para uso por modelos de IA.
- API REST documentada em `/docs` (Swagger) e `/redoc`.

## Pontuação

A pontuação de maturidade é uma **média simples, deliberadamente mais simples
que a da planilha oficial**. Leia isto antes de comparar um número desta
ferramenta com um número da planilha do SOC-CMM® — eles não são calculados da
mesma forma.

Cada opção de resposta tem um nível de maturidade de 1 a 5. A nota de um aspecto
é a média não ponderada das questões respondidas, a de um domínio é a média não
ponderada dos seus aspectos, e o percentual é `nota / 5 × 100`.

A planilha do SOC-CMM® 2.4.2 (advanced) difere em dois pontos que importam:

- **Ela normaliza a partir da base da escala.** O percentual por questão é
  `100 × (resposta − 1) / 4`, então a resposta mais baixa vale **0%**. Aqui, a
  mesma resposta vale 20%, porque o divisor é o topo da escala e não a sua
  amplitude. Um SOC que responda sempre no nível mais baixo aparece como 0% na
  planilha e 20% aqui.
- **Ela pondera as questões por importância.** Quem avalia marca cada questão
  como `none`, `low`, `normal`, `high` ou `critical`, o que corresponde a um
  fator de 0, 0,5, 1, 2 ou 4 (`_Score matrix`), e os totais por aspecto são
  somas ponderadas em vez de médias simples. Uma questão marcada como `none`
  sai inteiramente do cálculo. Esta ferramenta trata todas as questões como
  igualmente importantes. (Na planilha distribuída todas as questões vêm como
  `normal`, então a ponderação só passa a valer quando o avaliador a altera.)

A planilha também acompanha completude separadamente da maturidade e tem sua
própria aba de pontuação NIST CSF; nenhuma das duas é reproduzida aqui.

Nada disso torna os números errados, mas torna-os **os números desta
ferramenta**. Use-os para comparar um SOC consigo mesmo ao longo do tempo, que é
a função do gráfico de evolução. Para um número a ser apresentado a um auditor
ou comparado com o resultado SOC-CMM® de outra organização, use a planilha
oficial.

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
