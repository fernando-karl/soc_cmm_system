-- Script para atualizar o schema da tabela aspects
-- Permite usar códigos como "1.1", "2.1", etc. como IDs

BEGIN TRANSACTION;

-- 1. Desabilitar foreign keys temporariamente
PRAGMA foreign_keys = OFF;

-- 2. Criar nova tabela aspects com ID como VARCHAR
CREATE TABLE aspects_new (
    id VARCHAR(10) PRIMARY KEY,
    domain_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL,
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- 3. Inserir dados existentes usando o código como ID
INSERT INTO aspects_new (id, domain_id, name, description, order_index)
SELECT code, domain_id, name, description, order_index
FROM aspects;

-- 4. Criar tabela temporária para mapear aspect_id antigo para novo
CREATE TEMPORARY TABLE aspect_id_mapping AS
SELECT 
    old.id as old_aspect_id,
    new.id as new_aspect_id
FROM aspects old
JOIN aspects_new new ON old.code = new.id;

-- 5. Atualizar as questões para usar os novos aspect_id
UPDATE questions 
SET aspect_id = (
    SELECT aim.new_aspect_id 
    FROM aspect_id_mapping aim 
    WHERE aim.old_aspect_id = questions.aspect_id
);

-- 6. Dropar a tabela antiga e renomear a nova
DROP TABLE aspects;
ALTER TABLE aspects_new RENAME TO aspects;

-- 7. Recriar índices
CREATE INDEX idx_aspects_domain ON aspects(domain_id);

-- 8. Reabilitar foreign keys
PRAGMA foreign_keys = ON;

-- 9. Verificar se tudo está funcionando
SELECT 
    'Verificação final:' as info,
    'Total de aspects' as metric,
    COUNT(*) as count
FROM aspects

UNION ALL

SELECT 
    'Verificação final:' as info,
    'Total de questões' as metric,
    COUNT(*) as count
FROM questions

UNION ALL

SELECT 
    'Verificação final:' as info,
    'Questões com aspect_id válido' as metric,
    COUNT(*) as count
FROM questions q
JOIN aspects a ON q.aspect_id = a.id;

-- 10. Mostrar alguns exemplos
SELECT 
    'Exemplos de aspects:' as info,
    id as aspect_code,
    name,
    domain_id
FROM aspects
ORDER BY id
LIMIT 5;

COMMIT;

SELECT 'Schema atualizado com sucesso!' as status; 