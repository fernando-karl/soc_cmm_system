#!/usr/bin/env python3
import sqlite3
import json
import os
from datetime import datetime

def export_questions_to_json(db_path, output_file):
    """Exporta todas as questões da base de dados para JSON"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Busca todas as questões
    cursor.execute("""
        SELECT id, question_text, guidance, aspect_id, question_type, order_index
        FROM questions 
        ORDER BY id
    """)
    
    questions = cursor.fetchall()
    print(f"Exportando {len(questions)} questões...")
    
    # Converte para formato JSON
    questions_data = []
    for question_id, question_text, guidance, aspect_id, question_type, order_index in questions:
        questions_data.append({
            "id": question_id,
            "question_text": question_text,
            "guidance": guidance or "",
            "aspect_id": aspect_id,
            "question_type": question_type,
            "order_index": order_index,
            "needs_translation": False,  # Campo para marcar se precisa tradução
            "translation_notes": ""  # Campo para notas sobre a tradução
        })
    
    # Adiciona metadados
    export_data = {
        "metadata": {
            "export_date": datetime.now().isoformat(),
            "total_questions": len(questions_data),
            "source_database": db_path,
            "description": "Exportação completa das questões do SOC CMM para tradução no Gemini"
        },
        "questions": questions_data
    }
    
    # Salva o arquivo JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, ensure_ascii=False, indent=2)
    
    print(f"Exportação concluída: {output_file}")
    
    # Mostra algumas estatísticas
    english_questions = sum(1 for q in questions_data if 
        any(word in q['question_text'].lower() for word in 
            ['please', 'the ', 'are ', 'is ', 'do ', 'does ', 'have ', 'has ', 'o ', 'você ']))
    
    print(f"\nEstatísticas:")
    print(f"- Total de questões: {len(questions_data)}")
    print(f"- Questões com elementos em inglês: {english_questions}")
    print(f"- Questões potencialmente traduzidas: {len(questions_data) - english_questions}")
    
    conn.close()
    return output_file

def create_import_template():
    """Cria um template para importação das traduções"""
    template = {
        "metadata": {
            "import_date": "",
            "translated_by": "Gemini",
            "description": "Traduções geradas pelo Gemini"
        },
        "questions": [
            {
                "id": 1,
                "question_text": "Tradução em português da questão",
                "guidance": "Tradução em português da orientação",
                "aspect_id": 1,
                "question_type": "multiple_choice",
                "order_index": 1,
                "original_question": "Original question in English",
                "translation_notes": "Notas sobre a tradução se necessário"
            }
        ]
    }
    
    with open('dataset/import_template.json', 'w', encoding='utf-8') as f:
        json.dump(template, f, ensure_ascii=False, indent=2)
    
    print("Template de importação criado: import_template.json")

def show_sample_questions(db_path):
    """Mostra exemplos de questões que precisam de tradução"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Busca questões com elementos em inglês
    cursor.execute("""
        SELECT id, question_text 
        FROM questions 
        WHERE question_text LIKE '%Please%' 
           OR question_text LIKE '%The %' 
           OR question_text LIKE '%Are %' 
           OR question_text LIKE '%Is %' 
           OR question_text LIKE '%Do %' 
           OR question_text LIKE '%Does %' 
           OR question_text LIKE '%Have %' 
           OR question_text LIKE '%Has %'
           OR question_text LIKE '%O %'
           OR question_text LIKE '%Você %'
        ORDER BY id
        LIMIT 20
    """)
    
    problematic_questions = cursor.fetchall()
    
    print(f"\nExemplos de questões que precisam de tradução:")
    for question_id, question_text in problematic_questions:
        print(f"  ID {question_id}: {question_text}")
    
    conn.close()

def main():
    print("=== Exportação de Questões para Tradução ===")
    
    # Verifica se a base traduzida existe
    if not os.path.exists("soc_cmm_translated.db"):
        print("Arquivo soc_cmm_translated.db não encontrado!")
        return
    
    # 1. Exporta todas as questões
    output_file = "dataset/questions_for_gemini_translation.json"
    export_questions_to_json("soc_cmm_translated.db", output_file)
    
    # 2. Cria template de importação
    create_import_template()
    
    # 3. Mostra exemplos de questões problemáticas
    show_sample_questions("soc_cmm_translated.db")
    
    print(f"\n=== Instruções para uso no Gemini ===")
    print(f"1. Abra o arquivo: {output_file}")
    print(f"2. Copie o conteúdo para o Gemini")
    print(f"3. Solicite tradução completa para português brasileiro")
    print(f"4. Use o template import_template.json para formatar a resposta")
    print(f"5. Execute o script de importação para aplicar as traduções")
    
    print(f"\n=== Processo concluído ===")
    print(f"Arquivo exportado: {output_file}")
    print(f"Template criado: import_template.json")

if __name__ == "__main__":
    main() 