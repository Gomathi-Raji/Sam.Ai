"""
Quick test script to verify Web UI setup
Tests:
1. Flask imports
2. SocketIO imports
3. Template file exists
4. Dependencies installed
"""

import sys
import os

def test_imports():
    """Test all required imports"""
    print("🔍 Testing imports...")
    
    try:
        import flask
        print("  ✅ Flask installed")
    except ImportError:
        print("  ❌ Flask not installed")
        return False
    
    try:
        import flask_socketio
        print("  ✅ Flask-SocketIO installed")
    except ImportError:
        print("  ❌ Flask-SocketIO not installed")
        return False
    
    try:
        import pygame
        print("  ✅ Pygame installed")
    except ImportError:
        print("  ❌ Pygame not installed")
        return False
    
    return True

def test_files():
    """Test required files exist"""
    print("\n🔍 Testing required files...")
    
    files_to_check = [
        'web_ui.py',
        'templates/orb_ui.html',
        'voice/listener.py',
        'voice/speaker.py',
        'ai/gemini_ai.py',
    ]
    
    all_exist = True
    for file_path in files_to_check:
        full_path = os.path.join('/workspaces/Sam.Ai', file_path)
        if os.path.exists(full_path):
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} not found")
            all_exist = False
    
    return all_exist

def test_web_ui_module():
    """Test web_ui module can be imported"""
    print("\n🔍 Testing web_ui module...")
    
    sys.path.insert(0, '/workspaces/Sam.Ai')
    
    try:
        import web_ui
        print("  ✅ web_ui module can be imported")
        
        # Check if start_server function exists
        if hasattr(web_ui, 'start_server'):
            print("  ✅ start_server function exists")
        else:
            print("  ❌ start_server function not found")
            return False
        
        return True
    except Exception as e:
        print(f"  ❌ Error importing web_ui: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("Zara AI - Web UI Setup Test")
    print("=" * 50)
    
    tests = [
        ("Imports", test_imports),
        ("Files", test_files),
        ("Web UI Module", test_web_ui_module),
    ]
    
    results = []
    for test_name, test_func in tests:
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 50)
    print("Test Results:")
    print("=" * 50)
    
    all_passed = True
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")
        if not result:
            all_passed = False
    
    print("=" * 50)
    
    if all_passed:
        print("\n🎉 All tests passed! You can now run:")
        print("   python main.py")
        print("\nOr use the startup script:")
        print("   ./start_web_ui.sh")
        print("\nThen open http://localhost:5000 in your browser")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("Run: pip install -r requirements.txt")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
