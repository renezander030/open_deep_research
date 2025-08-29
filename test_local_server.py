#!/usr/bin/env python3
"""
Test script to verify the local LangGraph server is working with Azure OpenAI.
"""

import requests
import json

def test_local_server():
    """Test if the local LangGraph server is responding."""
    
    base_url = "http://127.0.0.1:2024"
    
    try:
        # Test if server is running
        response = requests.get(f"{base_url}/docs")
        if response.status_code == 200:
            print("✅ Local LangGraph server is running!")
            print(f"📚 API Documentation: {base_url}/docs")
            print(f"🚀 API Base URL: {base_url}")
        else:
            print(f"❌ Server responded with status code: {response.status_code}")
            return False
            
        # Test if we can get the available graphs/assistants
        try:
            assistants_response = requests.get(f"{base_url}/assistants")
            if assistants_response.status_code == 200:
                assistants = assistants_response.json()
                print(f"📋 Available assistants: {len(assistants)}")
                for assistant in assistants:
                    print(f"   - {assistant.get('assistant_id', 'Unknown')}")
            else:
                print(f"⚠️  Could not fetch assistants: {assistants_response.status_code}")
        except Exception as e:
            print(f"⚠️  Error fetching assistants: {e}")
            
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to local server. Make sure it's running on port 2024.")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("Testing local LangGraph server...")
    test_local_server()
    print("\nNext steps:")
    print("1. Visit http://127.0.0.1:2024/docs to see the API documentation")
    print("2. You can test your Azure OpenAI configuration by making API calls")
    print("3. The LangSmith Studio UI is optional - your server works independently!")
