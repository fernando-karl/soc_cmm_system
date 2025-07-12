#!/usr/bin/env python3
import json
import sqlite3

def load_json_files():
    """Carrega os arquivos JSON em inglês e português"""
    try:
        with open('soc_cmm_questions.json', 'r', encoding='utf-8') as f:
            english_data = json.load(f)
        print("Arquivo em inglês carregado")
    except FileNotFoundError:
        print("Arquivo soc_cmm_questions.json não encontrado!")
        return None, None
    
    try:
        with open('soc_cmm_questions-port.json', 'r', encoding='utf-8') as f:
            portuguese_data = json.load(f)
        print("Arquivo em português carregado")
    except FileNotFoundError:
        print("Arquivo soc_cmm_questions-port.json não encontrado!")
        return None, None
    
    return english_data, portuguese_data

def extract_questions_by_id(data):
    """Extrai questões organizadas por ID"""
    questions_by_id = {}
    
    def process_section(section_data, domain_name=""):
        for section_name, section_content in section_data.items():
            if isinstance(section_content, dict):
                # É um subseção
                process_section(section_content, f"{domain_name}.{section_name}" if domain_name else section_name)
            elif isinstance(section_content, list):
                # É uma lista de questões
                for question in section_content:
                    if isinstance(question, dict) and 'id' in question and 'question' in question:
                        question_id = question['id']
                        questions_by_id[question_id] = {
                            'question': question['question'],
                            'guidance': question.get('guidance', ''),
                            'field_type': question.get('fieldType', ''),
                            'answer_options': question.get('answerOptions', [])
                        }
    
    # Processa cada domínio
    for domain_name, domain_data in data.items():
        if isinstance(domain_data, dict):
            process_section(domain_data, domain_name)
    
    return questions_by_id

def create_translation_mapping():
    """Cria mapeamento de questões em inglês para português"""
    english_data, portuguese_data = load_json_files()
    if not english_data or not portuguese_data:
        return {}
    
    # Extrai questões por ID
    english_questions = extract_questions_by_id(english_data)
    portuguese_questions = extract_questions_by_id(portuguese_data)
    
    print(f"Questões em inglês: {len(english_questions)}")
    print(f"Questões em português: {len(portuguese_questions)}")
    
    # Cria mapeamento baseado no ID da questão
    translation_mapping = {}
    
    for question_id, english_question in english_questions.items():
        if question_id in portuguese_questions:
            portuguese_question = portuguese_questions[question_id]
            
            # Mapeia pelo texto da questão em inglês
            translation_mapping[english_question['question']] = {
                'translated_question': portuguese_question['question'],
                'translated_guidance': portuguese_question['guidance'],
                'question_id': question_id
            }
    
    print(f"Mapeamento criado: {len(translation_mapping)} traduções")
    return translation_mapping

def update_database_with_translations(db_path, translation_mapping):
    """Atualiza a base de dados com as traduções"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    updated_count = 0
    
    # Atualiza questões
    cursor.execute("SELECT id, question_text FROM questions")
    questions = cursor.fetchall()
    
    for question_id, original_question in questions:
        if original_question in translation_mapping:
            translation = translation_mapping[original_question]
            
            cursor.execute("""
                UPDATE questions 
                SET question_text = ?, guidance = ?
                WHERE id = ?
            """, (translation['translated_question'], translation['translated_guidance'], question_id))
            
            if cursor.rowcount > 0:
                updated_count += 1
                print(f"Questão {question_id} atualizada: '{original_question[:50]}...' -> '{translation['translated_question'][:50]}...'")
    
    print(f"\nTotal de questões atualizadas: {updated_count}")
    
    conn.commit()
    conn.close()

def verify_translations(db_path):
    """Verifica se as traduções foram aplicadas"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT question_text FROM questions LIMIT 5")
    questions = cursor.fetchall()
    
    print("\nPrimeiras 5 questões após tradução:")
    for question in questions:
        print(f"  - {question[0][:80]}...")
    
    conn.close()

def main():
    print("=== Script de Tradução Baseado em ID ===")
    
    # 1. Criar mapeamento
    translation_mapping = create_translation_mapping()
    if not translation_mapping:
        print("Erro ao criar mapeamento!")
        return
    
    # 2. Atualizar base traduzida
    update_database_with_translations('soc_cmm_translated.db', translation_mapping)
    
    # 3. Verificar resultado
    verify_translations('soc_cmm_translated.db')
    
    print("\n=== Processo concluído ===")

if __name__ == "__main__":
    main() 