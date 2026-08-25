-- Script para verificar e corrigir duplicações nas opções de resposta
-- Este script identifica e remove opções de resposta duplicadas

-- 1. Verificar questões que não têm opções de resposta
SELECT 
    q.id as question_id,
    q.question_text,
    COUNT(ao.id) as answer_options_count
FROM questions q
LEFT JOIN answer_options ao ON q.id = ao.question_id
WHERE q.question_type = 'multiple_choice'
GROUP BY q.id, q.question_text
HAVING COUNT(ao.id) = 0
ORDER BY q.id;

-- 2. Verificar opções de resposta duplicadas por questão
SELECT 
    ao.question_id,
    ao.option_text,
    ao.maturity_level,
    ao.order_index,
    COUNT(*) as duplicate_count
FROM answer_options ao
GROUP BY ao.question_id, ao.option_text, ao.maturity_level, ao.order_index
HAVING COUNT(*) > 1
ORDER BY ao.question_id, ao.order_index;

-- 3. Remover opções de resposta duplicadas (manter apenas a primeira ocorrência)
-- Este comando remove duplicações mantendo apenas a primeira ocorrência de cada combinação
DELETE FROM answer_options 
WHERE id NOT IN (
    SELECT MIN(id)
    FROM (
        SELECT id, question_id, option_text, maturity_level, order_index
        FROM answer_options
    ) AS temp
    GROUP BY question_id, option_text, maturity_level, order_index
);

-- 4. Verificar se há questões com opções de resposta em ordem incorreta
SELECT 
    ao.question_id,
    ao.option_text,
    ao.order_index,
    ROW_NUMBER() OVER (PARTITION BY ao.question_id ORDER BY ao.maturity_level) as expected_order
FROM answer_options ao
WHERE ao.order_index != ROW_NUMBER() OVER (PARTITION BY ao.question_id ORDER BY ao.maturity_level)
ORDER BY ao.question_id, ao.order_index;

-- 5. Corrigir ordem das opções de resposta baseado no nível de maturidade
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

-- 6. Verificar integridade final
SELECT 
    'Questões sem opções de resposta' as check_type,
    COUNT(*) as count
FROM questions q
LEFT JOIN answer_options ao ON q.id = ao.question_id
WHERE q.question_type = 'multiple_choice' AND ao.id IS NULL

UNION ALL

SELECT 
    'Opções de resposta duplicadas' as check_type,
    COUNT(*) as count
FROM (
    SELECT question_id, option_text, maturity_level, order_index, COUNT(*) as cnt
    FROM answer_options
    GROUP BY question_id, option_text, maturity_level, order_index
    HAVING COUNT(*) > 1
) AS duplicates

UNION ALL

SELECT 
    'Total de questões' as check_type,
    COUNT(*) as count
FROM questions
WHERE question_type = 'multiple_choice'

UNION ALL

SELECT 
    'Total de opções de resposta' as check_type,
    COUNT(*) as count
FROM answer_options; 