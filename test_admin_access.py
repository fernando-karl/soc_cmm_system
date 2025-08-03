#!/usr/bin/env python3
"""
Script para testar as restrições de acesso administrativo
"""

import requests
import json
import time

BASE_URL = "http://localhost:8400"

def test_admin_access():
    """Testar acesso administrativo"""
    
    print("Testando Restrições de Acesso Administrativo")
    print("=" * 50)
    
    # 1. Criar um usuário normal (não admin)
    print("\n1. Criando usuário normal...")
    normal_user = {
        "username": "testuser2",
        "email": "testuser2@example.com",
        "password": "testpass123",
        "full_name": "Test User"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/auth/register", json=normal_user)
        if response.status_code == 200:
            print("✓ Usuário normal criado com sucesso")
        else:
            print(f"✗ Erro ao criar usuário: {response.text}")
            return
    except Exception as e:
        print(f"✗ Erro de conexão: {e}")
        return
    
    # 2. Fazer login com usuário normal
    print("\n2. Fazendo login com usuário normal...")
    login_data = {
        "username": "testuser2",
        "password": "testpass123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
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
    
    # 3. Tentar acessar páginas administrativas com usuário normal
    print("\n3. Testando acesso às páginas administrativas com usuário normal...")
    
    admin_pages = [
        "/admin",
        "/admin/users",
        "/admin/users/new"
    ]
    
    headers = {"Authorization": f"Bearer {access_token}"}
    
    for page in admin_pages:
        try:
            # Testar acesso via API (Bearer token)
            response = requests.get(f"{BASE_URL}{page}", headers=headers)
            if response.status_code == 302:  # Redirect to home
                print(f"✓ Acesso negado corretamente para {page} (redirect)")
            elif response.status_code == 403:
                print(f"✓ Acesso negado corretamente para {page} (403)")
            else:
                print(f"✗ Acesso inesperado para {page}: {response.status_code}")
            
            # Testar acesso via cookies
            response = requests.get(f"{BASE_URL}{page}", cookies=cookies)
            if response.status_code == 302:  # Redirect to home
                print(f"✓ Acesso negado corretamente para {page} via cookies (redirect)")
            elif response.status_code == 403:
                print(f"✓ Acesso negado corretamente para {page} via cookies (403)")
            else:
                print(f"✗ Acesso inesperado para {page} via cookies: {response.status_code}")
                
        except Exception as e:
            print(f"✗ Erro ao testar {page}: {e}")
    
    # 4. Testar APIs administrativas
    print("\n4. Testando APIs administrativas com usuário normal...")
    
    admin_apis = [
        "/api/admin/dashboard",
        "/api/admin/users"
    ]
    
    for api in admin_apis:
        try:
            response = requests.get(f"{BASE_URL}{api}", headers=headers)
            if response.status_code == 403:
                print(f"✓ API {api} corretamente protegida (403)")
            else:
                print(f"✗ API {api} não protegida: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro ao testar API {api}: {e}")
    
    # 5. Fazer login com usuário admin
    print("\n5. Fazendo login com usuário admin...")
    admin_login = {
        "username": "admin",
        "password": "Admin@123"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/auth/login", json=admin_login)
        if response.status_code == 200:
            print("✓ Login admin realizado com sucesso")
            admin_response = response.json()
            admin_token = admin_response.get("access_token")
            admin_cookies = response.cookies
        else:
            print(f"✗ Erro no login admin: {response.text}")
            return
    except Exception as e:
        print(f"✗ Erro de conexão: {e}")
        return
    
    # 6. Testar acesso administrativo com usuário admin
    print("\n6. Testando acesso administrativo com usuário admin...")
    
    admin_headers = {"Authorization": f"Bearer {admin_token}"}
    
    for page in admin_pages:
        try:
            # Testar acesso via API (Bearer token)
            response = requests.get(f"{BASE_URL}{page}", headers=admin_headers)
            if response.status_code == 200:
                print(f"✓ Acesso permitido para {page} (admin)")
            else:
                print(f"✗ Acesso negado para {page} (admin): {response.status_code}")
            
            # Testar acesso via cookies
            response = requests.get(f"{BASE_URL}{page}", cookies=admin_cookies)
            if response.status_code == 200:
                print(f"✓ Acesso permitido para {page} via cookies (admin)")
            else:
                print(f"✗ Acesso negado para {page} via cookies (admin): {response.status_code}")
                
        except Exception as e:
            print(f"✗ Erro ao testar {page} (admin): {e}")
    
    # 7. Testar APIs administrativas com admin
    print("\n7. Testando APIs administrativas com usuário admin...")
    
    for api in admin_apis:
        try:
            response = requests.get(f"{BASE_URL}{api}", headers=admin_headers)
            if response.status_code == 200:
                print(f"✓ API {api} acessível para admin")
            else:
                print(f"✗ API {api} não acessível para admin: {response.status_code}")
        except Exception as e:
            print(f"✗ Erro ao testar API {api} (admin): {e}")
    
    print("\n" + "=" * 50)
    print("Teste concluído!")

if __name__ == "__main__":
    # Aguardar um pouco para o servidor inicializar
    print("Aguardando servidor inicializar...")
    time.sleep(3)
    
    test_admin_access() 