#!/usr/bin/env python3
"""
Script corrigido para executar o SQL de população da base de dados do SOC CMM Assessment System
"""

import sqlite3
import os
import re

def populate_database():
    """Executa o SQL para popular a base de dados"""
    
    # Verificar se o arquivo SQL existe
    sql_file = 'sql/seed/complete_populate_database.sql'
    if not os.path.exists(sql_file):
        print(f"Erro: Arquivo {sql_file} não encontrado!")
        print("Execute primeiro o script generate_complete_sql.py")
        return
    
    # Conectar à base de dados
    try:
        conn = sqlite3.connect('soc_cmm.db')
        cursor = conn.cursor()
        print("Conectado à base de dados soc_cmm.db")
        
        # Ler o arquivo SQL
        with open(sql_file, 'r', encoding='utf-8') as f:
            sql_content = f.read()
        
        # Dividir o SQL em comandos completos usando ponto e vírgula
        # Remover comentários primeiro
        sql_content = re.sub(r'--.*$', '', sql_content, flags=re.MULTILINE)
        
        # Dividir por ponto e vírgula, mas manter comandos completos
        commands = []
        current_command = ""
        
        for line in sql_content.split('\n'):
            line = line.strip()
            if line:
                current_command += line + " "
                if line.endswith(';'):
                    commands.append(current_command.strip())
                    current_command = ""
        
        # Executar cada comando
        print("Executando comandos SQL...")
        successful_commands = 0
        failed_commands = 0
        
        for i, command in enumerate(commands, 1):
            if command and command != ";":
                try:
                    cursor.execute(command)
                    successful_commands += 1
                    if i % 50 == 0:  # Mostrar progresso a cada 50 comandos
                        print(f"Executados {i} comandos...")
                except sqlite3.Error as e:
                    failed_commands += 1
                    print(f"Erro no comando {i}: {e}")
                    print(f"Comando: {command[:100]}...")
                    continue
        
        # Commit das alterações
        conn.commit()
        print(f"Alterações commitadas com sucesso!")
        print(f"Comandos executados com sucesso: {successful_commands}")
        print(f"Comandos com erro: {failed_commands}")
        
        # Verificar os dados inseridos
        print("\nVerificando dados inseridos:")
        
        # Contar domínios
        cursor.execute("SELECT COUNT(*) FROM domains")
        domains_count = cursor.fetchone()[0]
        print(f"Domínios inseridos: {domains_count}")
        
        # Contar aspectos
        cursor.execute("SELECT COUNT(*) FROM aspects")
        aspects_count = cursor.fetchone()[0]
        print(f"Aspectos inseridos: {aspects_count}")
        
        # Contar questões
        cursor.execute("SELECT COUNT(*) FROM questions")
        questions_count = cursor.fetchone()[0]
        print(f"Questões inseridas: {questions_count}")
        
        # Contar opções de resposta
        cursor.execute("SELECT COUNT(*) FROM answer_options")
        options_count = cursor.fetchone()[0]
        print(f"Opções de resposta inseridas: {options_count}")
        
        # Mostrar alguns exemplos
        print("\nExemplos de domínios:")
        cursor.execute("SELECT id, name FROM domains ORDER BY id")
        for row in cursor.fetchall():
            print(f"  {row[0]}: {row[1]}")
        
        print("\nExemplos de aspectos:")
        cursor.execute("SELECT a.id, d.name as domain, a.name FROM aspects a JOIN domains d ON a.domain_id = d.id ORDER BY a.id LIMIT 10")
        for row in cursor.fetchall():
            print(f"  {row[0]}: {row[2]} ({row[1]})")
        
        print("\nExemplos de questões:")
        cursor.execute("SELECT q.id, a.name as aspect, q.question_text FROM questions q JOIN aspects a ON q.aspect_id = a.id ORDER BY q.id LIMIT 5")
        for row in cursor.fetchall():
            print(f"  {row[0]}: {row[2][:50]}... ({row[1]})")
        
        conn.close()
        print("\nBase de dados populada com sucesso!")
        
    except sqlite3.Error as e:
        print(f"Erro na base de dados: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    populate_database() 