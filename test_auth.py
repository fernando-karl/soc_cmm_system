#!/usr/bin/env python3
"""
Script para testar autenticação e criar cliente como admin
"""

import requests
import json

# Configuração
BASE_URL = "http://127.0.0.1:8400"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "(use-ADMIN_PASSWORD)"  # Assumindo que a senha é 'admin'

def test_auth():
    """Testa o processo de autenticação completo"""
    
    # 1. Fazer login como admin
    print("1. Fazendo login como admin...")
    login_data = {
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD
    }
    
    login_response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    
    if login_response.status_code != 200:
        print(f"Erro no login: {login_response.status_code}")
        print(f"Resposta: {login_response.text}")
        return None
    
    login_result = login_response.json()
    print(f"Login bem-sucedido! Token: {login_result['access_token'][:50]}...")
    
    # 2. Extrair cookies da resposta
    cookies = login_response.cookies
    print(f"Cookies recebidos: {dict(cookies)}")
    
    # 3. Testar criação de cliente com autenticação
    print("\n2. Testando criação de cliente com autenticação...")
    
    customer_data = {
        "name": "Cliente Teste Admin",
        "email": "teste@admin.com",
        "organization": "Organização Teste"
    }
    
    # Fazer requisição com cookies
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    create_response = requests.post(
        f"{BASE_URL}/api/customers",
        json=customer_data,
        headers=headers,
        cookies=cookies
    )
    
    print(f"Status da criação: {create_response.status_code}")
    print(f"Resposta: {create_response.text}")
    
    if create_response.status_code == 200:
        print("✅ Cliente criado com sucesso!")
        return cookies
    else:
        print("❌ Falha na criação do cliente")
        return None

def test_with_bearer_token():
    """Testa usando Bearer token no header"""
    
    # 1. Fazer login
    print("\n3. Testando com Bearer token...")
    login_data = {
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD
    }
    
    login_response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    
    if login_response.status_code != 200:
        print(f"Erro no login: {login_response.status_code}")
        return
    
    login_result = login_response.json()
    access_token = login_result['access_token']
    
    # 2. Criar cliente com Bearer token
    customer_data = {
        "name": "Cliente Teste Bearer",
        "email": "teste@bearer.com",
        "organization": "Organização Bearer"
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    create_response = requests.post(
        f"{BASE_URL}/api/customers",
        json=customer_data,
        headers=headers
    )
    
    print(f"Status da criação (Bearer): {create_response.status_code}")
    print(f"Resposta: {create_response.text}")
    
    if create_response.status_code == 200:
        print("✅ Cliente criado com sucesso usando Bearer token!")

def test_get_customers(cookies):
    """Testa listagem de clientes"""
    if not cookies:
        return
    
    print("\n4. Testando listagem de clientes...")
    
    headers = {
        "Accept": "application/json"
    }
    
    response = requests.get(
        f"{BASE_URL}/api/customers",
        headers=headers,
        cookies=cookies
    )
    
    print(f"Status da listagem: {response.status_code}")
    if response.status_code == 200:
        customers = response.json()
        print(f"Clientes encontrados: {len(customers.get('customers', []))}")
        for customer in customers.get('customers', []):
            print(f"  - {customer['name']} ({customer['email']})")
    else:
        print(f"Erro: {response.text}")

if __name__ == "__main__":
    print("=== Teste de Autenticação SOC CMM System ===\n")
    
    # Teste principal
    cookies = test_auth()
    
    # Teste com Bearer token
    test_with_bearer_token()
    
    # Teste de listagem
    test_get_customers(cookies)
    
    print("\n=== Fim dos testes ===") 