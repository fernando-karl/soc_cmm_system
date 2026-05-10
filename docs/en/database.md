# Database

SQLite, with the following main tables:

- `users` — accounts and authentication
- `customers` — customers (with `user_id` foreign key)
- `assessments` — assessments and their status
- `domains` — SOC-CMM domains
- `aspects` — aspects per domain
- `questions` — questions per aspect
- `answer_options` — answer options (maturity level 1..5)
- `assessment_answers` — user-submitted answers
- `assessment_scores` — computed scores

Main relationships:

- User 1:N Customer
- Customer 1:N Assessment
- Domain 1:N Aspect
- Aspect 1:N Question
- Question 1:N AnswerOption

Relevant scripts:

- `database_schema.sql` — base schema
- `complete_populate_database.sql` — data population
- `fix_*` scripts — fixes and migrations
