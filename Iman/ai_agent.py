#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple AI Agent
A basic conversational AI agent that can respond to user input.
"""

import random
import json
from datetime import datetime
from typing import Dict, List, Optional

class SimpleAIAgent:
    """A simple AI agent with basic conversational capabilities."""
    
    def __init__(self):
        self.name = "Simple AI Agent"
        self.version = "1.0.0"
        self.conversation_history = []
        self.responses = {
            "greeting": [
                "مرحباً! كيف يمكنني مساعدتك اليوم؟",
                "أهلاً وسهلاً! أنا هنا لمساعدتك.",
                "مرحباً! أنا AI Agent بسيط، كيف حالك؟"
            ],
            "farewell": [
                "وداعاً! أتمنى لك يوماً رائعاً!",
                "مع السلامة! أرجو أن أكون قد ساعدتك.",
                "إلى اللقاء! لا تتردد في العودة."
            ],
            "help": [
                "يمكنني مساعدتك في:",
                "- الإجابة على الأسئلة البسيطة",
                "- إجراء محادثة ودية",
                "- تقديم معلومات عامة",
                "- مساعدتك في المهام البسيطة"
            ],
            "default": [
                "هذا سؤال مثير للاهتمام!",
                "دعني أفكر في ذلك...",
                "أفهم ما تقصده.",
                "هذا موضوع مهم جداً.",
                "شكراً لك على مشاركة ذلك معي."
            ]
        }
    
    def greet(self) -> str:
        """Return a greeting message."""
        return random.choice(self.responses["greeting"])
    
    def farewell(self) -> str:
        """Return a farewell message."""
        return random.choice(self.responses["farewell"])
    
    def get_help(self) -> str:
        """Return help information."""
        return "\n".join(self.responses["help"])
    
    def process_input(self, user_input: str) -> str:
        """Process user input and generate a response."""
        user_input = user_input.strip().lower()
        
        # Log the conversation
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "response": ""
        })
        
        # Simple keyword matching for responses
        if any(word in user_input for word in ["مرحبا", "أهلا", "سلام", "hello", "hi"]):
            response = self.greet()
        elif any(word in user_input for word in ["وداع", "مع السلامة", "bye", "goodbye"]):
            response = self.farewell()
        elif any(word in user_input for word in ["مساعدة", "help", "ماذا يمكنك"]):
            response = self.get_help()
        elif any(word in user_input for word in ["اسمك", "من أنت", "what is your name"]):
            response = f"أنا {self.name} - نسخة {self.version}"
        elif any(word in user_input for word in ["الوقت", "الساعة", "time"]):
            response = f"الوقت الحالي هو: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        elif any(word in user_input for word in ["كيف حالك", "how are you"]):
            response = "أنا بخير، شكراً لك! كيف حالك أنت؟"
        else:
            response = random.choice(self.responses["default"])
        
        # Update conversation history with response
        self.conversation_history[-1]["response"] = response
        
        return response
    
    def get_conversation_history(self) -> List[Dict]:
        """Return the conversation history."""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []
    
    def get_stats(self) -> Dict:
        """Return basic statistics about the agent."""
        return {
            "name": self.name,
            "version": self.version,
            "total_conversations": len(self.conversation_history),
            "last_interaction": self.conversation_history[-1]["timestamp"] if self.conversation_history else None
        }

def main():
    """Main function to run the AI agent in interactive mode."""
    agent = SimpleAIAgent()
    
    print("=" * 50)
    print(f"🤖 {agent.name} v{agent.version}")
    print("=" * 50)
    print(agent.greet())
    print("\nاكتب 'exit' أو 'quit' للخروج")
    print("اكتب 'help' للمساعدة")
    print("اكتب 'stats' لعرض الإحصائيات")
    print("اكتب 'clear' لمسح تاريخ المحادثة")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nأنت: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'خروج']:
                print(f"\n{agent.farewell()}")
                break
            elif user_input.lower() == 'help':
                print(f"\n{agent.get_help()}")
            elif user_input.lower() == 'stats':
                stats = agent.get_stats()
                print(f"\n📊 الإحصائيات:")
                print(f"الاسم: {stats['name']}")
                print(f"الإصدار: {stats['version']}")
                print(f"عدد المحادثات: {stats['total_conversations']}")
                if stats['last_interaction']:
                    print(f"آخر تفاعل: {stats['last_interaction']}")
            elif user_input.lower() == 'clear':
                agent.clear_history()
                print("\n✅ تم مسح تاريخ المحادثة")
            elif user_input:
                response = agent.process_input(user_input)
                print(f"\n{agent.name}: {response}")
            else:
                print("يرجى إدخال رسالة...")
                
        except KeyboardInterrupt:
            print(f"\n\n{agent.farewell()}")
            break
        except Exception as e:
            print(f"\n❌ حدث خطأ: {e}")

if __name__ == "__main__":
    main()
