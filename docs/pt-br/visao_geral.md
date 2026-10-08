# Visão Geral

O **SOC CMM Assessment System** é uma aplicação web para conduzir avaliações
de maturidade de SOC (Security Operations Center) com base no framework
**SOC-CMM®** publicado por **Rob van Os** (<https://www.soc-cmm.com>).

## Capacidades principais

- Cadastro e gestão de clientes (organizações avaliadas).
- Criação de avaliações por cliente, com salvamento incremental.
- Questionário guiado pelos cinco domínios pontuados do SOC-CMM® (Business,
  People, Process, Technology, Services) e seus 27 aspectos — 649 questões do
  SOC-CMM® 2.4.2 advanced. `Results` é a seção de saída da planilha, não um
  domínio pontuado.
- Cálculo automático a partir de cinco níveis de maturidade por questão,
  seguindo a fórmula da planilha oficial do SOC-CMM®, inclusive a ponderação
  por importância — veja a seção Pontuação abaixo.
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

As pontuações seguem a **planilha oficial do SOC-CMM® 2.4.2 (advanced)**, de
modo que um número desta ferramenta é comparável com um número da planilha.

Cada opção de resposta tem um nível de maturidade de 1 a 5. Para um aspecto,
sobre as questões respondidas, com resposta `a` e fator de importância `h`:

```
total = SUM(a × h)      max = SUM(5 × h)      min = SUM(h)
percentual = 100 × (total − min) / (max − min)
```

o que equivale a uma média de `(a − 1) / 4` ponderada pelo fator. A maturidade
na escala conhecida de 0 a 5 é `5 × percentual / 100`, e a nota de um domínio é
a média simples dos seus aspectos — ambas como a aba de resultados da planilha
as calcula.

Duas consequências da fórmula:

- **A escala é normalizada pela sua amplitude, não pelo seu topo.** A resposta
  mais baixa vale **0%**, então um SOC que não tem determinada capacidade
  aparece como zero, e não como 20%.
- **As questões são ponderadas por importância.** Cada resposta carrega uma
  importância para aquele SOC — `none`, `low`, `normal`, `high`, `critical` —
  que corresponde a um fator de 0, 0,5, 1, 2 ou 4 (aba `_Score matrix` da
  planilha). Uma questão marcada como `none` sai inteiramente do cálculo. Envie
  `importance` em `POST /api/answers`; o padrão é `normal`, que é como todas as
  questões vêm na planilha, e com tudo em `normal` a ponderação não tem efeito
  e a nota é a média simples de `(a − 1) / 4`.

Onde o fator se cancela — dentro de uma mesma questão e num aspecto cujas
questões compartilham a mesma importância — a ponderação não muda nada. Ela só
altera o resultado quando um aspecto mistura importâncias.

Duas partes da planilha **não** são reproduzidas aqui: ela acompanha completude
separadamente da maturidade e tem a sua própria aba de pontuação NIST CSF. Cada
questão continua trazendo o seu mapeamento NIST CSF 2.0 no conjunto de dados.

> **Atualizando:** as pontuações gravadas por uma versão anterior a esta mudança
> foram calculadas como `média(a) / 5`, em que a resposta mais baixa valia 20%.
> O `scripts/init_db.py` as recalcula a partir das respostas armazenadas e avisa
> quando o faz. Espere que os percentuais **caiam**; as respostas em si não são
> alteradas.

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
