-- Script para adicionar o campo guidance na tabela questions
-- SOC CMM Assessment System

-- Adicionar o campo guidance na tabela questions
ALTER TABLE questions ADD COLUMN guidance TEXT;

-- Comentário sobre a mudança
-- O campo guidance contém orientações e explicações adicionais para cada pergunta
-- Isso ajuda os usuários a entender melhor o que está sendo perguntado e como responder 