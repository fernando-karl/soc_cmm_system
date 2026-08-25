-- Script principal para corrigir problemas no banco de dados SOC CMM
-- Este script resolve questões sem opções de resposta e remove duplicações

BEGIN TRANSACTION;

-- 1. Primeiro, vamos verificar o estado atual do banco
PRAGMA foreign_keys = ON;

-- 2. Adicionar opções de resposta para questões 546-565 que estão faltando
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

-- 3. Remover opções de resposta duplicadas (se houver)
DELETE FROM answer_options 
WHERE id NOT IN (
    SELECT MIN(id)
    FROM (
        SELECT id, question_id, option_text, maturity_level, order_index
        FROM answer_options
    ) AS temp
    GROUP BY question_id, option_text, maturity_level, order_index
);

-- 4. Corrigir ordem das opções de resposta baseado no nível de maturidade
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

-- 5. Verificar se todas as correções foram aplicadas com sucesso
SELECT 
    'Questões sem opções de resposta' as check_type,
    COUNT(*) as count
FROM questions q
LEFT JOIN answer_options ao ON q.id = ao.question_id
WHERE q.question_type = 'multiple_choice' AND ao.id IS NULL;

-- Se o resultado acima for 0, então todas as questões têm opções de resposta
-- Se for maior que 0, há ainda questões sem opções de resposta

COMMIT;

-- Mensagem de conclusão
SELECT 'Correções aplicadas com sucesso!' as status; 