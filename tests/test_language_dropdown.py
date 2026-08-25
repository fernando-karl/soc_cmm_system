#!/usr/bin/env python3
"""
Test script for the language dropdown functionality
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://localhost:8400"

def test_language_dropdown():
    """Test the language dropdown functionality"""
    
    print("🌍 Testing Language Dropdown Functionality")
    print("=" * 50)
    
    # Test 1: Check if dropdown is hidden by default
    print("\n1. Testing dropdown visibility by default...")
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        dropdown = soup.find('div', {'id': 'languageDropdown'})
        
        if dropdown:
            # Check if dropdown has the 'show' class
            if 'show' in dropdown.get('class', []):
                print("❌ Dropdown is visible by default (should be hidden)")
            else:
                print("✅ Dropdown is hidden by default (correct)")
        else:
            print("❌ Language dropdown not found")
    else:
        print(f"❌ Failed to load page: {response.status_code}")
        return
    
    # Test 2: Check if flag icons are present
    print("\n2. Testing flag icons presence...")
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check toggle button flag
        toggle_flag = soup.find('div', {'class': 'flag-icon'})
        if toggle_flag:
            print("✅ Flag icon found in toggle button")
        else:
            print("❌ Flag icon not found in toggle button")
        
        # Check dropdown flags
        dropdown_flags = soup.find_all('div', {'class': 'flag-icon'})
        if len(dropdown_flags) >= 2:
            print(f"✅ Found {len(dropdown_flags)} flag icons in dropdown")
        else:
            print(f"❌ Expected 2 flag icons, found {len(dropdown_flags)}")
    
    # Test 3: Check active state
    print("\n3. Testing active state...")
    response = requests.get(f"{BASE_URL}/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check which language is active
        active_item = soup.find('a', {'class': 'dropdown-item active'})
        if active_item:
            if 'English' in active_item.text:
                print("✅ English is marked as active (default)")
            elif 'Português' in active_item.text:
                print("✅ Portuguese is marked as active")
            else:
                print("⚠️  Active language not clearly identified")
        else:
            print("❌ No active language found")
    
    # Test 4: Test language switching
    print("\n4. Testing language switching...")
    
    # Switch to Portuguese
    response = requests.get(f"{BASE_URL}/change-language/pt_br")
    if response.status_code == 302:
        print("✅ Language switch to Portuguese successful")
        
        # Check if cookie was set
        cookies = response.cookies
        if 'language' in cookies and cookies['language'] == 'pt_br':
            print("✅ Portuguese language cookie set correctly")
        else:
            print("❌ Language cookie not set correctly")
    else:
        print(f"❌ Language switch failed: {response.status_code}")
    
    # Test 5: Check Portuguese page
    print("\n5. Testing Portuguese page...")
    session = requests.Session()
    session.cookies.set('language', 'pt_br', domain='localhost')
    
    response = session.get(f"{BASE_URL}/")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Check if Portuguese is now active
        active_item = soup.find('a', {'class': 'dropdown-item active'})
        if active_item and 'Português' in active_item.text:
            print("✅ Portuguese is now marked as active")
        else:
            print("❌ Portuguese not marked as active")
        
        # Check if page content is in Portuguese
        if 'Sistema de Avaliação SOC CMM' in response.text:
            print("✅ Page content is in Portuguese")
        else:
            print("⚠️  Could not verify Portuguese content")
    
    print("\n" + "=" * 50)
    print("🎉 Language dropdown testing completed!")
    print("\nManual testing instructions:")
    print("1. Open http://localhost:8400")
    print("2. Verify dropdown is hidden by default")
    print("3. Click the language selector (flag icon)")
    print("4. Verify dropdown appears with flag icons")
    print("5. Verify current language is highlighted")
    print("6. Click on a different language")
    print("7. Verify page changes language and dropdown closes")

if __name__ == "__main__":
    try:
        test_language_dropdown()
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the server. Make sure it's running on http://localhost:8400")
    except Exception as e:
        print(f"❌ Test failed with error: {e}") 