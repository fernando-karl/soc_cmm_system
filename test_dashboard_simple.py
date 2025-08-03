#!/usr/bin/env python3
"""
Script simples para testar o dashboard
"""

import requests
import json

def test_dashboard():
    """Testar o dashboard administrativo"""
    
    print("Testando Dashboard Administrativo")
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
            login_response = response.json()
            access_token = login_response.get("access_token")
            cookies = response.cookies
        else:
            print(f"✗ Erro no login: {response.text}")
            return
    except Exception as e:
        print(f"✗ Erro de conexão: {e}")
        return
    
    # 2. Testar API do dashboard
    print("\n2. Testando API do dashboard...")
    headers = {"Authorization": f"Bearer {access_token}"}
    
    try:
        response = requests.get("http://localhost:8400/api/admin/dashboard", headers=headers)
        if response.status_code == 200:
            print("✓ API do dashboard funcionando")
            dashboard_data = response.json()
            print(f"Dados retornados: {json.dumps(dashboard_data, indent=2)}")
        else:
            print(f"✗ Erro na API do dashboard: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"✗ Erro ao acessar API do dashboard: {e}")
    
    # 3. Testar página do dashboard
    print("\n3. Testando página do dashboard...")
    
    try:
        response = requests.get("http://localhost:8400/admin", cookies=cookies)
        if response.status_code == 200:
            print("✓ Página do dashboard carregada com sucesso")
            print(f"Tamanho da resposta: {len(response.text)} caracteres")
            
            # Verificar se há erros JavaScript na página
            if "error" in response.text.lower() or "undefined" in response.text.lower():
                print("⚠️  Possíveis erros JavaScript detectados na página")
            else:
                print("✓ Nenhum erro JavaScript aparente")
        else:
            print(f"✗ Erro ao carregar página do dashboard: {response.status_code}")
    except Exception as e:
        print(f"✗ Erro ao acessar página do dashboard: {e}")

if __name__ == "__main__":
    test_dashboard() 