#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Agent - Norhan's Interactive Assistant
A friendly AI agent that can interact with users in Arabic and English
"""

import random
import datetime
import json
import os
from typing import Dict, List, Any

class NorhanAI:
    def __init__(self):
        self.name = "نورهان"  # Norhan in Arabic
        self.english_name = "Norhan"
        self.conversation_count = 0
        self.user_preferences = {}
        self.memory_file = "conversation_memory.json"
        self.load_memory()
        
        # Arabic responses
        self.arabic_responses = {
            "greeting": [
                "أهلاً وسهلاً! أنا نورهان، مسرورة بلقائك! 🌟",
                "مرحباً! كيف حالك؟ أنا نورهان 🤗",
                "أهلاً بك! نورهان في خدمتك ✨",
                "مرحبا! أنا نورهان، مساعدة الذكاء الاصطناعي 😊"
            ],
            "how_are_you": [
                "أنا بخير، شكراً لك! سعيد لأني أتحدث معك 🌸",
                "الحمد لله، أنا بخير! وأنت كيف حالك؟ 😊",
                "أشعر بالراحة، شكراً! كيف يمكنني مساعدتك؟ 💫",
                "بخير والحمد لله! سعيد لوجودك هنا 🌺"
            ],
            "help": [
                "أنا هنا لمساعدتك! يمكنني الإجابة على أسئلتك وإجراء محادثات ممتعة 🌟",
                "يمكنني مساعدتك في العديد من الأشياء! فقط اسأل 😊",
                "أنا جاهزة لخدمتك! ماذا تريد أن نناقش؟ 💭",
                "سأساعدك بكل سرور! ما الذي تحتاجه؟ 🤝"
            ],
            "farewell": [
                "وداعاً! كان من دواعي سروري التحدث معك! 🌸",
                "مع السلامة! أتمنى لك يوماً رائعاً! ✨",
                "إلى اللقاء! أتمنى أن نلتقي مرة أخرى! 💫",
                "وداعاً! شكراً لك على المحادثة الجميلة! 🌺"
            ],
            "joke": [
                "لماذا لا تذهب الأسماك إلى المدرسة؟ لأنها تسبح في الماء! 🐟",
                "ما هو الشيء الذي له رأس وذيل لكن ليس له جسم؟ عملة معدنية! 🪙",
                "لماذا الطيور تطير جنوباً في الشتاء؟ لأن المشي يستغرق وقتاً طويلاً! 🐦",
                "ما هو الشيء الذي كلما أخذت منه أكثر، كلما كبر؟ الحفرة! 🕳️"
            ],
            "compliment": [
                "أنت رائع! شكراً لك على كلماتك اللطيفة! 🌟",
                "هذا لطف منك! أنت أيضاً شخص رائع! 😊",
                "شكراً لك! كلماتك تجعلني سعيدة! 💖",
                "أنت لطيف جداً! أقدّر كلماتك الجميلة! ✨"
            ],
            "name": [
                "أنا نورهان، مساعدة الذكاء الاصطناعي! 😊",
                "اسمي نورهان، في خدمتك! 🌸",
                "أنا نورهان، جاهزة لمساعدتك! 💫",
                "نورهان اسمي، مسرورة بلقائك! 🌟"
            ],
            "unknown": [
                "عذراً، لم أفهم ذلك. هل يمكنك إعادة صياغة السؤال؟ 🤔",
                "مثير للاهتمام! هل يمكنك توضيح ما تقصده؟ 💭",
                "لم أتمكن من فهم ذلك تماماً. هل يمكنك مساعدتي؟ 😊",
                "هذا سؤال ممتع! هل يمكنك شرح المزيد؟ 🌟"
            ]
        }
        
        # English responses
        self.english_responses = {
            "greeting": [
                "Hello there! I'm Norhan, nice to meet you! 🌟",
                "Hi! How are you? I'm Norhan 🤗",
                "Welcome! Norhan at your service ✨",
                "Hello! I'm Norhan, your AI assistant 😊"
            ],
            "how_are_you": [
                "I'm doing great, thank you! Happy to be talking with you! 🌸",
                "I'm fine, thanks! How are you doing? 😊",
                "I'm feeling good, thank you! How can I help you? 💫",
                "I'm doing well! Glad you're here 🌺"
            ],
            "help": [
                "I'm here to help! I can answer questions and have fun conversations 🌟",
                "I can help you with many things! Just ask 😊",
                "I'm ready to serve you! What would you like to discuss? 💭",
                "I'll be happy to help! What do you need? 🤝"
            ],
            "farewell": [
                "Goodbye! It was wonderful talking with you! 🌸",
                "Take care! Have a great day! ✨",
                "See you later! Hope we meet again! 💫",
                "Farewell! Thanks for the lovely conversation! 🌺"
            ],
            "joke": [
                "Why don't fish go to school? Because they're already swimming in water! 🐟",
                "What has a head and a tail but no body? A coin! 🪙",
                "Why do birds fly south for winter? Because walking takes too long! 🐦",
                "What gets bigger the more you take away from it? A hole! 🕳️"
            ],
            "compliment": [
                "You're wonderful! Thank you for your kind words! 🌟",
                "That's very sweet of you! You're amazing too! 😊",
                "Thank you! Your words make me happy! 💖",
                "You're so kind! I appreciate your beautiful words! ✨"
            ],
            "name": [
                "I'm Norhan, your AI assistant! 😊",
                "My name is Norhan, at your service! 🌸",
                "I'm Norhan, ready to help you! 💫",
                "My name is Norhan, pleased to meet you! 🌟"
            ],
            "unknown": [
                "Sorry, I didn't understand that. Can you rephrase your question? 🤔",
                "Interesting! Can you clarify what you mean? 💭",
                "I couldn't quite understand that. Can you help me? 😊",
                "That's a fascinating question! Can you explain more? 🌟"
            ]
        }
        
        # Keywords for detecting response types
        self.arabic_keywords = {
            "greeting": ["أهلاً", "مرحباً", "السلام", "هلا", "أهلا", "مرحبا", "hello", "hi", "hey"],
            "how_are_you": ["كيف", "حالك", "أحوالك", "أخبارك", "how are you", "how do you do"],
            "help": ["مساعدة", "ساعد", "مساعدة", "help", "assist", "support"],
            "farewell": ["وداعاً", "مع السلامة", "إلى اللقاء", "bye", "goodbye", "see you", "exit", "quit"],
            "joke": ["نكتة", "نكت", "ضحك", "joke", "funny", "laugh"],
            "compliment": ["جميل", "رائع", "ممتاز", "beautiful", "awesome", "great", "smart"],
            "name": ["اسمك", "من أنت", "name", "who are you"],
            "time": ["وقت", "ساعة", "time", "clock"],
            "date": ["تاريخ", "يوم", "date", "today"]
        }
        
        self.english_keywords = {
            "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"],
            "how_are_you": ["how are you", "how do you do", "how's it going"],
            "help": ["help", "assist", "support", "what can you do"],
            "farewell": ["bye", "goodbye", "see you", "exit", "quit", "leave"],
            "joke": ["joke", "funny", "tell me a joke", "laugh"],
            "compliment": ["beautiful", "awesome", "great", "smart", "amazing", "wonderful"],
            "name": ["name", "who are you", "what's your name"],
            "time": ["time", "clock", "what time", "current time"],
            "date": ["date", "today", "what date", "current date"]
        }

    def load_memory(self):
        """Load conversation memory from file"""
        try:
            if os.path.exists(self.memory_file):
                with open(self.memory_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.conversation_count = data.get('conversation_count', 0)
                    self.user_preferences = data.get('user_preferences', {})
        except Exception as e:
            print(f"Could not load memory: {e}")

    def save_memory(self):
        """Save conversation memory to file"""
        try:
            data = {
                'conversation_count': self.conversation_count,
                'user_preferences': self.user_preferences
            }
            with open(self.memory_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Could not save memory: {e}")

    def detect_language(self, text: str) -> str:
        """Detect if text is in Arabic or English"""
        arabic_chars = sum(1 for char in text if '\u0600' <= char <= '\u06FF')
        return "arabic" if arabic_chars > len(text) / 3 else "english"

    def get_response_type(self, text: str, language: str) -> str:
        """Determine the type of response needed"""
        text_lower = text.lower()
        
        keywords = self.arabic_keywords if language == "arabic" else self.english_keywords
        
        for response_type, keyword_list in keywords.items():
            for keyword in keyword_list:
                if keyword.lower() in text_lower:
                    return response_type
        
        return "unknown"

    def get_time_response(self, language: str) -> str:
        """Get current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M")
        
        if language == "arabic":
            return f"الوقت الحالي هو {time_str} 🕐"
        else:
            return f"The current time is {time_str} 🕐"

    def get_date_response(self, language: str) -> str:
        """Get current date"""
        now = datetime.datetime.now()
        
        if language == "arabic":
            date_str = now.strftime("%Y-%m-%d")
            return f"التاريخ اليوم هو {date_str} 📅"
        else:
            date_str = now.strftime("%B %d, %Y")
            return f"Today's date is {date_str} 📅"

    def get_personalized_response(self, response_type: str, language: str) -> str:
        """Get a personalized response based on conversation history"""
        responses = self.arabic_responses if language == "arabic" else self.english_responses
        response_list = responses.get(response_type, responses["unknown"])
        
        # Make responses more personal after a few conversations
        if self.conversation_count > 3:
            if language == "arabic":
                personal_additions = [
                    " أتذكر أننا تحدثنا من قبل! 😊",
                    " لطيف أن أراكم مرة أخرى! 🌸",
                    " سعيد بأنك عدت! 💫"
                ]
            else:
                personal_additions = [
                    " I remember talking with you before! 😊",
                    " Nice to see you again! 🌸",
                    " Glad you're back! 💫"
                ]
            
            base_response = random.choice(response_list)
            if response_type in ["greeting", "how_are_you"]:
                base_response += random.choice(personal_additions)
            
            return base_response
        
        return random.choice(response_list)

    def respond(self, user_input: str) -> str:
        """Generate a response to user input"""
        self.conversation_count += 1
        
        # Detect language
        language = self.detect_language(user_input)
        
        # Get response type
        response_type = self.get_response_type(user_input, language)
        
        # Handle special cases
        if response_type == "time":
            return self.get_time_response(language)
        elif response_type == "date":
            return self.get_date_response(language)
        
        # Get personalized response
        response = self.get_personalized_response(response_type, language)
        
        # Save memory
        self.save_memory()
        
        return response

    def get_conversation_stats(self) -> str:
        """Get conversation statistics"""
        if self.conversation_count > 0:
            return f"📊 We've had {self.conversation_count} conversations together!"
        return "📊 This is our first conversation!"

def main():
    """Main function to run the AI agent"""
    print("=" * 60)
    print("🤖 نورهان AI Agent - Norhan's Interactive Assistant")
    print("=" * 60)
    print("Type your messages in Arabic or English!")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'stats' to see conversation statistics")
    print("=" * 60)
    
    agent = NorhanAI()
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
                
            # Handle special commands
            if user_input.lower() in ['exit', 'quit', 'وداعاً', 'مع السلامة']:
                print(f"\n🤖 {agent.name}: {agent.get_personalized_response('farewell', agent.detect_language(user_input))}")
                break
            elif user_input.lower() in ['stats', 'إحصائيات']:
                print(f"\n🤖 {agent.name}: {agent.get_conversation_stats()}")
                continue
            
            # Generate response
            response = agent.respond(user_input)
            print(f"\n🤖 {agent.name}: {response}")
            
        except KeyboardInterrupt:
            print(f"\n\n🤖 {agent.name}: {agent.get_personalized_response('farewell', 'english')}")
            break
        except Exception as e:
            print(f"\n🤖 {agent.name}: عذراً، حدث خطأ. Sorry, an error occurred. 😅")
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
