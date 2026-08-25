#!/usr/bin/env python3
"""
Script específico para testar o gráfico de crescimento
"""

import os

import requests
import json
import re
import time


# Admin password for the local test instance. Never hard-code credentials.
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
if not ADMIN_PASSWORD:
    raise SystemExit("Set ADMIN_PASSWORD to the admin password of your local test instance.")

def test_growth_chart():
    """Testar especificamente o gráfico de crescimento"""
    
    print("Testando Gráfico de Crescimento")
    print("=" * 40)
    
    # 1. Fazer login com usuário admin
    print("\n1. Fazendo login com usuário admin...")
    login_data = {
        "username": "admin",
        "password": ADMIN_PASSWORD
    }
    
    try:
        response = requests.post("http://localhost:8400/api/auth/login", json=login_data)
        if response.status_code == 200:
            print("✓ Login realizado com sucesso")
            cookies = response.cookies
        else:
            print(f"✗ Erro no login: {response.text}")
            return
    except Exception as e:
        print(f"✗ Erro de conexão: {e}")
        return
    
    # 2. Obter a página do dashboard
    print("\n2. Obtendo página do dashboard...")
    
    try:
        response = requests.get("http://localhost:8400/admin", cookies=cookies)
        if response.status_code == 200:
            print("✓ Página do dashboard carregada")
            html_content = response.text
            
            # 3. Analisar dados do gráfico de crescimento
            print("\n3. Analisando dados do gráfico de crescimento...")
            
            # Extrair dados monthlyUsers e monthlyCustomers
            monthly_users_match = re.search(r'monthlyUsers: (\[.*?\])', html_content, re.DOTALL)
            monthly_customers_match = re.search(r'monthlyCustomers: (\[.*?\])', html_content, re.DOTALL)
            
            if monthly_users_match:
                monthly_users_str = monthly_users_match.group(1)
                print(f"✓ monthlyUsers encontrado: {monthly_users_str}")
                try:
                    monthly_users_data = json.loads(monthly_users_str)
                    print(f"  - {len(monthly_users_data)} registros de usuários")
                    for user in monthly_users_data:
                        print(f"    * {user.get('month', 'N/A')}: {user.get('new_users', 0)} usuários")
                except json.JSONDecodeError as e:
                    print(f"✗ Erro ao decodificar monthlyUsers: {e}")
            else:
                print("✗ monthlyUsers não encontrado")
            
            if monthly_customers_match:
                monthly_customers_str = monthly_customers_match.group(1)
                print(f"✓ monthlyCustomers encontrado: {monthly_customers_str}")
                try:
                    monthly_customers_data = json.loads(monthly_customers_str)
                    print(f"  - {len(monthly_customers_data)} registros de clientes")
                    for customer in monthly_customers_data:
                        print(f"    * {customer.get('month', 'N/A')}: {customer.get('new_customers', 0)} clientes")
                except json.JSONDecodeError as e:
                    print(f"✗ Erro ao decodificar monthlyCustomers: {e}")
            else:
                print("✗ monthlyCustomers não encontrado")
            
            # 4. Verificar JavaScript do gráfico de crescimento
            print("\n4. Verificando JavaScript do gráfico de crescimento...")
            
            # Procurar por problemas específicos do growthChart
            growth_chart_instances = html_content.count("growthChart")
            print(f"Referências ao growthChart: {growth_chart_instances}")
            
            # Verificar se há múltiplas criações do gráfico
            new_chart_instances = html_content.count("new Chart")
            print(f"Instâncias de 'new Chart': {new_chart_instances}")
            
            # Verificar se há problemas com map
            map_instances = html_content.count(".map(")
            print(f"Instâncias de '.map(': {map_instances}")
            
            # Verificar se há loops ou problemas
            if "setInterval" in html_content:
                print("⚠️  setInterval encontrado - possível causa de loops")
            
            if "setTimeout" in html_content:
                print("⚠️  setTimeout encontrado - possível causa de loops")
            
            # 5. Verificar se há problemas com os dados
            print("\n5. Verificando problemas com dados...")
            
            # Verificar se há valores undefined ou null
            undefined_count = html_content.count("undefined")
            null_count = html_content.count("null")
            print(f"Valores 'undefined': {undefined_count}")
            print(f"Valores 'null': {null_count}")
            
            # Verificar se há problemas com arrays vazios
            if "[]" in html_content:
                print("⚠️  Arrays vazios encontrados")
            
            # 6. Verificar estrutura do canvas
            print("\n6. Verificando estrutura do canvas...")
            
            canvas_instances = html_content.count("<canvas")
            print(f"Elementos canvas: {canvas_instances}")
            
            growth_canvas = html_content.count('id="growthChart"')
            print(f"Canvas growthChart: {growth_canvas}")
            
            if growth_canvas == 0:
                print("✗ Canvas growthChart não encontrado")
            elif growth_canvas > 1:
                print("⚠️  Múltiplos canvas growthChart encontrados")
            else:
                print("✓ Canvas growthChart encontrado corretamente")
            
            # 7. Verificar se há problemas de sintaxe
            print("\n7. Verificando sintaxe JavaScript...")
            
            # Verificar se há problemas com aspas ou vírgulas
            if "'," in html_content or '",' in html_content:
                print("⚠️  Possíveis problemas com aspas e vírgulas")
            
            # Verificar se há problemas com parênteses
            open_parens = html_content.count("(")
            close_parens = html_content.count(")")
            print(f"Parênteses abertos: {open_parens}, fechados: {close_parens}")
            
            if open_parens != close_parens:
                print("⚠️  Parênteses desbalanceados")
            
        else:
            print(f"✗ Erro ao carregar página: {response.status_code}")
    except Exception as e:
        print(f"✗ Erro ao acessar página: {e}")

if __name__ == "__main__":
    test_growth_chart() 