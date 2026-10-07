#!/usr/bin/env python3
"""
Test script for the language switching system
"""

import requests
import time

BASE_URL = "http://localhost:8400"

def test_language_system():
    """Test the language switching functionality"""
    
    print("🌍 Testing Language Switching System")
    print("=" * 50)
    
    # Test 1: Default language (should be English)
    print("\n1. Testing default language...")
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        print("✅ Home page loaded successfully")
        if "SOC CMM Assessment System" in response.text:
            print("✅ Default language appears to be English")
        else:
            print("⚠️  Could not verify default language")
    else:
        print(f"❌ Failed to load home page: {response.status_code}")
        return
    
    # Test 2: Switch to Portuguese
    print("\n2. Testing switch to Portuguese...")
    response = requests.get(f"{BASE_URL}/change-language/pt_br")
    if response.status_code == 302:  # Redirect
        print("✅ Language change request successful (redirect)")
        
        # Check if cookie was set
        cookies = response.cookies
        if 'language' in cookies:
            print(f"✅ Language cookie set: {cookies['language']}")
        else:
            print("⚠️  Language cookie not found")
    else:
        print(f"❌ Language change failed: {response.status_code}")
    
    # Test 3: Access page with Portuguese cookie
    print("\n3. Testing page access with Portuguese cookie...")
    session = requests.Session()
    session.cookies.set('language', 'pt_br', domain='localhost')
    
    response = session.get(f"{BASE_URL}/")
    if response.status_code == 200:
        print("✅ Home page loaded with Portuguese cookie")
        if "Sistema de Avaliação SOC CMM" in response.text:
            print("✅ Portuguese content detected")
        else:
            print("⚠️  Could not verify Portuguese content")
    else:
        print(f"❌ Failed to load home page with Portuguese cookie: {response.status_code}")
    
    # Test 4: Switch back to English
    print("\n4. Testing switch back to English...")
    response = session.get(f"{BASE_URL}/change-language/en")
    if response.status_code == 302:
        print("✅ Language change back to English successful")
        
        # Check if cookie was updated
        cookies = response.cookies
        if 'language' in cookies and cookies['language'] == 'en':
            print("✅ Language cookie updated to English")
        else:
            print("⚠️  Language cookie not updated correctly")
    else:
        print(f"❌ Language change back to English failed: {response.status_code}")
    
    # Test 5: Test different pages with language switching
    print("\n5. Testing different pages with language switching...")
    
    pages_to_test = [
        "/login",
        "/register", 
        "/help",
        "/faq",
        "/terms",
        "/privacy-policy"
    ]
    
    for page in pages_to_test:
        print(f"\n   Testing {page}...")
        
        # Test English version
        response = session.get(f"{BASE_URL}{page}")
        if response.status_code == 200:
            print(f"   ✅ {page} loaded successfully")
        else:
            print(f"   ❌ {page} failed to load: {response.status_code}")
    
    # Test 6: Test with query parameter
    print("\n6. Testing language switching with query parameter...")
    response = requests.get(f"{BASE_URL}/?lang=pt_br")
    if response.status_code == 200:
        print("✅ Query parameter language switching works")
        if "Sistema de Avaliação SOC CMM" in response.text:
            print("✅ Portuguese content loaded via query parameter")
        else:
            print("⚠️  Could not verify Portuguese content via query parameter")
    else:
        print(f"❌ Query parameter language switching failed: {response.status_code}")
    
    print("\n" + "=" * 50)
    print("🎉 Language system testing completed!")
    print("\nTo manually test:")
    print("1. Open http://localhost:8400")
    print("2. Click the language selector (globe icon) in the navigation")
    print("3. Choose between English and Portuguese")
    print("4. Verify that the page content changes language")

if __name__ == "__main__":
    try:
        test_language_system()
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the server. Make sure it's running on http://localhost:8400")
    except Exception as e:
        print(f"❌ Test failed with error: {e}") 