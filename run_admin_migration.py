#!/usr/bin/env python3
"""
Script para adicionar campo is_admin à tabela de usuários
"""

import sqlite3
import os
from datetime import datetime

def run_admin_migration(db_path="soc_cmm_translated.db"):
    """Executar migração para adicionar campo is_admin"""
    
    if not os.path.exists(db_path):
        print(f"Banco de dados {db_path} não encontrado!")
        return False
    
    # Criar backup
    backup_path = f"{db_path}.backup_admin_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"Criando backup: {backup_path}")
    
    try:
        # Copiar arquivo do banco de dados
        with open(db_path, 'rb') as src, open(backup_path, 'wb') as dst:
            dst.write(src.read())
    except Exception as e:
        print(f"Falha ao criar backup: {e}")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        print("Iniciando migração para adicionar campo is_admin...")
        
        # Verificar se o campo is_admin já existe
        cursor.execute("PRAGMA table_info(users)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'is_admin' not in columns:
            print("Adicionando campo is_admin à tabela users...")
            cursor.execute("ALTER TABLE users ADD COLUMN is_admin BOOLEAN DEFAULT FALSE")
        else:
            print("Campo is_admin já existe na tabela users.")
        
        # Verificar se existe usuário admin
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
        admin_exists = cursor.fetchone()[0] > 0
        
        if not admin_exists:
            print("Criando usuário administrador padrão...")
            from auth import auth_manager
            
            try:
                admin_user_id = auth_manager.create_user(
                    username="admin",
                    email="admin@soc-cmm.com",
                    password="admin123",
                    full_name="System Administrator",
                    is_admin=True
                )
                print(f"Usuário admin criado com ID: {admin_user_id}")
                print("Credenciais padrão: admin / admin123")
                print("IMPORTANTE: Altere essas credenciais após o primeiro login!")
            except Exception as e:
                print(f"Aviso: Não foi possível criar usuário admin: {e}")
        else:
            print("Usuário admin já existe. Atualizando para ter privilégios de administrador...")
            cursor.execute("UPDATE users SET is_admin = TRUE WHERE username = 'admin'")
        
        conn.commit()
        print("Migração concluída com sucesso!")
        return True
        
    except Exception as e:
        print(f"Migração falhou: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    print("Migração do Sistema de Administração SOC CMM")
    print("=" * 50)
    
    # Verificar arquivos de banco de dados
    db_files = [
        "soc_cmm_translated.db",
        "soc_cmm.db",
        "soc_cmm_portuguese.db"
    ]
    
    db_path = None
    for file in db_files:
        if os.path.exists(file):
            db_path = file
            break
    
    if not db_path:
        print("Nenhum arquivo de banco de dados encontrado!")
        print("Arquivos disponíveis:", db_files)
        exit(1)
    
    print(f"Usando banco de dados: {db_path}")
    
    # Executar migração
    if run_admin_migration(db_path):
        print("\nMigração concluída com sucesso!")
        print("O sistema agora tem controle de acesso administrativo implementado.")
        print("Apenas usuários com is_admin = TRUE podem acessar as páginas administrativas.")
    else:
        print("\nMigração falhou!")
        exit(1) 