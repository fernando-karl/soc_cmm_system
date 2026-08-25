#!/usr/bin/env python3
import sqlite3

def fix_aspects_table_ids():
    """Corrige os IDs da tabela aspects que são textos para códigos numéricos únicos"""
    conn = sqlite3.connect('soc_cmm_portuguese.db')
    cursor = conn.cursor()
    
    # Primeiro, vamos ver quais aspectos precisam ser corrigidos
    cursor.execute("SELECT id, name FROM aspects WHERE id NOT LIKE '%.%'")
    text_aspects = cursor.fetchall()
    
    print("Aspectos que precisam ser corrigidos:")
    for aspect_id, name in text_aspects:
        print(f"  ID: '{aspect_id}' -> Nome: '{name}'")
    
    # Mapeamento específico baseado nos nomes dos aspectos
    aspect_mapping = {
        # Aspectos de perfil (domínio 0)
        "Detalhes da Avaliação.Data da avaliação": "0.1",
        
        # Aspectos de ferramentas SOC (domínio 4)
        "SIEM / UEBA": "4.16",  # Usando ID não ocupado
        
        # Aspectos de serviços SOC (domínio 5)  
        "Monitoramento de Segurança": "5.16",  # Usando ID não ocupado
    }
    
    # Contador de atualizações
    updated_count = 0
    
    # Atualiza os IDs baseado no mapeamento
    for text_id, numeric_id in aspect_mapping.items():
        cursor.execute("""
            UPDATE aspects 
            SET id = ? 
            WHERE id = ?
        """, (numeric_id, text_id))
        
        if cursor.rowcount > 0:
            print(f"Atualizado aspecto: '{text_id}' -> '{numeric_id}' ({cursor.rowcount} registros)")
            updated_count += cursor.rowcount
    
    # Verifica se ainda há aspectos com IDs como texto
    cursor.execute("SELECT id, name FROM aspects WHERE id NOT LIKE '%.%'")
    remaining_text_aspects = cursor.fetchall()
    
    if remaining_text_aspects:
        print("\nAspectos que ainda precisam ser corrigidos:")
        for aspect_id, name in remaining_text_aspects:
            print(f"  ID: '{aspect_id}' -> Nome: '{name}'")
    else:
        print("\nTodos os aspectos foram corrigidos!")
    
    print(f"\nTotal de aspectos atualizados: {updated_count}")
    
    # Mostra todos os aspectos corrigidos
    cursor.execute("SELECT id, name FROM aspects ORDER BY id")
    corrected_aspects = cursor.fetchall()
    
    print("\nTodos os aspectos após correção:")
    for aspect_id, name in corrected_aspects:
        print(f"  {aspect_id}: {name}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Corrigindo IDs da tabela aspects...")
    fix_aspects_table_ids()
    print("Processo concluído!") 