#!/usr/bin/env python3
import sqlite3

def fix_aspects_table_ids():
    """Corrige os IDs da tabela aspects que são textos para códigos numéricos"""
    conn = sqlite3.connect('soc_cmm_portuguese.db')
    cursor = conn.cursor()
    
    # Mapeamento de textos para códigos de aspecto
    aspect_mapping = {
        # Aspectos do domínio Geral (0)
        "Detalhes da Avaliação.Data da avaliação": "0.1",
        "SIEM / UEBA": "4.1",  # Ferramenta SOC - domínio Tecnologia
        "Monitoramento de Segurança": "5.1",  # Serviço SOC - domínio Serviços
        
        # Aspectos do domínio Negócio (1)
        "Drivers de Negócio": "1.1",
        "Clientes": "1.2", 
        "Estatuto": "1.3",
        "Governança": "1.4",
        "Privacidade e Política": "1.5",
        
        # Aspectos do domínio Pessoas (2)
        "Funcionários": "2.1",
        "Funções e Hierarquia": "2.2",
        "Gerenciamento de Pessoas": "2.3",
        "Gerenciamento do Conhecimento": "2.4",
        "Treinamento e Educação": "2.5",
        
        # Aspectos do domínio Processo (3)
        "Gerenciamento": "3.1",
        "Coleta de Dados": "3.2",
        "Análise": "3.3",
        "Resposta": "3.4",
        "Gerenciamento de Casos": "3.5",
        "Comunicação": "3.6",
        
        # Aspectos do domínio Tecnologia (4)
        "NDR": "4.2",
        "EDR": "4.3",
        "SOAR": "4.4",
        
        # Aspectos do domínio Serviços (5)
        "Gerenciamento de Incidentes de Segurança": "5.2",
        "Análise de Segurança": "5.3",
        "Inteligência de Ameaças": "5.4",
        "Caça a Ameaças": "5.5",
        "Gerenciamento de Vulnerabilidades": "5.6",
        "Gerenciamento de Logs": "5.7"
    }
    
    # Primeiro, vamos ver quais aspectos precisam ser corrigidos
    cursor.execute("SELECT id, name FROM aspects WHERE id NOT LIKE '%.%'")
    text_aspects = cursor.fetchall()
    
    print("Aspectos que precisam ser corrigidos:")
    for aspect_id, name in text_aspects:
        print(f"  ID: '{aspect_id}' -> Nome: '{name}'")
    
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
    
    # Mostra alguns exemplos dos aspectos corrigidos
    cursor.execute("SELECT id, name FROM aspects ORDER BY id LIMIT 10")
    corrected_aspects = cursor.fetchall()
    
    print("\nExemplos de aspectos corrigidos:")
    for aspect_id, name in corrected_aspects:
        print(f"  {aspect_id}: {name}")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Corrigindo IDs da tabela aspects...")
    fix_aspects_table_ids()
    print("Processo concluído!") 