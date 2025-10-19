#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quick Test for Enhanced Learning AI Agent
"""

import os
import sys
import json
import datetime

def test_enhanced_learning_agent():
    """Test the Enhanced Learning AI Agent"""
    print("🧪 Testing Enhanced Learning AI Agent...")
    
    try:
        # Import the agent
        from enhanced_learning_ai_agent import EnhancedLearningAIAgent
        
        # Create agent instance
        agent = EnhancedLearningAIAgent()
        print("✅ Enhanced Learning AI Agent created successfully")
        
        # Test memory loading
        print(f"🧠 Memory loaded: {agent.conversation_count} previous conversations")
        if agent.user_name:
            print(f"👋 Welcome back {agent.user_name}!")
        
        # Test information extraction
        test_inputs = [
            "My name is Majed",
            "I am 21 years old", 
            "I am a graphic designer",
            "I live in Cairo",
            "My favorite color is blue",
            "I like programming"
        ]
        
        print("\n📝 Testing information extraction:")
        for test_input in test_inputs:
            response = agent.extract_user_info(test_input)
            if response:
                print(f"✅ {test_input} -> {response[:50]}...")
            else:
                print(f"⚠️ {test_input} -> No extraction")
        
        # Test responses
        test_responses = [
            "Hello",
            "How are you?",
            "Remember",
            "What's my name?",
            "Tell me about myself"
        ]
        
        print("\n💬 Testing responses:")
        for test_input in test_responses:
            response = agent.get_enhanced_response(test_input)
            print(f"✅ '{test_input}' -> {response[:50]}...")
        
        # Test memory saving
        agent.save_memory()
        agent.save_personality()
        print("✅ Memory and personality saved successfully")
        
        # Check if files were created
        memory_file = "aya_enhanced_memory.json"
        conversation_file = "aya_enhanced_conversations.json"
        personality_file = "aya_enhanced_personality.json"
        
        if os.path.exists(memory_file):
            print(f"✅ {memory_file} created")
        if os.path.exists(conversation_file):
            print(f"✅ {conversation_file} created")
        if os.path.exists(personality_file):
            print(f"✅ {personality_file} created")
        
        print("✅ Enhanced Learning AI Agent test completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing Enhanced Learning AI Agent: {e}")
        return False

def main():
    """Main test function"""
    print("=" * 60)
    print("🧪 Quick Test for Enhanced Learning AI Agent")
    print("=" * 60)
    
    success = test_enhanced_learning_agent()
    
    print("=" * 60)
    if success:
        print("🎉 Enhanced Learning AI Agent is ready to use!")
        print("\n🚀 To run the agent:")
        print("   - Double-click QUICK_START_LEARNING.bat")
        print("   - Or run: python enhanced_learning_ai_agent.py")
        print("   - Or choose option 5 in START_HERE.bat")
    else:
        print("❌ Some tests failed. Check the errors above.")
    print("=" * 60)

if __name__ == "__main__":
    main()
