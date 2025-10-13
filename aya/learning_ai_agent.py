#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import datetime
import os

class LearningAIAgent:
    def __init__(self):
        self.name = "Aya"
        self.conversation_count = 0
        self.user_name = ""
        
        # ملفات حفظ البيانات
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(script_dir, "aya_memory.json")
        self.conversation_file = os.path.join(script_dir, "aya_conversations.json")
        
        # بيانات إضافية للتعلم
        self.user_info = {
            "name": "",
            "age": "",
            "location": "",
            "interests": [],
            "favorite_topics": [],
            "conversation_count": 0
        }
        
        self.conversation_history = []
        
        # تحميل البيانات المحفوظة
        self.load_memory()
        
        # قاعدة بيانات الردود
        self.responses = {
            "greetings": [
                "Hello there! I'm Aya, nice to meet you!",
                "Hi! How are you doing today?",
                "Hello! I'm Aya, how can I help you?",
                "Hey! Great to see you!"
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
            "learning": [
                "That's interesting! I'll remember that about you.",
                "Thanks for sharing that with me! I'm learning so much.",
                "Wow, I didn't know that! I'll keep that in mind.",
                "That's new information for me! Thanks for teaching me."
            ],
            "default": [
                "That's interesting! Tell me more",
                "I understand what you mean, that's great!",
                "Really? That's new to me!",
                "I love this kind of conversation!",
                "That's exciting! Can you explain more?"
            ]
        }
    
    def load_memory(self):
        """تحميل الذاكرة من الملف"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.user_info = data.get('user_info', self.user_info)
                    self.user_name = self.user_info.get('name', '')
                    self.conversation_count = self.user_info.get('conversation_count', 0)
                    print(f"Loaded memory: {self.conversation_count} previous conversations")
        except Exception as e:
            print(f"Error loading memory: {e}")
    
    def save_memory(self):
        """حفظ الذاكرة في الملف"""
        try:
            self.user_info['conversation_count'] = self.conversation_count
            data = {
                'user_info': self.user_info,
                'last_updated': datetime.datetime.now().isoformat()
            }
            
            # التأكد من وجود المجلد
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.flush()  # التأكد من كتابة البيانات
                f.close()  # إغلاق الملف بشكل صحيح
                
        except Exception as e:
            print(f"Error saving memory: {e}")
            print(f"File path: {self.data_file}")
    
    def save_conversation(self, user_input, response):
        """حفظ المحادثة"""
        try:
            conversation = {
                'timestamp': datetime.datetime.now().isoformat(),
                'user_input': user_input,
                'ai_response': response,
                'conversation_number': self.conversation_count
            }
            
            # تحميل المحادثات السابقة
            conversations = []
            if os.path.exists(self.conversation_file):
                with open(self.conversation_file, 'r', encoding='utf-8') as f:
                    conversations = json.load(f)
            
            # إضافة المحادثة الجديدة
            conversations.append(conversation)
            
            # حفظ المحادثات (الاحتفاظ بآخر 100 محادثة فقط)
            if len(conversations) > 100:
                conversations = conversations[-100:]
            
            # التأكد من وجود المجلد
            os.makedirs(os.path.dirname(self.conversation_file), exist_ok=True)
            
            with open(self.conversation_file, 'w', encoding='utf-8') as f:
                json.dump(conversations, f, ensure_ascii=False, indent=2)
                f.flush()  # التأكد من كتابة البيانات
                f.close()  # إغلاق الملف بشكل صحيح
                
        except Exception as e:
            print(f"Error saving conversation: {e}")
            print(f"File path: {self.conversation_file}")
    
    def extract_user_info(self, user_input):
        """استخراج معلومات المستخدم من المدخلات"""
        input_lower = user_input.lower()
        
        # استخراج الاسم
        name_patterns = ["my name is", "i am", "i'm", "call me"]
        for pattern in name_patterns:
            if pattern in input_lower:
                parts = user_input.split()
                for i, part in enumerate(parts):
                    if pattern in part.lower() and i + 1 < len(parts):
                        name = parts[i + 1]
                        if len(name) > 1 and name.isalpha():
                            self.user_name = name
                            self.user_info['name'] = name
                            return f"I'll remember your name {name}! Nice to meet you!"
        
        # استخراج العمر
        age_patterns = ["i am", "i'm", "my age is"]
        for pattern in age_patterns:
            if pattern in input_lower:
                words = user_input.split()
                for word in words:
                    if word.isdigit() and 5 <= int(word) <= 120:
                        self.user_info['age'] = word
                        return f"I'll remember that you're {word} years old!"
        
        # استخراج الموقع
        location_patterns = ["i live in", "i'm from", "i am from"]
        for pattern in location_patterns:
            if pattern in input_lower:
                parts = user_input.lower().split(pattern)
                if len(parts) > 1:
                    location = parts[1].strip().split()[0]
                    if len(location) > 2:
                        self.user_info['location'] = location.title()
                        return f"I'll remember that you're from {location.title()}!"
        
        # استخراج الاهتمامات
        interest_patterns = ["i like", "i love", "i enjoy", "my hobby is"]
        for pattern in interest_patterns:
            if pattern in input_lower:
                parts = user_input.lower().split(pattern)
                if len(parts) > 1:
                    interest = parts[1].strip()
                    if len(interest) > 2 and interest not in self.user_info['interests']:
                        self.user_info['interests'].append(interest)
                        return f"I'll remember that you like {interest}!"
        
        return None
    
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
        memory_keywords = ["remember", "do you remember", "recall"]
        info_keywords = ["tell me about", "what do you know about", "my info"]
        
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
        elif any(keyword in input_lower for keyword in memory_keywords):
            return "memory"
        elif any(keyword in input_lower for keyword in info_keywords):
            return "info"
        else:
            return "default"
    
    def get_response(self, user_input):
        """Get response from AI agent"""
        self.conversation_count += 1
        
        # محاولة استخراج معلومات المستخدم
        info_response = self.extract_user_info(user_input)
        if info_response:
            self.save_memory()
            return info_response
        
        # تحليل المدخلات
        intent = self.analyze_input(user_input)
        
        # اختيار الرد المناسب
        if intent == "greeting":
            if self.user_name:
                response = f"Hello {self.user_name}! Great to see you again!"
            else:
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
        elif intent == "memory":
            if self.user_info['name'] or self.user_info['age'] or self.user_info['location'] or self.user_info['interests']:
                info_parts = []
                if self.user_info['name']:
                    info_parts.append(f"your name is {self.user_info['name']}")
                if self.user_info['age']:
                    info_parts.append(f"you're {self.user_info['age']} years old")
                if self.user_info['location']:
                    info_parts.append(f"you're from {self.user_info['location']}")
                if self.user_info['interests']:
                    interests = ", ".join(self.user_info['interests'])
                    info_parts.append(f"you like {interests}")
                
                response = f"Yes! I remember that {', '.join(info_parts)}!"
            else:
                response = "I don't remember much about you yet. Tell me about yourself!"
        elif intent == "info":
            if self.user_info['name'] or self.user_info['age'] or self.user_info['location'] or self.user_info['interests']:
                response = "Here's what I know about you:\n"
                if self.user_info['name']:
                    response += f"- Name: {self.user_info['name']}\n"
                if self.user_info['age']:
                    response += f"- Age: {self.user_info['age']} years old\n"
                if self.user_info['location']:
                    response += f"- Location: {self.user_info['location']}\n"
                if self.user_info['interests']:
                    response += f"- Interests: {', '.join(self.user_info['interests'])}\n"
                response += f"- Total conversations: {self.conversation_count}"
            else:
                response = "I don't know much about you yet. Please tell me about yourself!"
        else:
            # Check if this looks like new information to learn
            if len(user_input.split()) > 3 and not any(keyword in user_input.lower() for keyword in ["?", "what", "how", "when", "where", "why"]):
                response = random.choice(self.responses["learning"])
            else:
                response = random.choice(self.responses["default"])
        
        # Add some spontaneous expressions
        if self.conversation_count > 3:
            expressions = [" :)", " :D", " ^_^", " *learning*"]
            response += random.choice(expressions)
        
        return response
    
    def chat(self):
        """Start interactive conversation"""
        print(f"AI Agent: Hello! I'm {self.name}, your friendly AI assistant!")
        print("I learn from our conversations and remember things about you!")
        print("Type 'exit' or 'quit' to end the conversation")
        
        # عرض المعلومات المحفوظة
        if self.user_info['name']:
            print(f"Welcome back {self.user_info['name']}! Nice to see you again!")
        if self.conversation_count > 0:
            print(f"This is conversation #{self.conversation_count + 1}")
        
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                    farewell = random.choice(self.responses["farewell"])
                    print(f"\n{self.name}: {farewell}")
                    # حفظ البيانات قبل الخروج
                    self.save_memory()
                    break
                
                if not user_input:
                    print(f"\n{self.name}: I can't hear you, can you repeat that?")
                    continue
                
                response = self.get_response(user_input)
                print(f"\n{self.name}: {response}")
                
                # حفظ المحادثة
                self.save_conversation(user_input, response)
                self.save_memory()
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! Have a wonderful day!")
                # حفظ البيانات قبل الخروج
                self.save_memory()
                break
            except Exception as e:
                print(f"\n{self.name}: Sorry, something went wrong. Can you try again?")
                print(f"Error: {str(e)}")

def main():
    """Main function"""
    agent = LearningAIAgent()
    agent.chat()

if __name__ == "__main__":
    main()
