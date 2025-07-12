#!/usr/bin/env python3
import sqlite3
import json
import os

def import_translations(json_file, db_path):
    if not os.path.exists(json_file):
        print(f"Arquivo {json_file} não encontrado!")
        return
    if not os.path.exists(db_path):
        print(f"Arquivo {db_path} não encontrado!")
        return

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = data.get('questions', [])
    print(f"Importando {len(questions)} questões traduzidas...")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    updated = 0
    not_found = []

    for q in questions:
        qid = q['id']
        question_text = q['question_text']
        guidance = q.get('guidance', '')
        cursor.execute("SELECT id FROM questions WHERE id = ?", (qid,))
        if cursor.fetchone():
            cursor.execute(
                "UPDATE questions SET question_text = ?, guidance = ? WHERE id = ?",
                (question_text, guidance, qid)
            )
            updated += 1
        else:
            not_found.append(qid)

    conn.commit()
    conn.close()

    print(f"Questões atualizadas: {updated}")
    if not_found:
        print(f"IDs não encontrados na base: {not_found}")
    else:
        print("Todas as questões foram atualizadas com sucesso!")

if __name__ == "__main__":
    import_translations('traduzido.json', 'soc_cmm_translated.db') 