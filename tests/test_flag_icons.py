#!/usr/bin/env python3
"""
Test script to verify flag icons are displaying correctly
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://localhost:8400"

def test_flag_icons():
    """Test if flag icons are displaying correctly"""
    
    print("🏁 Testing Flag Icons Display")
    print("=" * 40)
    
    try:
        # Test 1: Check if server is running
        print("\n1. Checking server status...")
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running")
        else:
            print(f"❌ Server returned status {response.status_code}")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to server. Please start the server with: python3 main.py")
        return
    except Exception as e:
        print(f"❌ Error connecting to server: {e}")
        return
    
    # Test 2: Check flag icons in HTML
    print("\n2. Checking flag icons in HTML...")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all flag icons
    flag_icons = soup.find_all('div', {'class': 'flag-icon'})
    print(f"✅ Found {len(flag_icons)} flag icons")
    
    # Check specific flag classes
    en_flags = soup.find_all('div', {'class': 'flag-icon en'})
    pt_br_flags = soup.find_all('div', {'class': 'flag-icon pt-br'})
    
    print(f"   - English flags: {len(en_flags)}")
    print(f"   - Portuguese flags: {len(pt_br_flags)}")
    
    # Test 3: Check language selector structure
    print("\n3. Checking language selector structure...")
    language_selector = soup.find('div', {'class': 'language-selector'})
    
    if language_selector:
        print("✅ Language selector found")
        
        # Check for language links
        language_links = language_selector.find_all('a', {'class': 'dropdown-item'})
        print(f"✅ Found {len(language_links)} language links")
        
        for link in language_links:
            text = link.get_text(strip=True)
            href = link.get('href', '')
            classes = link.get('class', [])
            
            print(f"   - Link: {text} -> {href}")
            print(f"     Classes: {classes}")
            
            # Check if it has a flag icon
            flag = link.find('div', {'class': 'flag-icon'})
            if flag:
                flag_classes = flag.get('class', [])
                print(f"     Flag classes: {flag_classes}")
            else:
                print("     ❌ No flag icon found")
    else:
        print("❌ Language selector not found")
    
    # Test 4: Check for active state
    print("\n4. Checking active state...")
    active_links = soup.find_all('a', {'class': 'dropdown-item active'})
    
    if active_links:
        for link in active_links:
            text = link.get_text(strip=True)
            print(f"✅ Active language: {text}")
    else:
        print("⚠️  No active language found")
    
    # Test 5: Check CSS classes
    print("\n5. Checking CSS classes...")
    
    # Look for the specific CSS classes we added
    page_text = response.text
    
    if 'language-selector .dropdown-item .flag-icon' in page_text:
        print("✅ CSS for language selector flag icons found")
    else:
        print("⚠️  CSS for language selector flag icons not found")
    
    if 'flag-icon.en' in page_text or 'flag-icon.pt-br' in page_text:
        print("✅ Flag icon CSS classes found")
    else:
        print("⚠️  Flag icon CSS classes not found")
    
    print("\n" + "=" * 40)
    print("🎯 Manual Verification Steps:")
    print("1. Open http://localhost:8400 in your browser")
    print("2. Look at the top navigation bar")
    print("3. You should see: [🇺🇸 Eng] / [🇧🇷 Port]")
    print("4. The current language should be highlighted")
    print("5. Click on a language to switch")
    print("6. Verify the page content changes language")
    
    print("\n🔧 If flags are not showing:")
    print("- Check browser developer tools (F12)")
    print("- Look for CSS errors in the Console tab")
    print("- Verify the flag-icon divs are present in Elements tab")
    print("- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)")

if __name__ == "__main__":
    test_flag_icons() 