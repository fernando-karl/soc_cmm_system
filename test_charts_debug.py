#!/usr/bin/env python3
"""
Script para debugar problemas dos gráficos
"""

import requests
import json
import re

def test_charts_debug():
    """Debugar problemas dos gráficos"""
    
    print("Debugando Problemas dos Gráficos")
    print("=" * 40)
    
    # 1. Fazer login com usuário admin
    print("\n1. Fazendo login com usuário admin...")
    login_data = {
        "username": "admin",
        "password": "Admin@123"
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
            
            # 3. Extrair dados JavaScript
            print("\n3. Analisando dados JavaScript...")
            
            # Procurar por dashboardData
            dashboard_data_match = re.search(r'const dashboardData = ({.*?});', html_content, re.DOTALL)
            if dashboard_data_match:
                print("✓ dashboardData encontrado")
                dashboard_data_str = dashboard_data_match.group(1)
                print(f"Dados: {dashboard_data_str[:200]}...")
            else:
                print("✗ dashboardData não encontrado")
            
            # Procurar por erros JavaScript
            print("\n4. Verificando erros JavaScript...")
            
            # Verificar se há loops ou problemas
            if "setInterval" in html_content or "setTimeout" in html_content:
                print("⚠️  Encontrados setInterval/setTimeout - possível causa de loops")
            
            if "while" in html_content or "for" in html_content:
                print("⚠️  Encontrados loops while/for no JavaScript")
            
            # Verificar se há múltiplas instâncias de Chart
            chart_instances = html_content.count("new Chart")
            print(f"Instâncias de Chart encontradas: {chart_instances}")
            
            if chart_instances > 2:
                print("⚠️  Múltiplas instâncias de Chart detectadas - possível causa de loops")
            
            # Verificar se há problemas com os dados
            if "undefined" in html_content:
                print("⚠️  Valores 'undefined' encontrados no JavaScript")
            
            if "null" in html_content:
                print("⚠️  Valores 'null' encontrados no JavaScript")
            
            # Verificar se há problemas com os arrays
            if "map" in html_content and "monthlyUsers" in html_content:
                print("✓ Função map encontrada para monthlyUsers")
            
            if "map" in html_content and "monthlyCustomers" in html_content:
                print("✓ Função map encontrada para monthlyCustomers")
            
            # 5. Verificar estrutura dos dados
            print("\n5. Verificando estrutura dos dados...")
            
            # Extrair dados JSON
            try:
                # Procurar por dados JSON no JavaScript
                json_pattern = r'{{ stats\.(\w+) \| tojson }}'
                json_matches = re.findall(json_pattern, html_content)
                print(f"Campos JSON encontrados: {json_matches}")
                
                # Verificar se todos os campos necessários estão presentes
                required_fields = ['assessments_by_status', 'monthly_users', 'monthly_customers']
                for field in required_fields:
                    if field in json_matches:
                        print(f"✓ Campo {field} presente")
                    else:
                        print(f"✗ Campo {field} ausente")
                        
            except Exception as e:
                print(f"Erro ao analisar dados JSON: {e}")
            
            # 6. Verificar se há problemas de sintaxe
            print("\n6. Verificando sintaxe JavaScript...")
            
            # Procurar por problemas comuns
            if "{{" in html_content and "}}" in html_content:
                print("✓ Template Jinja2 encontrado")
                
                # Verificar se há problemas com aspas
                if "'{{" in html_content or '"{{' in html_content:
                    print("⚠️  Possíveis problemas com aspas nos templates")
            
            # Verificar se há problemas com getContext
            if "getContext('2d')" in html_content:
                print("⚠️  getContext('2d') encontrado - pode causar problemas")
            
        else:
            print(f"✗ Erro ao carregar página: {response.status_code}")
    except Exception as e:
        print(f"✗ Erro ao acessar página: {e}")

if __name__ == "__main__":
    test_charts_debug() 