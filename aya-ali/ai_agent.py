import json
import random
import datetime
from typing import Dict, List, Any

class SimpleAIAgent:
    def __init__(self):
        self.name = "Aya-Ali AI"
        self.memory_file = "agent_memory.json"
        self.conversations_file = "conversations.json"
        self.load_memory()
        self.load_conversations()
        
        # Basic response rules
        self.responses = {
            "greeting": [
                "Hello! I'm Aya-Ali AI, how can I help you today?",
                "Hi there! I'm here to assist you, what would you like to talk about?",
                "Welcome! I'm a simple AI agent, how are you doing?"
            ],
            "farewell": [
                "Goodbye! It was great talking with you",
                "See you later! I hope I was able to help you",
                "Take care! Feel free to chat with me anytime"
            ],
            "help": [
                "I can chat with you about any topic you want!",
                "Ask me anything and I'll try to help you",
                "I'm here to answer your questions and chat with you"
            ],
            "question": [
                "That's a great question! Let me think about that",
                "Interesting! Can you tell me more about that?",
                "I'd be happy to help with that. What specifically would you like to know?"
            ],
            "compliment": [
                "Thank you! That's very kind of you",
                "I appreciate that! You're very nice",
                "That means a lot to me, thank you!"
            ],
            "default": [
                "That's interesting! Tell me more about it",
                "I understand, would you like to talk about something else?",
                "Great! What do you think about this topic?",
                "Fascinating! I'd love to hear more",
                "That sounds cool! Can you elaborate?"
            ]
        }
        
        # Keywords for conversation type detection
        self.keywords = {
            "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings", "welcome"],
            "farewell": ["goodbye", "bye", "see you", "farewell", "take care", "later", "exit", "quit"],
            "help": ["help", "assist", "what can you do", "how can you help", "support"],
            "question": ["what", "how", "why", "where", "when", "who", "which", "?"],
            "compliment": ["thank you", "thanks", "appreciate", "great", "awesome", "amazing", "wonderful", "excellent"]
        }

    def load_memory(self):
        """Load agent memory"""
        try:
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                self.memory = json.load(f)
        except FileNotFoundError:
            self.memory = {
                "user_preferences": {},
                "conversation_history": [],
                "learned_patterns": {}
            }

    def save_memory(self):
        """Save agent memory"""
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=2)

    def load_conversations(self):
        """Load conversation history"""
        try:
            with open(self.conversations_file, 'r', encoding='utf-8') as f:
                self.conversations = json.load(f)
        except FileNotFoundError:
            self.conversations = []

    def save_conversations(self):
        """Save conversation history"""
        with open(self.conversations_file, 'w', encoding='utf-8') as f:
            json.dump(self.conversations, f, ensure_ascii=False, indent=2)

    def detect_intent(self, message: str) -> str:
        """Detect user intent from message"""
        message_lower = message.lower()
        
        for intent, keywords in self.keywords.items():
            for keyword in keywords:
                if keyword in message_lower:
                    return intent
        
        return "default"

    def generate_response(self, user_message: str) -> str:
        """Generate response to message"""
        intent = self.detect_intent(user_message)
        
        # Save conversation
        conversation = {
            "timestamp": datetime.datetime.now().isoformat(),
            "user_message": user_message,
            "intent": intent
        }
        
        # Generate response
        if intent in self.responses:
            response = random.choice(self.responses[intent])
        else:
            response = random.choice(self.responses["default"])
        
        conversation["agent_response"] = response
        self.conversations.append(conversation)
        
        # Save conversation and memory
        self.save_conversations()
        self.save_memory()
        
        return response

    def chat(self):
        """Start interactive chat"""
        print(f"🤖 {self.name} - AI Agent")
        print("=" * 50)
        print("Type 'exit' or 'quit' to end the conversation")
        print("Type 'help' for assistance")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    print(f"\n🤖 {self.name}: {random.choice(self.responses['farewell'])}")
                    break
                
                if not user_input:
                    continue
                
                response = self.generate_response(user_input)
                print(f"\n🤖 {self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n🤖 {self.name}: {random.choice(self.responses['farewell'])}")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("🤖 Please try again...")

    def get_conversation_stats(self):
        """Get conversation statistics"""
        total_conversations = len(self.conversations)
        if total_conversations == 0:
            return "No conversations yet"
        
        intents = {}
        for conv in self.conversations:
            intent = conv.get('intent', 'unknown')
            intents[intent] = intents.get(intent, 0) + 1
        
        stats = f"Total conversations: {total_conversations}\n"
        stats += "Conversation types:\n"
        for intent, count in intents.items():
            stats += f"  - {intent}: {count}\n"
        
        return stats

if __name__ == "__main__":
    agent = SimpleAIAgent()
    agent.chat()
