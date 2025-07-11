-- Script de migração completo para SOC CMM Assessment System
-- Este script corrige:
-- 1. Aspect IDs para usar códigos corretos ("1.1", "2.1", etc.)
-- 2. Questões sem opções de resposta
-- 3. Possíveis duplicações

BEGIN TRANSACTION;

PRAGMA foreign_keys = OFF;

-- ========================================
-- PARTE 1: CORRIGIR ASPECT IDs
-- ========================================

-- 1.1 Criar nova tabela aspects com ID como VARCHAR
CREATE TABLE aspects_new (
    id VARCHAR(10) PRIMARY KEY,
    domain_id INTEGER NOT NULL,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    order_index INTEGER NOT NULL,
    FOREIGN KEY (domain_id) REFERENCES domains(id)
);

-- 1.2 Inserir dados existentes usando o código como ID
INSERT INTO aspects_new (id, domain_id, name, description, order_index)
SELECT code, domain_id, name, description, order_index
FROM aspects;

-- 1.3 Criar tabela temporária para mapear aspect_id antigo para novo
CREATE TEMPORARY TABLE aspect_id_mapping AS
SELECT 
    old.id as old_aspect_id,
    new.id as new_aspect_id
FROM aspects old
JOIN aspects_new new ON old.code = new.id;

-- 1.4 Atualizar as questões para usar os novos aspect_id
UPDATE questions 
SET aspect_id = (
    SELECT aim.new_aspect_id 
    FROM aspect_id_mapping aim 
    WHERE aim.old_aspect_id = questions.aspect_id
);

-- 1.5 Dropar a tabela antiga e renomear a nova
DROP TABLE aspects;
ALTER TABLE aspects_new RENAME TO aspects;

-- 1.6 Recriar índices
CREATE INDEX idx_aspects_domain ON aspects(domain_id);

-- ========================================
-- PARTE 2: ADICIONAR OPÇÕES DE RESPOSTA FALTANTES
-- ========================================

-- 2.1 Adicionar opções de resposta para questões 546-565
-- Questão 546: End-point log collection
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(546, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(546, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(546, 'Yes', 3, 3);

-- Questão 547: Application log collection
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(547, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(547, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(547, 'Yes', 3, 3);

-- Questão 548: Database log collection
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(548, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(548, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(548, 'Yes', 3, 3);

-- Questão 549: Network flow data collection
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(549, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(549, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(549, 'Yes', 3, 3);

-- Questão 550: Network device log collection
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(550, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(550, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(550, 'Yes', 3, 3);

-- Questão 551: Security device log collection
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(551, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(551, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(551, 'Yes', 3, 3);

-- Questão 552: Centralized aggregation and storage
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(552, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(552, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(552, 'Yes', 3, 3);

-- Questão 553: Multiple retention periods
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(553, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(553, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(553, 'Yes', 3, 3);

-- Questão 554: Secure log transfer
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(554, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(554, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(554, 'Yes', 3, 3);

-- Questão 555: Support for multiple log formats
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(555, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(555, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(555, 'Yes', 3, 3);

-- Questão 556: Support for multiple transfer techniques
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(556, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(556, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(556, 'Yes', 3, 3);

-- Questão 557: Data normalization
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(557, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(557, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(557, 'Yes', 3, 3);

-- Questão 558: Log searching and filtering
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(558, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(558, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(558, 'Yes', 3, 3);

-- Questão 559: Alerting
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(559, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(559, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(559, 'Yes', 3, 3);

-- Questão 560: Reporting and dashboards
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(560, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(560, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(560, 'Yes', 3, 3);

-- Questão 561: Log tampering detection
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(561, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(561, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(561, 'Yes', 3, 3);

-- Questão 562: Log collection policy
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(562, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(562, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(562, 'Yes', 3, 3);

-- Questão 563: Logging policy
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(563, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(563, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(563, 'Yes', 3, 3);

-- Questão 564: Data retention policy
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(564, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(564, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(564, 'Yes', 3, 3);

-- Questão 565: Privacy and Sensitive data handling policy
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(565, 'No', 1, 1);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(565, 'Partially', 2, 2);
INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES
(565, 'Yes', 3, 3);

-- ========================================
-- PARTE 3: REMOVER DUPLICAÇÕES
-- ========================================

-- 3.1 Remover opções de resposta duplicadas
DELETE FROM answer_options 
WHERE id NOT IN (
    SELECT MIN(id)
    FROM (
        SELECT id, question_id, option_text, maturity_level, order_index
        FROM answer_options
    ) AS temp
    GROUP BY question_id, option_text, maturity_level, order_index
);

-- 3.2 Corrigir ordem das opções de resposta baseado no nível de maturidade
UPDATE answer_options 
SET order_index = (
    SELECT rn 
    FROM (
        SELECT id, ROW_NUMBER() OVER (PARTITION BY question_id ORDER BY maturity_level) as rn
        FROM answer_options
    ) AS temp 
    WHERE temp.id = answer_options.id
)
WHERE order_index != (
    SELECT rn 
    FROM (
        SELECT id, ROW_NUMBER() OVER (PARTITION BY question_id ORDER BY maturity_level) as rn
        FROM answer_options
    ) AS temp2 
    WHERE temp2.id = answer_options.id
);

-- ========================================
-- PARTE 4: VERIFICAÇÃO FINAL
-- ========================================

PRAGMA foreign_keys = ON;

-- 4.1 Verificar se todas as correções foram aplicadas
SELECT 
    'RELATÓRIO DE MIGRAÇÃO' as section,
    '===================' as separator;

SELECT 
    'Aspects com códigos corretos:' as metric,
    COUNT(*) as count
FROM aspects
WHERE id LIKE '%.%';

SELECT 
    'Questões sem opções de resposta:' as metric,
    COUNT(*) as count
FROM questions q
LEFT JOIN answer_options ao ON q.id = ao.question_id
WHERE q.question_type = 'multiple_choice' AND ao.id IS NULL;

SELECT 
    'Opções de resposta duplicadas:' as metric,
    COUNT(*) as count
FROM (
    SELECT question_id, option_text, maturity_level, order_index, COUNT(*) as cnt
    FROM answer_options
    GROUP BY question_id, option_text, maturity_level, order_index
    HAVING COUNT(*) > 1
) AS duplicates;

SELECT 
    'Total de aspects:' as metric,
    COUNT(*) as count
FROM aspects;

SELECT 
    'Total de questões:' as metric,
    COUNT(*) as count
FROM questions
WHERE question_type = 'multiple_choice';

SELECT 
    'Total de opções de resposta:' as metric,
    COUNT(*) as count
FROM answer_options;

-- 4.2 Mostrar alguns exemplos de aspects com códigos corretos
SELECT 
    'EXEMPLOS DE ASPECTS:' as section,
    '==================' as separator;

SELECT 
    id as aspect_code,
    name,
    domain_id
FROM aspects
ORDER BY id
LIMIT 10;

COMMIT;

SELECT 'MIGRAÇÃO CONCLUÍDA COM SUCESSO!' as status; 