-- Script para corrigir os aspect_id para usar os códigos corretos
-- Este script altera a estrutura da tabela aspects para usar os códigos como IDs

BEGIN TRANSACTION;

-- 1. Primeiro, vamos criar uma tabela temporária para armazenar o mapeamento atual
CREATE TEMPORARY TABLE aspect_mapping AS
SELECT 
    id as old_id,
    code as new_id,
    domain_id,
    name,
    description,
    order_index
FROM aspects;

-- 2. Verificar o mapeamento
SELECT 
    'Mapeamento atual:' as info,
    old_id,
    new_id,
    name
FROM aspect_mapping
ORDER BY old_id;

-- 3. Atualizar as referências nas questões para usar os códigos corretos
-- Primeiro, vamos adicionar uma coluna temporária para o novo aspect_id
ALTER TABLE questions ADD COLUMN new_aspect_id VARCHAR(10);

-- 4. Atualizar a nova coluna com os códigos corretos
UPDATE questions 
SET new_aspect_id = (
    SELECT am.new_id 
    FROM aspect_mapping am 
    WHERE am.old_id = questions.aspect_id
);

-- 5. Verificar se todas as questões foram mapeadas corretamente
SELECT 
    'Questões sem aspect_id válido:' as check_type,
    COUNT(*) as count
FROM questions 
WHERE new_aspect_id IS NULL;

-- 6. Se tudo estiver correto, vamos alterar a estrutura da tabela aspects
-- Primeiro, vamos dropar as foreign keys
PRAGMA foreign_keys = OFF;

-- 7. Criar nova tabela aspects com o código como ID
CREATE TABLE aspects_new (
    id VARCHAR(10) PRIMARY KEY,
    domain_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL,
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- 8. Inserir dados na nova tabela
INSERT INTO aspects_new (id, domain_id, name, description, order_index)
SELECT new_id, domain_id, name, description, order_index
FROM aspect_mapping;

-- 9. Atualizar as questões para usar os novos IDs
UPDATE questions 
SET aspect_id = new_aspect_id;

-- 10. Remover a coluna temporária
ALTER TABLE questions DROP COLUMN new_aspect_id;

-- 11. Dropar a tabela antiga e renomear a nova
DROP TABLE aspects;
ALTER TABLE aspects_new RENAME TO aspects;

-- 12. Recriar os índices
CREATE INDEX idx_aspects_domain ON aspects(domain_id);

-- 13. Reativar foreign keys
PRAGMA foreign_keys = ON;

-- 14. Verificar se tudo está funcionando
SELECT 
    'Total de aspects:' as info,
    COUNT(*) as count
FROM aspects;

SELECT 
    'Total de questões:' as info,
    COUNT(*) as count
FROM questions;

SELECT 
    'Questões com aspect_id válido:' as info,
    COUNT(*) as count
FROM questions q
JOIN aspects a ON q.aspect_id = a.id;

-- 15. Mostrar alguns exemplos de aspectos com seus códigos corretos
SELECT 
    'Exemplos de aspects:' as info,
    id as aspect_code,
    name,
    domain_id
FROM aspects
ORDER BY id
LIMIT 10;

COMMIT;

-- Mensagem de conclusão
SELECT 'Aspect IDs corrigidos com sucesso!' as status; 