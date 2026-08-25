#!/usr/bin/env python3
import sqlite3
import json

def load_translations():
    """Carrega as traduções do arquivo JSON"""
    with open('dataset/soc_cmm_questions-port.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_translation_mapping(translations):
    """Cria mapeamento de traduções baseado no texto da questão"""
    mapping = {}
    
    def process_section(section_data, domain_name=""):
        for section_name, section_content in section_data.items():
            if isinstance(section_content, dict):
                # É um subseção
                process_section(section_content, f"{domain_name}.{section_name}" if domain_name else section_name)
            elif isinstance(section_content, list):
                # É uma lista de questões
                for question in section_content:
                    if isinstance(question, dict) and 'question' in question:
                        original_text = question['question']
                        translated_text = question.get('question', original_text)
                        guidance = question.get('guidance', '')
                        
                        # Mapeia pelo texto da questão
                        mapping[original_text] = {
                            'translated_question': translated_text,
                            'translated_guidance': guidance,
                            'aspect_id': question.get('id', ''),
                            'field_type': question.get('fieldType', ''),
                            'answer_options': question.get('answerOptions', [])
                        }
    
    # Processa cada domínio
    for domain_name, domain_data in translations.items():
        if isinstance(domain_data, dict):
            process_section(domain_data, domain_name)
    
    return mapping

def debug_mapping():
    """Debuga o mapeamento de traduções"""
    # Carrega traduções
    translations = load_translations()
    translation_mapping = create_translation_mapping(translations)
    
    print(f"Total de traduções no JSON: {len(translation_mapping)}")
    
    # Conecta ao banco
    conn = sqlite3.connect('soc_cmm_translated.db')
    cursor = conn.cursor()
    
    # Pega algumas questões do banco
    cursor.execute("SELECT id, question_text FROM questions LIMIT 10")
    db_questions = cursor.fetchall()
    
    print("\nPrimeiras 10 questões do banco:")
    for q_id, question_text in db_questions:
        print(f"ID {q_id}: {question_text}")
        
        # Verifica se existe tradução
        if question_text in translation_mapping:
            translation = translation_mapping[question_text]
            print(f"  -> Tradução encontrada: {translation['translated_question']}")
        else:
            print(f"  -> NENHUMA TRADUÇÃO ENCONTRADA!")
    
    # Mostra algumas traduções disponíveis
    print("\nPrimeiras 10 traduções disponíveis:")
    count = 0
    for original, translation in translation_mapping.items():
        if count < 10:
            print(f"'{original}' -> '{translation['translated_question']}'")
            count += 1
        else:
            break
    
    # Verifica quantas questões têm tradução
    cursor.execute("SELECT COUNT(*) FROM questions")
    total_questions = cursor.fetchone()[0]
    
    matched_count = 0
    for q_id, question_text in db_questions:
        if question_text in translation_mapping:
            matched_count += 1
    
    print(f"\nEstatísticas:")
    print(f"Total de questões no banco: {total_questions}")
    print(f"Questões com tradução encontrada: {matched_count}")
    print(f"Taxa de sucesso: {matched_count/len(db_questions)*100:.1f}%")
    
    conn.close()

if __name__ == "__main__":
    debug_mapping() 