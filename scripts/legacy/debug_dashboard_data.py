#!/usr/bin/env python3
"""
Script para debugar os dados do dashboard administrativo
"""

import sys
from pathlib import Path

# Scripts live outside the repository root; make the application modules importable.
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import json
from database import DatabaseManager

def debug_dashboard_data():
    """Debugar os dados do dashboard"""
    
    print("Debugando Dados do Dashboard Administrativo")
    print("=" * 50)
    
    # Inicializar o banco de dados
    db = DatabaseManager()
    
    try:
        # Obter estatísticas do dashboard
        stats = db.get_dashboard_stats()
        
        print("\n1. Estrutura completa dos dados:")
        print(json.dumps(stats, indent=2, default=str))
        
        print("\n2. Verificando campos específicos:")
        
        # Verificar campos obrigatórios
        required_fields = [
            'total_users', 'active_users', 'total_customers', 'total_assessments',
            'assessments_by_status', 'customers_by_user', 'recent_assessments',
            'monthly_users', 'monthly_customers'
        ]
        
        for field in required_fields:
            if field in stats:
                print(f"✓ {field}: {stats[field]}")
            else:
                print(f"✗ {field}: CAMPO AUSENTE")
        
        print("\n3. Verificando dados para gráficos:")
        
        # Verificar assessments_by_status
        print(f"assessments_by_status: {stats.get('assessments_by_status', {})}")
        if 'assessments_by_status' in stats:
            for status, count in stats['assessments_by_status'].items():
                print(f"  - {status}: {count}")
        
        # Verificar monthly_users
        print(f"\nmonthly_users: {stats.get('monthly_users', [])}")
        if 'monthly_users' in stats:
            for user_data in stats['monthly_users']:
                print(f"  - {user_data}")
        
        # Verificar monthly_customers
        print(f"\nmonthly_customers: {stats.get('monthly_customers', [])}")
        if 'monthly_customers' in stats:
            for customer_data in stats['monthly_customers']:
                print(f"  - {customer_data}")
        
        print("\n4. Verificando dados para template:")
        
        # Simular o que o template espera
        template_data = {
            'assessments_by_status': stats.get('assessments_by_status', {}),
            'monthly_users': stats.get('monthly_users', []),
            'monthly_customers': stats.get('monthly_customers', [])
        }
        
        print("Dados para template:")
        print(json.dumps(template_data, indent=2, default=str))
        
        # Verificar se há dados vazios que podem causar problemas
        if not stats.get('monthly_users'):
            print("\n⚠️  AVISO: monthly_users está vazio - isso pode causar problemas no gráfico")
        
        if not stats.get('monthly_customers'):
            print("\n⚠️  AVISO: monthly_customers está vazio - isso pode causar problemas no gráfico")
        
        if not stats.get('assessments_by_status'):
            print("\n⚠️  AVISO: assessments_by_status está vazio - isso pode causar problemas no gráfico")
        
        print("\n5. Verificando dados do banco diretamente:")
        
        # Verificar se há dados na tabela users
        conn = db.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"Total de usuários no banco: {user_count}")
        
        cursor.execute("SELECT COUNT(*) FROM customers")
        customer_count = cursor.fetchone()[0]
        print(f"Total de clientes no banco: {customer_count}")
        
        cursor.execute("SELECT COUNT(*) FROM assessments")
        assessment_count = cursor.fetchone()[0]
        print(f"Total de avaliações no banco: {assessment_count}")
        
        # Verificar dados mensais
        cursor.execute("""
            SELECT 
                strftime('%Y-%m', created_at) as month,
                COUNT(*) as new_users
            FROM users
            WHERE created_at >= date('now', '-6 months')
            GROUP BY strftime('%Y-%m', created_at)
            ORDER BY month DESC
        """)
        monthly_users_db = cursor.fetchall()
        print(f"Dados mensais de usuários no banco: {monthly_users_db}")
        
        cursor.execute("""
            SELECT 
                strftime('%Y-%m', created_at) as month,
                COUNT(*) as new_customers
            FROM customers
            WHERE created_at >= date('now', '-6 months')
            GROUP BY strftime('%Y-%m', created_at)
            ORDER BY month DESC
        """)
        monthly_customers_db = cursor.fetchall()
        print(f"Dados mensais de clientes no banco: {monthly_customers_db}")
        
        conn.close()
        
    except Exception as e:
        print(f"Erro ao debugar dados: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    debug_dashboard_data() 