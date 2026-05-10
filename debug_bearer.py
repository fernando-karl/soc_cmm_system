#!/usr/bin/env python3
"""
Script para debugar o problema com Bearer token
"""

import os
import requests
import json

# Configuração — credenciais via variáveis de ambiente
BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8400")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
if not ADMIN_PASSWORD:
    raise SystemExit("Set ADMIN_PASSWORD env var before running this debug script.")

def debug_bearer():
    """Debuga o problema com Bearer token"""
    
    # 1. Fazer login
    print("1. Fazendo login...")
    login_data = {
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD
    }
    
    login_response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
    
    if login_response.status_code != 200:
        print(f"Erro no login: {login_response.status_code}")
        print(f"Resposta: {login_response.text}")
        return
    
    login_result = login_response.json()
    access_token = login_result['access_token']
    print(f"Token obtido: {access_token[:50]}...")
    
    # 2. Testar Bearer token diretamente
    print("\n2. Testando Bearer token...")
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    # Testar endpoint simples primeiro
    test_response = requests.get(f"{BASE_URL}/api/customers", headers=headers)
    print(f"GET /api/customers - Status: {test_response.status_code}")
    print(f"Resposta: {test_response.text}")
    
    # Testar criação de cliente
    customer_data = {
        "name": "Debug Cliente",
        "email": "debug@test.com",
        "organization": "Debug Org"
    }
    
    create_response = requests.post(
        f"{BASE_URL}/api/customers",
        json=customer_data,
        headers=headers
    )
    
    print(f"\nPOST /api/customers - Status: {create_response.status_code}")
    print(f"Resposta: {create_response.text}")
    
    # 3. Verificar se o token é válido
    print(f"\n3. Verificando token...")
    print(f"Token completo: {access_token}")
    
    # Decodificar token (sem verificar assinatura para debug)
    import jwt
    try:
        # Decodificar sem verificar para ver o conteúdo
        payload = jwt.decode(access_token, options={"verify_signature": False})
        print(f"Payload do token: {json.dumps(payload, indent=2)}")
    except Exception as e:
        print(f"Erro ao decodificar token: {e}")

if __name__ == "__main__":
    print("=== Debug Bearer Token ===\n")
    debug_bearer()
    print("\n=== Fim do Debug ===") 