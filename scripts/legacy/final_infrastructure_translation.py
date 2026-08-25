#!/usr/bin/env python3
import sqlite3
import os

def create_infrastructure_mapping():
    """Cria mapeamento para questões de infraestrutura e suporte"""
    mapping = {
        # Questões sobre ambiente de teste
        "Is there a testing enviroment to test and validate detections before deploying them?": {
            "translated_question": "Existe um ambiente de teste para testar e validar detecções antes de implantá-las?",
            "translated_guidance": "Ambiente de teste garante qualidade antes da implantação"
        },
        "Is there a formal release process in place for new detections?": {
            "translated_question": "Existe um processo formal de liberação para novas detecções?",
            "translated_guidance": "Processo de liberação controla mudanças e riscos"
        },
        
        # Questões sobre suporte
        "Is there dedicated personnel for support?": {
            "translated_question": "Existe pessoal dedicado para suporte?",
            "translated_guidance": "Pessoal dedicado garante disponibilidade de suporte"
        },
        "Is there a support contract for the solution?": {
            "translated_question": "Existe um contrato de suporte para a solução?",
            "translated_guidance": "Contrato de suporte define níveis de serviço"
        },
        
        # Questões sobre alta disponibilidade
        "Is there high availability (HA) in place for the solution?": {
            "translated_question": "Existe alta disponibilidade (HA) implementada para a solução?",
            "translated_guidance": "Alta disponibilidade garante continuidade operacional"
        },
        "Is there data backup / replication in place for the solution?": {
            "translated_question": "Existe backup de dados / replicação implementada para a solução?",
            "translated_guidance": "Backup e replicação protegem contra perda de dados"
        },
        "Is there configuration backup / replication in place for the solution?": {
            "translated_question": "Existe backup de configuração / replicação implementada para a solução?",
            "translated_guidance": "Backup de configuração facilita recuperação"
        },
        "Is there a Disaster Recovery plan in place for this solution?": {
            "translated_question": "Existe um plano de Disaster Recovery implementado para esta solução?",
            "translated_guidance": "Plano de DR garante recuperação em caso de desastres"
        },
        "Is there a separate development / test environment for this solution?": {
            "translated_question": "Existe um ambiente separado de desenvolvimento / teste para esta solução?",
            "translated_guidance": "Ambiente separado permite desenvolvimento seguro"
        }
    }
    
    return mapping

def update_infrastructure_questions(db_path):
    """Atualiza as questões de infraestrutura em inglês"""
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
    """)
    
    english_questions = cursor.fetchall()
    print(f"Encontradas {len(english_questions)} questões ainda em inglês")
    
    # Carrega mapeamento de infraestrutura
    infrastructure_mapping = create_infrastructure_mapping()
    
    updated_count = 0
    not_found = []
    
    for question_id, original_question in english_questions:
        if original_question in infrastructure_mapping:
            translation = infrastructure_mapping[original_question]
            
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
        for question_id, question_text in not_found:
            print(f"  ID {question_id}: {question_text}")
    
    conn.commit()
    conn.close()
    return updated_count, not_found

def verify_final_result(db_path):
    """Verifica o resultado final"""
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
    print(f"- Percentual traduzido: {((total_questions - remaining_english) / total_questions * 100):.1f}%")
    
    if remaining_english > 0:
        print(f"\nQuestões ainda em inglês:")
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
        """)
        
        remaining_samples = cursor.fetchall()
        for question_id, question_text in remaining_samples:
            print(f"  ID {question_id}: {question_text}")
    
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
        ORDER BY id
        LIMIT 10
    """)
    
    translated_samples = cursor.fetchall()
    print(f"\nExemplos de questões traduzidas:")
    for i, (question,) in enumerate(translated_samples, 1):
        print(f"  {i}. {question[:80]}...")
    
    conn.close()

def main():
    print("=== Tradução Final de Infraestrutura ===")
    
    # Verifica se a base traduzida existe
    if not os.path.exists("soc_cmm_translated.db"):
        print("Arquivo soc_cmm_translated.db não encontrado!")
        return
    
    # 1. Atualizar questões de infraestrutura
    updated_count, not_found = update_infrastructure_questions("soc_cmm_translated.db")
    
    # 2. Verificar resultado final
    verify_final_result("soc_cmm_translated.db")
    
    print(f"\n=== Processo concluído ===")
    print(f"Questões atualizadas: {updated_count}")

if __name__ == "__main__":
    main() 