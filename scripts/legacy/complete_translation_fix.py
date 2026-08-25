#!/usr/bin/env python3
import sqlite3
import json
import os

def load_json_files():
    """Carrega os arquivos JSON original e traduzido"""
    try:
        with open('dataset/soc_cmm_questions.json', 'r', encoding='utf-8') as f:
            english_data = json.load(f)
        print("Arquivo JSON em inglês carregado")
    except FileNotFoundError:
        print("Arquivo soc_cmm_questions.json não encontrado!")
        return None, None
    
    try:
        with open('dataset/soc_cmm_questions-port.json', 'r', encoding='utf-8') as f:
            portuguese_data = json.load(f)
        print("Arquivo JSON em português carregado")
    except FileNotFoundError:
        print("Arquivo soc_cmm_questions-port.json não encontrado!")
        return None, None
    
    return english_data, portuguese_data

def extract_questions_from_json(data, language="english"):
    """Extrai todas as questões do JSON com seus IDs"""
    questions = {}
    
    def process_section(section_data, path=""):
        for section_name, section_content in section_data.items():
            current_path = f"{path}.{section_name}" if path else section_name
            
            if isinstance(section_content, dict):
                # É um subseção
                process_section(section_content, current_path)
            elif isinstance(section_content, list):
                # É uma lista de questões
                for question in section_content:
                    if isinstance(question, dict) and 'question' in question:
                        question_id = question.get('id', '')
                        question_text = question['question']
                        guidance = question.get('guidance', '')
                        
                        # Usa o ID como chave para mapeamento
                        questions[question_id] = {
                            'question': question_text,
                            'guidance': guidance,
                            'path': current_path
                        }
    
    # Processa cada domínio
    for domain_name, domain_data in data.items():
        if isinstance(domain_data, dict):
            process_section(domain_data, domain_name)
    
    print(f"Extraídas {len(questions)} questões do arquivo {language}")
    return questions

def create_translation_mapping(english_questions, portuguese_questions):
    """Cria mapeamento entre questões em inglês e português"""
    mapping = {}
    
    # Mapeia por ID
    for question_id, english_data in english_questions.items():
        if question_id in portuguese_questions:
            portuguese_data = portuguese_questions[question_id]
            mapping[english_data['question']] = {
                'translated_question': portuguese_data['question'],
                'translated_guidance': portuguese_data['guidance'],
                'question_id': question_id
            }
    
    print(f"Mapeamento criado com {len(mapping)} traduções")
    return mapping

def update_remaining_questions(db_path, translation_mapping):
    """Atualiza as questões restantes em inglês"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Busca todas as questões que ainda estão em inglês
    cursor.execute("""
        SELECT id, question_text 
        FROM questions 
        WHERE question_text LIKE '%Is there%' 
           OR question_text LIKE '%Are there%' 
           OR question_text LIKE '%Do you%' 
           OR question_text LIKE '%Does the%' 
           OR question_text LIKE '%Is the%' 
           OR question_text LIKE '%Are the%' 
           OR question_text LIKE '%Does your%' 
           OR question_text LIKE '%Is your%' 
           OR question_text LIKE '%Are your%'
           OR question_text LIKE '%Does this%'
           OR question_text LIKE '%Is this%'
           OR question_text LIKE '%Are this%'
           OR question_text LIKE '%Do the%'
           OR question_text LIKE '%Have you%'
           OR question_text LIKE '%Has the%'
           OR question_text LIKE '%Have the%'
    """)
    
    english_questions = cursor.fetchall()
    print(f"Encontradas {len(english_questions)} questões ainda em inglês")
    
    updated_count = 0
    not_found = []
    
    for question_id, original_question in english_questions:
        if original_question in translation_mapping:
            translation = translation_mapping[original_question]
            
            cursor.execute("""
                UPDATE questions 
                SET question_text = ?, guidance = ?
                WHERE id = ?
            """, (translation['translated_question'], translation['translated_guidance'], question_id))
            
            if cursor.rowcount > 0:
                updated_count += 1
                print(f"✓ Questão {question_id}: '{original_question[:50]}...' -> '{translation['translated_question'][:50]}...'")
        else:
            not_found.append((question_id, original_question))
    
    print(f"\nResumo:")
    print(f"- Questões atualizadas: {updated_count}")
    print(f"- Questões não encontradas: {len(not_found)}")
    
    if not_found:
        print("\nQuestões não encontradas no mapeamento:")
        for question_id, question_text in not_found[:10]:  # Mostra apenas as primeiras 10
            print(f"  ID {question_id}: {question_text[:80]}...")
        if len(not_found) > 10:
            print(f"  ... e mais {len(not_found) - 10} questões")
    
    conn.commit()
    conn.close()
    return updated_count, not_found

def verify_final_translation(db_path):
    """Verifica o resultado final da tradução"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Conta questões ainda em inglês
    cursor.execute("""
        SELECT COUNT(*) 
        FROM questions 
        WHERE question_text LIKE '%Is there%' 
           OR question_text LIKE '%Are there%' 
           OR question_text LIKE '%Do you%' 
           OR question_text LIKE '%Does the%' 
           OR question_text LIKE '%Is the%' 
           OR question_text LIKE '%Are the%' 
           OR question_text LIKE '%Does your%' 
           OR question_text LIKE '%Is your%' 
           OR question_text LIKE '%Are your%'
    """)
    
    remaining_english = cursor.fetchone()[0]
    
    # Conta total de questões
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_questions = cursor.fetchone()[0]
    
    print(f"\nVerificação final:")
    print(f"- Total de questões: {total_questions}")
    print(f"- Questões ainda em inglês: {remaining_english}")
    print(f"- Questões traduzidas: {total_questions - remaining_english}")
    
    # Mostra algumas questões traduzidas
    cursor.execute("""
        SELECT question_text 
        FROM questions 
        WHERE question_text NOT LIKE '%Is there%' 
           AND question_text NOT LIKE '%Are there%' 
           AND question_text NOT LIKE '%Do you%' 
           AND question_text NOT LIKE '%Does the%' 
           AND question_text NOT LIKE '%Is the%' 
           AND question_text NOT LIKE '%Are the%' 
           AND question_text NOT LIKE '%Does your%' 
           AND question_text NOT LIKE '%Is your%' 
           AND question_text NOT LIKE '%Are your%'
        LIMIT 5
    """)
    
    translated_samples = cursor.fetchall()
    print(f"\nExemplos de questões traduzidas:")
    for i, (question,) in enumerate(translated_samples, 1):
        print(f"  {i}. {question[:80]}...")
    
    conn.close()

def main():
    print("=== Correção Completa de Tradução ===")
    
    # Verifica se a base traduzida existe
    if not os.path.exists("soc_cmm_translated.db"):
        print("Arquivo soc_cmm_translated.db não encontrado!")
        return
    
    # 1. Carregar arquivos JSON
    english_data, portuguese_data = load_json_files()
    if not english_data or not portuguese_data:
        return
    
    # 2. Extrair questões
    english_questions = extract_questions_from_json(english_data, "inglês")
    portuguese_questions = extract_questions_from_json(portuguese_data, "português")
    
    # 3. Criar mapeamento
    translation_mapping = create_translation_mapping(english_questions, portuguese_questions)
    
    # 4. Atualizar questões restantes
    updated_count, not_found = update_remaining_questions("soc_cmm_translated.db", translation_mapping)
    
    # 5. Verificar resultado
    verify_final_translation("soc_cmm_translated.db")
    
    print(f"\n=== Processo concluído ===")
    print(f"Questões atualizadas: {updated_count}")

if __name__ == "__main__":
    main() 