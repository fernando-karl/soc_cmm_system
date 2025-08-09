# Administração

## Recursos
- Dashboard `/admin` com estatísticas (usuários, clientes, avaliações, andamento)
- Gráficos (Chart.js): status de avaliações e crescimento mensal
- Lista de usuários `/admin/users` com busca, edição e exclusão
- Páginas: editar usuário, novo usuário, alterar senha

## Backend
- Novas rotas de admin no `main.py` (páginas + API)
- Métodos no `database.py` para buscar/atualizar/deletar usuários e estatísticas
- Métodos no `auth.py` para atualizar dados e senha do usuário

## Segurança
- Autenticação obrigatória para páginas de admin
- Requisitos de senha e validação de dados
- Usuários não podem excluir a si próprios

## Melhorias Futuras
- Perfis de acesso (RBAC)
- Auditoria de ações
- Operações em massa e exportação