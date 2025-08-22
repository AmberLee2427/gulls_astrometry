#!/usr/bin/env python3
"""
Simple test runner script for GullsParser tests.
Run this script to execute all tests.
"""

import sys
import subprocess
import pathlib


def run_tests():
    """Run all tests for the GullsParser module."""
    
    # Get the project root directory
    project_root = pathlib.Path(__file__).parent
    
    print("=" * 60)
    print("Running GullsParser Tests")
    print("=" * 60)
    
    try:
        # Try to run pytest
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            str(project_root / "tests"),
            "-v",
            "--tb=short"
        ], cwd=project_root, capture_output=False)
        
        if result.returncode == 0:
            print("\n" + "=" * 60)
            print("All tests passed! ✅")
            print("=" * 60)
        else:
            print("\n" + "=" * 60)
            print("Some tests failed! ❌")
            print("=" * 60)
            return False
            
    except FileNotFoundError:
        print("pytest not found. Please install test requirements:")
        print("pip install -r requirements-test.txt")
        return False
    
    except Exception as e:
        print(f"Error running tests: {e}")
        return False
    
    return True


def check_requirements():
    """Check if test requirements are installed."""
    required_packages = ['pytest', 'pandas', 'numpy']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        print("Missing required packages:")
        for pkg in missing:
            print(f"  - {pkg}")
        print("\nInstall with: pip install -r requirements-test.txt")
        return False
    
    return True


if __name__ == "__main__":
    print("Checking requirements...")
    if not check_requirements():
        sys.exit(1)
    
    print("Requirements OK. Running tests...\n")
    success = run_tests()
    
    if not success:
        sys.exit(1)
