#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import datetime

class SimpleAIAgent:
    def __init__(self):
        self.name = "Aya"
        self.conversation_count = 0
        
        # Response database
        self.responses = {
            "greetings": [
                "Hello there! I'm Aya, nice to meet you!",
                "Hi! How are you doing today?",
                "Hello! I'm Aya, how can I help you?",
                "Hey! Great to see you!",
                "Hi there! Welcome! I'm Aya."
            ],
            "how_are_you": [
                "I'm doing great, thank you! I'm happy to be talking with you!",
                "I'm wonderful! How are you doing?",
                "Excellent! Today is amazing, especially since I'm talking with you!",
                "I'm fantastic! Thanks for asking!"
            ],
            "help": [
                "Of course! I'm here to help you. What would you like to know?",
                "I love to help! Tell me how I can assist you",
                "My help is always available! What do you need?",
                "I'm here for you! Ask me anything"
            ],
            "farewell": [
                "Goodbye! It was wonderful talking with you!",
                "See you later! I hope you have a great day",
                "Take care! I look forward to seeing you again",
                "Goodbye! Enjoy your time!"
            ],
            "jokes": [
                "Why don't computers play cards? Because they're afraid of poker!",
                "What's the fastest animal in the forest? The turtle... when it's running from the wolf!",
                "Why doesn't the sun go to school? Because it's already bright!",
                "What's the only bird that can't fly? The penguin... because it prefers swimming!"
            ],
            "compliments": [
                "Oh, thank you! That's so kind of you",
                "You're wonderful too! Thanks for your nice words",
                "That makes me so happy! You're a great person",
                "Thank you! You're very kind"
            ],
            "default": [
                "That's interesting! Tell me more",
                "I understand what you mean, that's great!",
                "Really? That's new to me!",
                "I love this kind of conversation!",
                "That's exciting! Can you explain more?"
            ]
        }
    
    def get_current_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        return now.strftime("%H:%M")
    
    def get_current_date(self):
        """Get current date"""
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")
    
    def analyze_input(self, user_input):
        """Analyze user input"""
        input_lower = user_input.lower()
        
        # Keywords
        greeting_keywords = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"]
        how_are_you_keywords = ["how are you", "how do you do", "how's it going", "how are things"]
        help_keywords = ["help", "assist", "support", "can you help"]
        farewell_keywords = ["bye", "goodbye", "see you", "farewell", "take care"]
        joke_keywords = ["joke", "funny", "laugh", "humor", "tell me a joke"]
        time_keywords = ["time", "clock", "what time", "current time"]
        date_keywords = ["date", "today", "what date", "current date"]
        name_keywords = ["what's your name", "your name", "who are you", "name"]
        compliment_keywords = ["beautiful", "smart", "awesome", "great", "wonderful", "amazing"]
        
        if any(keyword in input_lower for keyword in greeting_keywords):
            return "greeting"
        elif any(keyword in input_lower for keyword in how_are_you_keywords):
            return "how_are_you"
        elif any(keyword in input_lower for keyword in help_keywords):
            return "help"
        elif any(keyword in input_lower for keyword in farewell_keywords):
            return "farewell"
        elif any(keyword in input_lower for keyword in joke_keywords):
            return "joke"
        elif any(keyword in input_lower for keyword in time_keywords):
            return "time"
        elif any(keyword in input_lower for keyword in date_keywords):
            return "date"
        elif any(keyword in input_lower for keyword in name_keywords):
            return "name"
        elif any(keyword in input_lower for keyword in compliment_keywords):
            return "compliment"
        else:
            return "default"
    
    def get_response(self, user_input):
        """Get response from AI agent"""
        self.conversation_count += 1
        
        # Analyze input
        intent = self.analyze_input(user_input)
        
        # Choose appropriate response
        if intent == "greeting":
            response = random.choice(self.responses["greetings"])
        elif intent == "how_are_you":
            response = random.choice(self.responses["how_are_you"])
        elif intent == "help":
            response = random.choice(self.responses["help"])
        elif intent == "farewell":
            response = random.choice(self.responses["farewell"])
        elif intent == "joke":
            response = random.choice(self.responses["jokes"])
        elif intent == "compliment":
            response = random.choice(self.responses["compliments"])
        elif intent == "time":
            current_time = self.get_current_time()
            response = f"The current time is {current_time}"
        elif intent == "date":
            current_date = self.get_current_date()
            response = f"Today's date is {current_date}"
        elif intent == "name":
            response = f"I'm {self.name}! Nice to meet you"
        else:
            response = random.choice(self.responses["default"])
        
        # Add some spontaneous expressions
        if self.conversation_count > 3:
            expressions = [" :)", " :D", " ^_^", " :)"]
            response += random.choice(expressions)
        
        return response
    
    def chat(self):
        """Start interactive conversation"""
        print(f"AI Agent: Hello! I'm {self.name}, your friendly AI assistant!")
        print("Type 'exit' or 'quit' to end the conversation")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    farewell = random.choice(self.responses["farewell"])
                    print(f"\n{self.name}: {farewell}")
                    break
                
                if not user_input:
                    print(f"\n{self.name}: I can't hear you, can you repeat that?")
                    continue
                
                response = self.get_response(user_input)
                print(f"\n{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Have a wonderful day!")
                break
            except Exception as e:
                print(f"\n{self.name}: Sorry, something went wrong. Can you try again?")

def main():
    """Main function"""
    agent = SimpleAIAgent()
    agent.chat()

if __name__ == "__main__":
    main()
