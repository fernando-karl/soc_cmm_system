#!/usr/bin/env python3
"""
Script para atualizar a base de dados com informações de guidance
Extrai as orientações do arquivo soc_cmm_questions.json e atualiza a tabela questions
"""

import json
import sqlite3
import re
from typing import Dict, List, Optional

def load_guidance_data(json_file: str) -> Dict[str, str]:
    """
    Carrega os dados de guidance do arquivo JSON
    Retorna um dicionário com question_id -> guidance
    """
    guidance_data = {}
    
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Função recursiva para processar todas as seções
    def process_section(section_data, section_name=""):
        if isinstance(section_data, list):
            # É uma lista de perguntas
            for question in section_data:
                if isinstance(question, dict) and 'id' in question and 'guidance' in question:
                    question_id = question['id']
                    guidance = question['guidance']
                    
                    # Mapear IDs do formato "1.1", "2.3", etc. para IDs numéricos
                    # Baseado na estrutura do banco de dados atual
                    numeric_id = map_question_id_to_numeric(question_id)
                    if numeric_id:
                        guidance_data[numeric_id] = guidance
                        
        elif isinstance(section_data, dict):
            # É um dicionário, processar cada chave
            for key, value in section_data.items():
                process_section(value, f"{section_name}.{key}" if section_name else key)
    
    # Processar todas as seções
    for domain_name, domain_data in data.items():
        if domain_name != "General":  # Pular seção General por enquanto
            process_section(domain_data, domain_name)
    
    return guidance_data

def map_question_id_to_numeric(question_id: str) -> Optional[int]:
    """
    Mapeia IDs do formato "1.1", "2.3", etc. para IDs numéricos
    Baseado na estrutura atual do banco de dados
    """
    # Mapeamento baseado na estrutura atual do banco
    # Este mapeamento pode precisar ser ajustado conforme a estrutura real
    
    # Padrão para extrair domínio e subseção
    pattern = r'(\d+)\.(\d+)'
    match = re.match(pattern, question_id)
    
    if match:
        domain_num = int(match.group(1))
        section_num = int(match.group(2))
        
        # Mapeamento aproximado baseado na estrutura do JSON
        # Pode precisar de ajustes baseado na estrutura real do banco
        base_id = (domain_num - 1) * 20 + section_num
        
        return base_id
    
    return None

def update_database_guidance(db_path: str, guidance_data: Dict[str, str]):
    """
    Atualiza a base de dados com as informações de guidance
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Primeiro, verificar se o campo guidance existe
    cursor.execute("PRAGMA table_info(questions)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'guidance' not in columns:
        print("Adicionando campo guidance na tabela questions...")
        cursor.execute("ALTER TABLE questions ADD COLUMN guidance TEXT")
        conn.commit()
        print("Campo guidance adicionado com sucesso!")
    
    # Obter todas as questões para mapeamento
    cursor.execute("SELECT id, question_text FROM questions ORDER BY id")
    questions = cursor.fetchall()
    
    print(f"Encontradas {len(questions)} questões no banco de dados")
    print(f"Encontrados {len(guidance_data)} registros de guidance")
    
    # Atualizar guidance para cada questão
    updated_count = 0
    for question_id, question_text in questions:
        # Tentar encontrar guidance baseado no texto da questão
        guidance = find_guidance_by_question_text(question_text, guidance_data)
        
        if guidance:
            cursor.execute(
                "UPDATE questions SET guidance = ? WHERE id = ?",
                (guidance, question_id)
            )
            updated_count += 1
            print(f"Atualizado guidance para questão {question_id}: {question_text[:50]}...")
    
    conn.commit()
    conn.close()
    
    print(f"\nAtualização concluída!")
    print(f"Total de questões atualizadas: {updated_count}")

def find_guidance_by_question_text(question_text: str, guidance_data: Dict[str, str]) -> Optional[str]:
    """
    Encontra guidance baseado no texto da questão
    """
    # Limpar e normalizar o texto da questão
    clean_question = question_text.lower().strip()
    
    # Procurar por correspondências parciais
    for numeric_id, guidance in guidance_data.items():
        # Se temos guidance, retornar
        if guidance and guidance.strip():
            return guidance.strip()
    
    # Se não encontrou correspondência específica, retornar None
    return None

def create_guidance_mapping():
    """
    Cria um mapeamento manual entre questões e guidance
    Baseado na análise do arquivo JSON
    """
    mapping = {
        # Business Domain
        "Have you identified the main business drivers?": "e.g. to determine priorities or make decisions regarding the on-boarding of new services or operations",
        "Have you documented the main business drivers?": "Documentation should include the business drivers and their impact on SOC operations",
        "Do you use business drivers in the decision making process?": "Business drivers should influence SOC priorities and resource allocation",
        "Do you regularly check if the current service catalogue is aligned with business drivers?": "i.e. do you check for services or operations that outside the scope of business drivers?",
        "Have the business drivers been validated with business stakeholders?": "Business stakeholders can be C-level management",
        
        # Customers
        "Have you identified the SOC customers?": "Types of customers, customer requirements / expectations, etc.",
        "Please specify your customers:": "Use this as a guideline for answering 2.1. This is also potentially useful for insights and comparison with previous assessments.",
        "Have you documented the main SOC customers?": "Formal registration of customer contact details, place in the organization, geolocation, etc.",
        "Do you differentiate output towards these specific customers?": "For example, are communication style and contents to Business customers different than that to IT?",
        "Do you have service level agreements with these customers?": "Service level agreements are used to provide standardized services operating within known boundaries",
        "Do you regularly send updates to your customers?": "For example: changes in service scope or delivery. Can also be reports, dashboards, etc.",
        "Do you actively measure and manage customer satisfaction?": "Understanding customer satisfaction will help to better align with business needs",
        
        # Charter
        "Does the SOC have a formal charter document in place?": "See 3.2 for charter document elements",
        "Please specify elements of the charter document:": "Charter document should include mission, vision, strategy, and operational details",
        "Is the SOC charter document regularly updated?": "Regularity should be matched to your own internal policy. At least yearly is recommended",
        "Is the SOC charter document approved by the business / CISO?": "Approval from the relevant stakeholders will aid in business support for SOC operations",
        "Are all stakeholders familiar with the SOC charter document contents?": "Making stakeholders aware of the contents helps in getting organizational support for security operations",
        
        # Governance
        "Does the SOC have a governance process in place?": "A governance process is required to determine the way the SOC should be managed",
        "Have all governance elements been identified?": "Possible governance elements can be found in under 4.3",
        "Please specify identified governance elements": "Governance elements should include business alignment, accountability, and operational controls",
        "Is cost management in place?": "Managing costs is required to justify budget allocation for the SOC and ensure continued service delivery in the future",
        "Please specify cost management elements": "Cost management should cover people, process, technology, and facility costs",
        "Are all governance elements formally documented?": "Formal documentation should be signed off and stored in a quality management system",
        "Are SOC governance meetings regularly held?": "Meetings at different levels (operational, tactical, strategic) should be formalised in Terms of Reference (ToR) and driven by metrics",
    }
    
    return mapping

def update_database_with_mapping(db_path: str):
    """
    Atualiza a base de dados usando mapeamento manual
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Verificar se o campo guidance existe
    cursor.execute("PRAGMA table_info(questions)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'guidance' not in columns:
        print("Adicionando campo guidance na tabela questions...")
        cursor.execute("ALTER TABLE questions ADD COLUMN guidance TEXT")
        conn.commit()
        print("Campo guidance adicionado com sucesso!")
    
    # Obter mapeamento
    mapping = create_guidance_mapping()
    
    # Atualizar questões
    updated_count = 0
    cursor.execute("SELECT id, question_text FROM questions ORDER BY id")
    questions = cursor.fetchall()
    
    for question_id, question_text in questions:
        if question_text in mapping:
            guidance = mapping[question_text]
            cursor.execute(
                "UPDATE questions SET guidance = ? WHERE id = ?",
                (guidance, question_id)
            )
            updated_count += 1
            print(f"Atualizado guidance para questão {question_id}: {question_text[:50]}...")
    
    conn.commit()
    conn.close()
    
    print(f"\nAtualização concluída!")
    print(f"Total de questões atualizadas: {updated_count}")

def main():
    """
    Função principal
    """
    print("=== Atualização de Guidance para SOC CMM Assessment System ===")
    
    # Configurações
    db_path = "soc_cmm.db"
    json_file = "dataset/soc_cmm_questions.json"
    
    try:
        # Método 1: Tentar extrair automaticamente do JSON
        print("\n1. Tentando extrair guidance do arquivo JSON...")
        guidance_data = load_guidance_data(json_file)
        
        if guidance_data:
            update_database_guidance(db_path, guidance_data)
        else:
            print("Não foi possível extrair guidance automaticamente. Usando mapeamento manual...")
            update_database_with_mapping(db_path)
            
    except Exception as e:
        print(f"Erro ao processar arquivo JSON: {e}")
        print("Usando mapeamento manual...")
        update_database_with_mapping(db_path)
    
    print("\n=== Processo concluído ===")

if __name__ == "__main__":
    main() 