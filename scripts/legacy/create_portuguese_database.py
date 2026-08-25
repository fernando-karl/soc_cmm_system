#!/usr/bin/env python3
"""
Script para criar novo banco de dados SOC CMM com dados em português
Baseado no arquivo soc_cmm_questions-port.json
"""

import json
import sqlite3
import os
from typing import Dict, List, Any

def create_database_schema(db_path: str):
    """
    Cria o schema do banco de dados
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Criar tabela domains
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    ''')
    
    # Criar tabela aspects
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS aspects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain_id INTEGER NOT NULL,
            aspect_id TEXT NOT NULL,
            name TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY (domain_id) REFERENCES domains (id),
            UNIQUE(domain_id, aspect_id)
        )
    ''')
    
    # Criar tabela questions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aspect_id INTEGER NOT NULL,
            question_id TEXT NOT NULL,
            question_text TEXT NOT NULL,
            field_type TEXT NOT NULL,
            guidance TEXT,
            FOREIGN KEY (aspect_id) REFERENCES aspects (id),
            UNIQUE(aspect_id, question_id)
        )
    ''')
    
    # Criar tabela answer_options
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS answer_options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            option_text TEXT NOT NULL,
            option_order INTEGER NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions (id)
        )
    ''')
    
    # Criar tabela customers
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Criar tabela assessments
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assessments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (customer_id) REFERENCES customers (id)
        )
    ''')
    
    # Criar tabela responses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            assessment_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            response_value TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (assessment_id) REFERENCES assessments (id),
            FOREIGN KEY (question_id) REFERENCES questions (id),
            UNIQUE(assessment_id, question_id)
        )
    ''')
    
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

def insert_domains_and_aspects(cursor, data: Dict[str, Any]):
    """
    Insere domínios e aspectos no banco de dados
    """
    domain_mapping = {
        "Geral": "Geral",
        "Negócio": "Business", 
        "Pessoas": "People",
        "Processo": "Process",
        "Tecnologia": "Technology",
        "Serviços": "Services"
    }
    
    # Inserir domínios
    for domain_name, domain_data in data.items():
        if domain_name in domain_mapping:
            cursor.execute(
                "INSERT INTO domains (name, description) VALUES (?, ?)",
                (domain_name, f"Domínio {domain_name}")
            )
            domain_id = cursor.lastrowid
            
            # Processar aspectos do domínio
            if isinstance(domain_data, dict):
                for aspect_name, aspect_data in domain_data.items():
                    if isinstance(aspect_data, list):
                        # É uma lista de perguntas (aspecto simples)
                        aspect_id = f"{domain_name}.{aspect_name}"
                        cursor.execute(
                            "INSERT INTO aspects (domain_id, aspect_id, name, description) VALUES (?, ?, ?, ?)",
                            (domain_id, aspect_id, aspect_name, f"Aspecto {aspect_name}")
                        )
                    elif isinstance(aspect_data, dict):
                        # É um dicionário com subaspectos
                        for subaspect_name, subaspect_data in aspect_data.items():
                            if isinstance(subaspect_data, list):
                                aspect_id = f"{domain_name}.{aspect_name}.{subaspect_name}"
                                cursor.execute(
                                    "INSERT INTO aspects (domain_id, aspect_id, name, description) VALUES (?, ?, ?, ?)",
                                    (domain_id, aspect_id, f"{aspect_name} - {subaspect_name}", f"Aspecto {aspect_name} - {subaspect_name}")
                                )

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
                    aspect_id = f"{domain_name}.{aspect_name}"
                    cursor.execute("SELECT id FROM aspects WHERE aspect_id = ?", (aspect_id,))
                    aspect_db_id = cursor.fetchone()
                    
                    if aspect_db_id:
                        aspect_db_id = aspect_db_id[0]
                        for question in aspect_data:
                            if isinstance(question, dict) and 'question' in question:
                                question_id = question.get('id', str(question_counter))
                                question_text = question['question']
                                field_type = question.get('fieldType', 'dropdown')
                                guidance = question.get('guidance', '')
                                
                                cursor.execute(
                                    "INSERT INTO questions (aspect_id, question_id, question_text, field_type, guidance) VALUES (?, ?, ?, ?, ?)",
                                    (aspect_db_id, question_id, question_text, field_type, guidance)
                                )
                                question_db_id = cursor.lastrowid
                                
                                # Inserir opções de resposta
                                answer_options = question.get('answerOptions', [])
                                for i, option in enumerate(answer_options):
                                    cursor.execute(
                                        "INSERT INTO answer_options (question_id, option_text, option_order) VALUES (?, ?, ?)",
                                        (question_db_id, option, i + 1)
                                    )
                                
                                question_counter += 1
                
                elif isinstance(aspect_data, dict):
                    # Aspecto com subaspectos
                    for subaspect_name, subaspect_data in aspect_data.items():
                        if isinstance(subaspect_data, list):
                            aspect_id = f"{domain_name}.{aspect_name}.{subaspect_name}"
                            cursor.execute("SELECT id FROM aspects WHERE aspect_id = ?", (aspect_id,))
                            aspect_db_id = cursor.fetchone()
                            
                            if aspect_db_id:
                                aspect_db_id = aspect_db_id[0]
                                for question in subaspect_data:
                                    if isinstance(question, dict) and 'question' in question:
                                        question_id = question.get('id', str(question_counter))
                                        question_text = question['question']
                                        field_type = question.get('fieldType', 'dropdown')
                                        guidance = question.get('guidance', '')
                                        
                                        cursor.execute(
                                            "INSERT INTO questions (aspect_id, question_id, question_text, field_type, guidance) VALUES (?, ?, ?, ?, ?)",
                                            (aspect_db_id, question_id, question_text, field_type, guidance)
                                        )
                                        question_db_id = cursor.lastrowid
                                        
                                        # Inserir opções de resposta
                                        answer_options = question.get('answerOptions', [])
                                        for i, option in enumerate(answer_options):
                                            cursor.execute(
                                                "INSERT INTO answer_options (question_id, option_text, option_order) VALUES (?, ?, ?)",
                                                (question_db_id, option, i + 1)
                                            )
                                        
                                        question_counter += 1

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
    json_file = "dataset/soc_cmm_questions-port.json"
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