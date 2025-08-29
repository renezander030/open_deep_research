#!/usr/bin/env python3
"""
Test script to verify Azure OpenAI configuration works with the updated codebase.
"""

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

def test_azure_openai_connection():
    """Test if Azure OpenAI connection works with the current configuration."""
    
    print("Testing Azure OpenAI configuration...")
    print(f"AZURE_OPENAI_ENDPOINT: {os.getenv('AZURE_OPENAI_ENDPOINT')}")
    print(f"AZURE_OPENAI_API_KEY: {'***' + os.getenv('AZURE_OPENAI_API_KEY', '')[-4:] if os.getenv('AZURE_OPENAI_API_KEY') else 'Not set'}")
    print(f"AZURE_OPENAI_API_VERSION: {os.getenv('AZURE_OPENAI_API_VERSION')}")
    
    try:
        # Test with azure_openai provider
        model = init_chat_model(
            model="azure_openai:gpt-4.1-mini",
            api_key=os.getenv("AZURE_AI_API_KEY"),
            max_tokens=100
        )
        
        # Test a simple message
        response = model.invoke([HumanMessage(content="Hello, this is a test message. Please respond with 'Azure OpenAI is working!'")])
        
        print("✅ Success! Azure OpenAI is working correctly.")
        print(f"Response: {response.content}")
        return True
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Verify your Azure OpenAI deployment name matches 'gpt-4.1-mini'")
        print("2. Check that your Azure OpenAI endpoint and API key are correct")
        print("3. Ensure your deployment is active and has quota available")
        return False

if __name__ == "__main__":
    test_azure_openai_connection()
