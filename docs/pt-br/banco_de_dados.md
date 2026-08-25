# Banco de Dados

SQLite com as principais tabelas:
- `users` — contas e autenticação
- `customers` — clientes (com `user_id`)
- `assessments` — avaliações e status
- `domains` — domínios do SOC CMM
- `aspects` — aspectos por domínio
- `questions` — questões por aspecto
- `answer_options` — opções de resposta (nível de maturidade 1..5)
- `assessment_answers` — respostas do usuário
- `assessment_scores` — pontuações calculadas

Relacionamentos principais:
- User 1:N Customer
- Customer 1:N Assessment
- Domain 1:N Aspect
- Aspect 1:N Question
- Question 1:N AnswerOption

Scripts relevantes:
- `sql/schema/database_schema.sql` — esquema base
- `sql/seed/complete_populate_database.sql` — população
- Scripts `fix_*` — correções e migrações