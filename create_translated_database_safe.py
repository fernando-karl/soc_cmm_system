#!/usr/bin/env python3
import sqlite3
import json
import shutil
import os
from datetime import datetime

def create_backup():
    """Cria backup da base original"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"soc_cmm_backup_{timestamp}.db"
    
    if os.path.exists("soc_cmm.db"):
        shutil.copy2("soc_cmm.db", backup_name)
        print(f"Backup criado: {backup_name}")
        return backup_name
    else:
        print("Arquivo soc_cmm.db não encontrado!")
        return None

def create_translated_copy():
    """Cria uma cópia da base original para tradução"""
    translated_db = "soc_cmm_translated.db"
    
    if os.path.exists("soc_cmm.db"):
        shutil.copy2("soc_cmm.db", translated_db)
        print(f"Cópia traduzida criada: {translated_db}")
        return translated_db
    else:
        print("Arquivo soc_cmm.db não encontrado!")
        return None

def load_translations():
    """Carrega as traduções do arquivo JSON"""
    try:
        with open('soc_cmm_questions-port.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo soc_cmm_questions-port.json não encontrado!")
        return None
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return None

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

def update_database_translations(db_path, translation_mapping):
    """Atualiza a base de dados com as traduções"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Contadores
    updated_questions = 0
    updated_aspects = 0
    updated_domains = 0
    
    print("Atualizando traduções...")
    
    # 1. Atualizar domínios
    domain_translations = {
        "Business": "Negócio",
        "People": "Pessoas", 
        "Process": "Processo",
        "Technology": "Tecnologia",
        "Services": "Serviços"
    }
    
    for english_name, portuguese_name in domain_translations.items():
        cursor.execute("""
            UPDATE domains 
            SET name = ? 
            WHERE name = ?
        """, (portuguese_name, english_name))
        
        if cursor.rowcount > 0:
            print(f"Domínio atualizado: '{english_name}' -> '{portuguese_name}'")
            updated_domains += cursor.rowcount
    
    # 2. Atualizar aspectos
    aspect_translations = {
        "Business Drivers": "Drivers de Negócio",
        "Customers": "Clientes",
        "Charter": "Estatuto",
        "Governance": "Governança",
        "Privacy & Policy": "Privacidade e Política",
        "Employees": "Funcionários",
        "Roles and Hierarchy": "Funções e Hierarquia",
        "People Management": "Gerenciamento de Pessoas",
        "Knowledge Management": "Gerenciamento do Conhecimento",
        "Training and Education": "Treinamento e Educação",
        "Management": "Gerenciamento",
        "Data Collection": "Coleta de Dados",
        "Analysis": "Análise",
        "Response": "Resposta",
        "Case Management": "Gerenciamento de Casos",
        "Communication": "Comunicação"
    }
    
    for english_name, portuguese_name in aspect_translations.items():
        cursor.execute("""
            UPDATE aspects 
            SET name = ? 
            WHERE name = ?
        """, (portuguese_name, english_name))
        
        if cursor.rowcount > 0:
            print(f"Aspecto atualizado: '{english_name}' -> '{portuguese_name}'")
            updated_aspects += cursor.rowcount
    
    # 3. Atualizar questões
    cursor.execute("SELECT id, question_text, guidance FROM questions")
    questions = cursor.fetchall()
    
    for question_id, original_question, original_guidance in questions:
        if original_question in translation_mapping:
            translation = translation_mapping[original_question]
            
            cursor.execute("""
                UPDATE questions 
                SET question_text = ?, guidance = ?
                WHERE id = ?
            """, (translation['translated_question'], translation['translated_guidance'], question_id))
            
            if cursor.rowcount > 0:
                updated_questions += 1
                print(f"Questão atualizada: '{original_question[:50]}...' -> '{translation['translated_question'][:50]}...'")
    
    # 4. Atualizar opções de resposta
    cursor.execute("SELECT id, option_text FROM answer_options")
    options = cursor.fetchall()
    
    updated_options = 0
    for option_id, original_option in options:
        # Procura por traduções de opções comuns
        option_translations = {
            "Yes": "Sim",
            "No": "Não",
            "Partially": "Parcialmente",
            "Not defined": "Não definidos",
            "Partially defined": "Parcialmente definidos",
            "Fully defined": "Totalmente definidos",
            "Not documented": "Não documentados",
            "Partially documented": "Parcialmente documentados",
            "Fully documented": "Totalmente documentados",
            "Not identified": "Não identificados",
            "Partially identified": "Parcialmente identificados",
            "Fully identified": "Totalmente identificados"
        }
        
        if original_option in option_translations:
            translated_option = option_translations[original_option]
            cursor.execute("""
                UPDATE answer_options 
                SET option_text = ?
                WHERE id = ?
            """, (translated_option, option_id))
            
            if cursor.rowcount > 0:
                updated_options += 1
    
    print(f"\nResumo das atualizações:")
    print(f"- Domínios atualizados: {updated_domains}")
    print(f"- Aspectos atualizados: {updated_aspects}")
    print(f"- Questões atualizadas: {updated_questions}")
    print(f"- Opções de resposta atualizadas: {updated_options}")
    
    conn.commit()
    conn.close()

def verify_translations(db_path):
    """Verifica se as traduções foram aplicadas corretamente"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("\nVerificando traduções aplicadas:")
    
    # Verifica domínios
    cursor.execute("SELECT name FROM domains")
    domains = cursor.fetchall()
    print("Domínios:")
    for domain in domains:
        print(f"  - {domain[0]}")
    
    # Verifica alguns aspectos
    cursor.execute("SELECT name FROM aspects LIMIT 10")
    aspects = cursor.fetchall()
    print("\nAspectos (primeiros 10):")
    for aspect in aspects:
        print(f"  - {aspect[0]}")
    
    # Verifica algumas questões
    cursor.execute("SELECT question_text FROM questions LIMIT 5")
    questions = cursor.fetchall()
    print("\nQuestões (primeiras 5):")
    for question in questions:
        print(f"  - {question[0][:80]}...")
    
    conn.close()

def main():
    print("=== Script de Tradução Segura da Base de Dados ===")
    
    # 1. Criar backup
    backup_file = create_backup()
    if not backup_file:
        return
    
    # 2. Criar cópia para tradução
    translated_db = create_translated_copy()
    if not translated_db:
        return
    
    # 3. Carregar traduções
    translations = load_translations()
    if not translations:
        return
    
    # 4. Criar mapeamento de traduções
    print("Criando mapeamento de traduções...")
    translation_mapping = create_translation_mapping(translations)
    print(f"Mapeamento criado com {len(translation_mapping)} traduções")
    
    # 5. Atualizar base traduzida
    update_database_translations(translated_db, translation_mapping)
    
    # 6. Verificar resultado
    verify_translations(translated_db)
    
    print(f"\n=== Processo concluído ===")
    print(f"Backup original: {backup_file}")
    print(f"Base traduzida: {translated_db}")
    print("A base original permanece intacta!")

if __name__ == "__main__":
    main() 