# Uso (Interface Web)

Esta página descreve o fluxo típico de uso da aplicação web, do primeiro
login até a visualização dos resultados.

## 1. Login e cadastro

Após instalar a aplicação (ver [`instalacao.md`](./instalacao.md)) e iniciar
o servidor, acesse <http://localhost:8400>:

- **Primeiro acesso (administrador):** entre com o usuário `admin` e a senha
  definida em `ADMIN_PASSWORD`. Logo em seguida, abra a página de perfil e
  altere a senha.
- **Cadastro de novos usuários:** acesse `/register` para criar uma conta
  individual. Cada usuário só vê seus próprios clientes e avaliações.
- **Logout:** disponível no menu superior; limpa o cookie de sessão.

> Os tokens JWT expiram em 30 minutos por padrão (configurável via
> `ACCESS_TOKEN_EXPIRE_MINUTES`). A sessão também é mantida em cookie
> HTTP-only.

## 2. Gerenciar clientes

1. Vá em **Clientes** no menu.
2. Clique em **Adicionar Cliente** e informe nome, e-mail (opcional) e
   organização (opcional).
3. Cada cliente fica vinculado ao usuário que o criou — outros usuários não
   conseguem visualizá-lo.
4. Use a busca para localizar clientes pela lista.

## 3. Criar e responder uma avaliação

1. Na lista de clientes, clique em **Nova Avaliação**.
2. O sistema redireciona para o questionário.
3. As perguntas estão organizadas pelos cinco domínios pontuados do SOC-CMM®:
   - **Business** (estratégia, governança, custos, privacidade)
   - **People** (contratação, treinamento, desempenho)
   - **Process** (gestão, operação, relatórios, casos de uso)
   - **Technology** (SIEM, detecção, analytics)
   - **Services** (catálogo, threat hunting, vulnerabilidades)
4. Cada domínio contém **aspectos** com perguntas. Selecione um aspecto para
   ver suas questões.
5. Tipos de pergunta suportados:
   - Cinco níveis de maturidade, de 1 a 5, cada um descrito nas palavras
     da própria questão em vez de um rótulo genérico. A pior resposta
     disponível é o nível 1, que vale 20% — veja a seção Pontuação de
     [visao_geral.md](visao_geral.md) para entender por quê, e como isso difere da planilha oficial
   - Múltipla escolha
   - Numérica
   - Texto livre
   - Checkbox
6. As respostas são salvas automaticamente. O indicador de progresso mostra
   quantas perguntas faltam.
7. Quando todos os aspectos estiverem completos, clique em **Concluir
   Avaliação**.

## 4. Ver resultados

Ao concluir, a página de resultados exibe:

- **Gráfico radar** com a maturidade por domínio.
- **Pontuações detalhadas** por domínio e aspecto.
- **Comparação** com avaliações anteriores do mesmo cliente, quando houver.
- **Exportação** dos dados para análise externa.

## 5. Acompanhar progresso ao longo do tempo

Crie múltiplas avaliações para o mesmo cliente. A página de progresso mostra
gráficos de evolução por domínio e aspecto, permitindo acompanhar a
maturação do SOC ao longo de meses ou trimestres.

## 6. Trocar idioma (EN/PT-BR)

- Clique nas bandeiras 🇺🇸 / 🇧🇷 no topo da tela.
- A preferência é gravada num cookie `language` (válido por 1 ano).
- Também é possível trocar via URL: `?lang=pt_br` ou
  `/change-language/{language}`.

Detalhes em [`idiomas.md`](./idiomas.md).

## 7. Recursos administrativos

Apenas usuários com `is_admin = TRUE` veem os menus administrativos. Veja
[`administracao.md`](./administracao.md) para detalhes do dashboard, gestão
de usuários e operações privilegiadas.

## 8. API e MCP

- **REST API:** referência rápida em [`api.md`](./api.md). Documentação
  interativa em `/docs` (Swagger) ou `/redoc`. Use o token JWT no header
  `Authorization: Bearer <token>`.
- **MCP (Model Context Protocol):** integração com modelos de IA — veja
  [`mcp.md`](./mcp.md).

## Próximos passos

- [Instalação detalhada](./instalacao.md)
- [Autenticação](./autenticacao.md)
- [Solução de problemas](./solucao_de_problemas.md)
