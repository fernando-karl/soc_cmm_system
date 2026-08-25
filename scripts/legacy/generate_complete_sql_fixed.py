#!/usr/bin/env python3
"""
Script corrigido para gerar SQL completo para popular a base de dados do SOC CMM Assessment System
baseado no arquivo soc_cmm_questions.json e compatível com o schema atual
"""

import json
import re

def clean_text(text):
    """Limpa texto removendo caracteres especiais para SQL"""
    if not text:
        return ""
    # Remove aspas simples e duplas que podem quebrar o SQL
    text = text.replace("'", "''").replace('"', '""')
    return text.strip()

def generate_sql():
    """Gera o SQL completo baseado no arquivo JSON"""
    
    # Carrega o arquivo JSON
    with open('dataset/soc_cmm_questions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sql_lines = []
    sql_lines.append("-- SOC CMM Assessment System - Complete Database Population Script")
    sql_lines.append("-- Generated from soc_cmm_questions.json")
    sql_lines.append("-- Compatible with current database schema")
    sql_lines.append("")
    
    # Mapeamento de domínios
    domain_mapping = {
        'Business': 1,
        'People': 2, 
        'Process': 3,
        'Technology': 4,
        'Services': 5
    }
    
    # Primeiro, inserir os domínios
    sql_lines.append("-- Insert domains")
    sql_lines.append("INSERT INTO domains (id, name, description, order_index) VALUES")
    for domain_name, domain_id in domain_mapping.items():
        description = f"{domain_name} domain of SOC CMM assessment"
        sql_lines.append(f"({domain_id}, '{domain_name}', '{description}', {domain_id}),")
    sql_lines.append(";")
    sql_lines.append("")
    
    # Contadores para IDs
    aspect_id = 1
    question_id = 1
    
    # Processar cada domínio
    for domain_name, domain_data in data.items():
        if domain_name == 'General':
            continue  # Pular seção General por enquanto
            
        domain_id = domain_mapping.get(domain_name)
        if not domain_id:
            continue
            
        sql_lines.append(f"-- {domain_name} domain aspects")
        
        # Processar aspectos do domínio
        for aspect_name, aspect_questions in domain_data.items():
            if isinstance(aspect_questions, list):
                # É uma lista de questões (aspecto direto)
                aspect_description = f"{aspect_name} aspect of {domain_name} domain"
                aspect_code = f"{domain_id}.{aspect_id}"
                sql_lines.append(f"INSERT INTO aspects (id, domain_id, name, code, description, order_index) VALUES")
                sql_lines.append(f"({aspect_id}, {domain_id}, '{clean_text(aspect_name)}', '{aspect_code}', '{clean_text(aspect_description)}', {aspect_id});")
                sql_lines.append("")
                
                # Processar questões deste aspecto
                sql_lines.append(f"-- Questions for {aspect_name}")
                for question in aspect_questions:
                    if isinstance(question, dict) and 'question' in question:
                        question_text = clean_text(question['question'])
                        field_type = question.get('fieldType', 'text')
                        
                        # Mapear field_type para question_type
                        if field_type == 'dropdown':
                            question_type = 'multiple_choice'
                        elif field_type == 'checkbox':
                            question_type = 'multiple_choice'
                        elif field_type == 'numeric':
                            question_type = 'numeric'
                        else:
                            question_type = 'text'
                        
                        sql_lines.append(f"INSERT INTO questions (id, aspect_id, question_text, question_type, order_index) VALUES")
                        sql_lines.append(f"({question_id}, {aspect_id}, '{question_text}', '{question_type}', {question_id});")
                        
                        # Processar opções de resposta
                        answer_options = question.get('answerOptions', [])
                        if answer_options:
                            sql_lines.append(f"-- Answer options for question {question_id}")
                            for i, option in enumerate(answer_options, 1):
                                option_text = clean_text(option)
                                # Para checkboxes, maturity_level 0, para dropdowns, maturity_level baseado na posição
                                if field_type == 'dropdown':
                                    maturity_level = i
                                else:
                                    maturity_level = 0
                                sql_lines.append(f"INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES")
                                sql_lines.append(f"({question_id}, '{option_text}', {maturity_level}, {i});")
                            sql_lines.append("")
                        
                        question_id += 1
                
                aspect_id += 1
                
            elif isinstance(aspect_questions, dict):
                # É um dicionário com sub-aspectos
                for sub_aspect_name, sub_aspect_questions in aspect_questions.items():
                    if isinstance(sub_aspect_questions, list):
                        aspect_description = f"{sub_aspect_name} aspect of {domain_name} domain"
                        aspect_code = f"{domain_id}.{aspect_id}"
                        sql_lines.append(f"INSERT INTO aspects (id, domain_id, name, code, description, order_index) VALUES")
                        sql_lines.append(f"({aspect_id}, {domain_id}, '{clean_text(sub_aspect_name)}', '{aspect_code}', '{clean_text(aspect_description)}', {aspect_id});")
                        sql_lines.append("")
                        
                        # Processar questões deste sub-aspecto
                        sql_lines.append(f"-- Questions for {sub_aspect_name}")
                        for question in sub_aspect_questions:
                            if isinstance(question, dict) and 'question' in question:
                                question_text = clean_text(question['question'])
                                field_type = question.get('fieldType', 'text')
                                
                                # Mapear field_type para question_type
                                if field_type == 'dropdown':
                                    question_type = 'multiple_choice'
                                elif field_type == 'checkbox':
                                    question_type = 'multiple_choice'
                                elif field_type == 'numeric':
                                    question_type = 'numeric'
                                else:
                                    question_type = 'text'
                                
                                sql_lines.append(f"INSERT INTO questions (id, aspect_id, question_text, question_type, order_index) VALUES")
                                sql_lines.append(f"({question_id}, {aspect_id}, '{question_text}', '{question_type}', {question_id});")
                                
                                # Processar opções de resposta
                                answer_options = question.get('answerOptions', [])
                                if answer_options:
                                    sql_lines.append(f"-- Answer options for question {question_id}")
                                    for i, option in enumerate(answer_options, 1):
                                        option_text = clean_text(option)
                                        # Para checkboxes, maturity_level 0, para dropdowns, maturity_level baseado na posição
                                        if field_type == 'dropdown':
                                            maturity_level = i
                                        else:
                                            maturity_level = 0
                                        sql_lines.append(f"INSERT INTO answer_options (question_id, option_text, maturity_level, order_index) VALUES")
                                        sql_lines.append(f"({question_id}, '{option_text}', {maturity_level}, {i});")
                                    sql_lines.append("")
                                
                                question_id += 1
                        
                        aspect_id += 1
    
    # Escrever o arquivo SQL
    with open('sql/seed/complete_populate_database_fixed.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_lines))
    
    print(f"SQL corrigido gerado com sucesso!")
    print(f"Total de aspectos: {aspect_id - 1}")
    print(f"Total de questões: {question_id - 1}")

if __name__ == "__main__":
    generate_sql() 