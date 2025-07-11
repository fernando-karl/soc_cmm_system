#!/usr/bin/env python3
"""
Script para criar banco de dados SOC CMM em português com aspect_id corretos
Baseado no arquivo soc_cmm_questions-port.json
"""

import json
import sqlite3
import os
from typing import Dict, List, Any

def create_database_schema(db_path: str):
    """
    Cria o schema do banco de dados com a estrutura correta
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Criar tabela customers
    cursor.execute('''
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            organization VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Criar tabela domains
    cursor.execute('''
        CREATE TABLE domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            order_index INTEGER NOT NULL
        )
    ''')
    
    # Criar tabela aspects
    cursor.execute('''
        CREATE TABLE aspects (
            id VARCHAR(20) PRIMARY KEY,
            domain_id INTEGER NOT NULL,
            name VARCHAR(100) NOT NULL,
            description TEXT,
            order_index INTEGER NOT NULL,
            FOREIGN KEY (domain_id) REFERENCES domains(id)
        )
    ''')
    
    # Criar tabela questions
    cursor.execute('''
        CREATE TABLE questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aspect_id VARCHAR(20) NOT NULL,
            question_text TEXT NOT NULL,
            question_type VARCHAR(50) DEFAULT 'multiple_choice',
            order_index INTEGER NOT NULL,
            guidance TEXT,
            FOREIGN KEY (aspect_id) REFERENCES aspects(id)
        )
    ''')
    
    # Criar tabela answer_options
    cursor.execute('''
        CREATE TABLE answer_options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            option_text TEXT NOT NULL,
            maturity_level INTEGER NOT NULL,
            order_index INTEGER NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions(id)
        )
    ''')
    
    # Criar tabela assessments
    cursor.execute('''
        CREATE TABLE assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            name VARCHAR(255),
            status VARCHAR(50) DEFAULT 'in_progress',
            started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(id)
        )
    ''')
    
    # Criar tabela assessment_answers
    cursor.execute('''
        CREATE TABLE assessment_answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            answer_option_id INTEGER,
            answer_text TEXT,
            maturity_score INTEGER,
            answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (assessment_id) REFERENCES assessments(id),
            FOREIGN KEY (question_id) REFERENCES questions(id),
            FOREIGN KEY (answer_option_id) REFERENCES answer_options(id)
        )
    ''')
    
    # Criar tabela assessment_scores
    cursor.execute('''
        CREATE TABLE assessment_scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            aspect_id VARCHAR(20),
            domain_id INTEGER,
            score DECIMAL(5,2) NOT NULL,
            max_score DECIMAL(5,2) NOT NULL,
            percentage DECIMAL(5,2) NOT NULL,
            FOREIGN KEY (assessment_id) REFERENCES assessments(id),
            FOREIGN KEY (aspect_id) REFERENCES aspects(id),
            FOREIGN KEY (domain_id) REFERENCES domains(id)
        )
    ''')
    
    # Criar índices
    cursor.execute('CREATE INDEX idx_customers_email ON customers(email)')
    cursor.execute('CREATE INDEX idx_questions_aspect ON questions(aspect_id)')
    cursor.execute('CREATE INDEX idx_answer_options_question ON answer_options(question_id)')
    cursor.execute('CREATE INDEX idx_assessments_customer ON assessments(customer_id)')
    cursor.execute('CREATE INDEX idx_assessment_answers_assessment ON assessment_answers(assessment_id)')
    cursor.execute('CREATE INDEX idx_assessment_scores_assessment ON assessment_scores(assessment_id)')
    cursor.execute('CREATE INDEX idx_aspects_domain ON aspects(domain_id)')
    
    conn.commit()
    conn.close()
    print("Schema do banco de dados criado com sucesso!")

def load_portuguese_data(json_file: str) -> Dict[str, Any]:
    """
    Carrega os dados do arquivo JSON em português
    """
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def extract_aspect_id_from_question(question: Dict) -> str:
    """
    Extrai o aspect_id da primeira parte do ID da questão
    Ex: "1.3" de "1.3.7" ou "2.1" de "2.1"
    """
    question_id = question.get('id', '')
    if '.' in question_id:
        # Pega a primeira parte antes do segundo ponto (se houver)
        parts = question_id.split('.')
        if len(parts) >= 2:
            return f"{parts[0]}.{parts[1]}"
        else:
            return parts[0]
    return question_id

def insert_domains_and_aspects(cursor, data: Dict[str, Any]):
    """
    Insere domínios e aspectos no banco de dados
    """
    domain_order = {
        "Geral": 1,
        "Negócio": 2,
        "Pessoas": 3,
        "Processo": 4,
        "Tecnologia": 5,
        "Serviços": 6
    }
    
    aspect_counter = 1
    aspects_added = set()
    
    # Inserir domínios
    for domain_name, domain_data in data.items():
        if domain_name in domain_order:
            cursor.execute(
                "INSERT INTO domains (name, description, order_index) VALUES (?, ?, ?)",
                (domain_name, f"Domínio {domain_name}", domain_order[domain_name])
            )
            domain_id = cursor.lastrowid
            
            # Processar aspectos do domínio
            if isinstance(domain_data, dict):
                for aspect_name, aspect_data in domain_data.items():
                    if isinstance(aspect_data, list):
                        # É uma lista de perguntas (aspecto simples)
                        # Extrair aspect_id da primeira questão
                        if aspect_data and len(aspect_data) > 0:
                            aspect_id = extract_aspect_id_from_question(aspect_data[0])
                            if aspect_id and aspect_id not in aspects_added:
                                cursor.execute(
                                    "INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES (?, ?, ?, ?, ?)",
                                    (aspect_id, domain_id, aspect_name, f"Aspecto {aspect_name}", aspect_counter)
                                )
                                aspects_added.add(aspect_id)
                                aspect_counter += 1
                    elif isinstance(aspect_data, dict):
                        # É um dicionário com subaspectos
                        for subaspect_name, subaspect_data in aspect_data.items():
                            if isinstance(subaspect_data, list) and subaspect_data:
                                aspect_id = extract_aspect_id_from_question(subaspect_data[0])
                                if aspect_id and aspect_id not in aspects_added:
                                    cursor.execute(
                                        "INSERT INTO aspects (id, domain_id, name, description, order_index) VALUES (?, ?, ?, ?, ?)",
                                        (aspect_id, domain_id, f"{aspect_name} - {subaspect_name}", f"Aspecto {aspect_name} - {subaspect_name}", aspect_counter)
                                    )
                                    aspects_added.add(aspect_id)
                                    aspect_counter += 1

def insert_questions_and_options(cursor, data: Dict[str, Any]):
    """
    Insere perguntas e opções de resposta no banco de dados
    """
    question_counter = 1
    
    for domain_name, domain_data in data.items():
        if isinstance(domain_data, dict):
            for aspect_name, aspect_data in domain_data.items():
                if isinstance(aspect_data, list):
                    # Aspecto simples com lista de perguntas
                    for question in aspect_data:
                        if isinstance(question, dict) and 'question' in question:
                            aspect_id = extract_aspect_id_from_question(question)
                            question_text = question['question']
                            field_type = question.get('fieldType', 'dropdown')
                            guidance = question.get('guidance', '')
                            
                            cursor.execute(
                                "INSERT INTO questions (aspect_id, question_text, question_type, order_index, guidance) VALUES (?, ?, ?, ?, ?)",
                                (aspect_id, question_text, field_type, question_counter, guidance)
                            )
                            question_db_id = cursor.lastrowid
                            
                            # Inserir opções de resposta
                            answer_options = question.get('answerOptions', [])
                            for i, option in enumerate(answer_options):
                                # Mapear opções para níveis de maturidade
                                maturity_level = map_option_to_maturity(option)
                                cursor.execute(
                                    "INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES (?, ?, ?, ?)",
                                    (question_db_id, option, maturity_level, i + 1)
                                )
                            
                            question_counter += 1
                
                elif isinstance(aspect_data, dict):
                    # Aspecto com subaspectos
                    for subaspect_name, subaspect_data in aspect_data.items():
                        if isinstance(subaspect_data, list):
                            for question in subaspect_data:
                                if isinstance(question, dict) and 'question' in question:
                                    aspect_id = extract_aspect_id_from_question(question)
                                    question_text = question['question']
                                    field_type = question.get('fieldType', 'dropdown')
                                    guidance = question.get('guidance', '')
                                    
                                    cursor.execute(
                                        "INSERT INTO questions (aspect_id, question_text, question_type, order_index, guidance) VALUES (?, ?, ?, ?, ?)",
                                        (aspect_id, question_text, field_type, question_counter, guidance)
                                    )
                                    question_db_id = cursor.lastrowid
                                    
                                    # Inserir opções de resposta
                                    answer_options = question.get('answerOptions', [])
                                    for i, option in enumerate(answer_options):
                                        # Mapear opções para níveis de maturidade
                                        maturity_level = map_option_to_maturity(option)
                                        cursor.execute(
                                            "INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES (?, ?, ?, ?)",
                                            (question_db_id, option, maturity_level, i + 1)
                                        )
                                    
                                    question_counter += 1

def map_option_to_maturity(option: str) -> int:
    """
    Mapeia opções de resposta para níveis de maturidade (0-5)
    """
    option_lower = option.lower()
    
    # Mapeamento para opções em português
    if any(word in option_lower for word in ['não', 'nunca', '0', 'zero']):
        return 0
    elif any(word in option_lower for word in ['parcialmente', '1', 'um']):
        return 1
    elif any(word in option_lower for word in ['sim', '2', 'dois']):
        return 2
    elif any(word in option_lower for word in ['3', 'três']):
        return 3
    elif any(word in option_lower for word in ['4', 'quatro']):
        return 4
    elif any(word in option_lower for word in ['5', 'cinco']):
        return 5
    else:
        # Para opções de checkbox ou outras, usar 1 como padrão
        return 1

def create_portuguese_database(json_file: str, db_path: str):
    """
    Cria o banco de dados completo em português
    """
    print("=== Criando banco de dados SOC CMM em Português ===")
    
    # Remover banco existente se houver
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Banco de dados anterior removido: {db_path}")
    
    # Criar schema
    create_database_schema(db_path)
    
    # Carregar dados
    print("Carregando dados do arquivo JSON...")
    data = load_portuguese_data(json_file)
    
    # Conectar ao banco
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Inserir domínios e aspectos
        print("Inserindo domínios e aspectos...")
        insert_domains_and_aspects(cursor, data)
        
        # Inserir perguntas e opções
        print("Inserindo perguntas e opções de resposta...")
        insert_questions_and_options(cursor, data)
        
        # Commit das alterações
        conn.commit()
        
        # Estatísticas
        cursor.execute("SELECT COUNT(*) FROM domains")
        domains_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM aspects")
        aspects_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM questions")
        questions_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM answer_options")
        options_count = cursor.fetchone()[0]
        
        print(f"\n=== Banco de dados criado com sucesso! ===")
        print(f"Domínios: {domains_count}")
        print(f"Aspectos: {aspects_count}")
        print(f"Perguntas: {questions_count}")
        print(f"Opções de resposta: {options_count}")
        
    except Exception as e:
        print(f"Erro ao criar banco de dados: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()

def main():
    """
    Função principal
    """
    json_file = "soc_cmm_questions-port.json"
    db_path = "soc_cmm_portuguese.db"
    
    if not os.path.exists(json_file):
        print(f"Erro: Arquivo {json_file} não encontrado!")
        return
    
    try:
        create_portuguese_database(json_file, db_path)
        print(f"\nBanco de dados criado: {db_path}")
        print("Backup do banco anterior salvo como: soc_cmm_backup.db")
        
    except Exception as e:
        print(f"Erro durante a criação do banco: {e}")

if __name__ == "__main__":
    main() 