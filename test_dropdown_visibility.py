#!/usr/bin/env python3
"""
Test script to verify dropdown visibility
"""

import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "http://localhost:8400"

def test_dropdown_visibility():
    """Test if dropdown is properly hidden by default"""
    
    print("🔍 Testing Dropdown Visibility")
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
    
    # Test 2: Check dropdown HTML structure
    print("\n2. Checking dropdown HTML structure...")
    soup = BeautifulSoup(response.text, 'html.parser')
    dropdown = soup.find('div', {'id': 'languageDropdown'})
    
    if dropdown:
        print("✅ Language dropdown found in HTML")
        
        # Check if dropdown has the 'show' class
        classes = dropdown.get('class', [])
        if 'show' in classes:
            print("❌ Dropdown has 'show' class by default (should be hidden)")
        else:
            print("✅ Dropdown does not have 'show' class (correct)")
        
        # Check dropdown items
        items = dropdown.find_all('a', {'class': 'dropdown-item'})
        print(f"✅ Found {len(items)} dropdown items")
        
        for item in items:
            text = item.get_text(strip=True)
            if 'English' in text or 'Português' in text:
                print(f"   - {text}")
    else:
        print("❌ Language dropdown not found in HTML")
        return
    
    # Test 3: Check CSS classes and inline styles
    print("\n3. Checking CSS and styles...")
    
    # Look for any inline styles that might show the dropdown
    if 'style=' in str(dropdown):
        print("⚠️  Dropdown has inline styles - checking...")
        style_attr = dropdown.get('style', '')
        if 'display: block' in style_attr or 'display:block' in style_attr:
            print("❌ Dropdown has inline display:block style")
        elif 'display: none' in style_attr or 'display:none' in style_attr:
            print("✅ Dropdown has inline display:none style")
        else:
            print("ℹ️  Dropdown has other inline styles")
    else:
        print("✅ No inline styles found on dropdown")
    
    # Test 4: Check if dropdown items are visible in the rendered HTML
    print("\n4. Checking dropdown items visibility...")
    
    # Look for the text content that should be hidden
    page_text = response.text
    if 'English' in page_text and 'Português' in page_text:
        # Check if they appear in the navigation area
        nav_section = soup.find('nav', {'class': 'navbar'})
        if nav_section:
            nav_text = nav_section.get_text()
            if 'English' in nav_text and 'Português' in nav_text:
                print("⚠️  Language options found in navigation text")
                print("   This might indicate the dropdown is visible")
            else:
                print("✅ Language options not found in navigation text")
        else:
            print("⚠️  Could not find navigation section")
    else:
        print("✅ Language options not found in page text")
    
    print("\n" + "=" * 40)
    print("🎯 Manual Verification Steps:")
    print("1. Open http://localhost:8400 in your browser")
    print("2. Look at the top navigation bar")
    print("3. You should see a language selector button (with flag)")
    print("4. The dropdown should NOT be visible by default")
    print("5. Click the language selector to see the dropdown")
    print("6. The dropdown should appear with flag icons")
    print("7. Click outside to close the dropdown")
    
    print("\n🔧 If dropdown is still visible:")
    print("- Clear browser cache (Ctrl+F5 or Cmd+Shift+R)")
    print("- Check browser developer tools for CSS conflicts")
    print("- Verify the server is running the latest code")

if __name__ == "__main__":
    test_dropdown_visibility() 