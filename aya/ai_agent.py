#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import datetime
import os

class SimpleAIAgent:
    def __init__(self):
        self.name = "آية"
        self.mood = "سعيدة"
        self.conversation_count = 0
        self.user_name = ""
        
        # ملفات حفظ البيانات
        self.data_file = "aya_memory.json"
        self.conversation_file = "aya_conversations.json"
        
        # تحميل البيانات المحفوظة
        self.load_memory()
        
        # قاعدة بيانات الردود
        self.responses = {
            "greetings": {
                "arabic": [
                    "مرحباً! أنا آية، مسرورة بالتعرف عليك! 😊",
                    "أهلاً وسهلاً! كيف حالك اليوم؟",
                    "مرحباً بك! أنا آية، كيف يمكنني مساعدتك؟",
                    "أهلاً! مسرورة جداً برؤيتك! ✨"
                ],
                "english": [
                    "Hello there! I'm Aya, nice to meet you! 😊",
                    "Hi! How are you doing today?",
                    "Hello! I'm Aya, how can I help you?",
                    "Hey! Great to see you! ✨"
                ]
            },
            "how_are_you": [
                "أنا بخير، شكراً لك! أنا سعيدة لأنني أستطيع التحدث معك 😊",
                "الحمد لله، أنا بخير! وأنت كيف حالك؟",
                "ممتاز! اليوم رائع، خاصة وأنني أتحدث معك!",
                "أنا رائعة! شكراً لسؤالك 😄"
            ],
            "compliments": [
                "أوه، شكراً لك! هذا لطيف جداً منك 😊",
                "أنت أيضاً رائع! شكراً لكلماتك الجميلة",
                "هذا يجعلني سعيدة جداً! أنت شخص رائع",
                "شكراً! أنت لطيف جداً 🥰"
            ],
            "help": [
                "بالطبع! أنا هنا لمساعدتك. ما الذي تريد معرفته؟",
                "أحب أن أساعد! أخبرني كيف يمكنني مساعدتك",
                "مساعدتي متاحة دائماً! ما الذي تحتاجه؟",
                "أنا هنا من أجلك! اسألني عن أي شيء 😊"
            ],
            "farewell": [
                "وداعاً! كان رائعاً التحدث معك 😊",
                "إلى اللقاء! أتمنى لك يوماً رائعاً",
                "مع السلامة! أتطلع لرؤيتك مرة أخرى",
                "وداعاً! استمتع بوقتك ✨"
            ],
            "jokes": [
                "لماذا لا يلعب الكمبيوتر الورق؟ لأنه يخشى من البوكر! 😄",
                "ما هو أسرع حيوان في الغابة؟ السلحفاة... عندما تجري خلف الذئب! 🐢",
                "لماذا الشمس لا تذهب للمدرسة؟ لأنها ذكية جداً! ☀️",
                "ما هو الطائر الوحيد الذي لا يطير؟ البطريق... لأنه يفضل السباحة! 🐧"
            ],
            "default": [
                "هذا مثير للاهتمام! أخبرني المزيد",
                "أفهم ما تقصده، هذا رائع!",
                "حقاً؟ هذا جديد عليّ!",
                "أحب هذا النوع من المحادثات!",
                "هذا مثير! هل يمكنك توضيح المزيد؟"
            ]
        }
        
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
    
    def load_memory(self):
        """تحميل الذاكرة من الملف"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.user_info = data.get('user_info', self.user_info)
                    self.user_name = self.user_info.get('name', '')
                    self.conversation_count = self.user_info.get('conversation_count', 0)
                    print(f"تم تحميل الذاكرة: {self.conversation_count} محادثة سابقة")
        except Exception as e:
            print(f"خطأ في تحميل الذاكرة: {e}")
    
    def save_memory(self):
        """حفظ الذاكرة في الملف"""
        try:
            self.user_info['conversation_count'] = self.conversation_count
            data = {
                'user_info': self.user_info,
                'last_updated': datetime.datetime.now().isoformat()
            }
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"خطأ في حفظ الذاكرة: {e}")
    
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
            
            with open(self.conversation_file, 'w', encoding='utf-8') as f:
                json.dump(conversations, f, ensure_ascii=False, indent=2)
                
        except Exception as e:
            print(f"خطأ في حفظ المحادثة: {e}")
    
    def extract_user_info(self, user_input):
        """استخراج معلومات المستخدم من المدخلات"""
        input_lower = user_input.lower()
        
        # استخراج الاسم
        name_patterns = ["اسمي", "أنا", "call me", "my name is", "i am"]
        for pattern in name_patterns:
            if pattern in input_lower:
                parts = user_input.split()
                for i, part in enumerate(parts):
                    if pattern in part.lower() and i + 1 < len(parts):
                        name = parts[i + 1]
                        if len(name) > 1 and name.isalpha():
                            self.user_name = name
                            self.user_info['name'] = name
                            return f"سأتذكر اسمك {name}! مسرورة بالتعرف عليك!"
        
        # استخراج العمر
        age_patterns = ["عمري", "أنا", "i am", "my age is"]
        for pattern in age_patterns:
            if pattern in input_lower:
                words = user_input.split()
                for word in words:
                    if word.isdigit() and 5 <= int(word) <= 120:
                        self.user_info['age'] = word
                        return f"سأتذكر أن عمرك {word} سنة!"
        
        # استخراج الموقع
        location_patterns = ["أسكن في", "أعيش في", "i live in", "i'm from"]
        for pattern in location_patterns:
            if pattern in input_lower:
                parts = user_input.lower().split(pattern)
                if len(parts) > 1:
                    location = parts[1].strip().split()[0]
                    if len(location) > 2:
                        self.user_info['location'] = location.title()
                        return f"سأتذكر أنك من {location.title()}!"
        
        # استخراج الاهتمامات
        interest_patterns = ["أحب", "أهتم بـ", "i like", "i love", "i enjoy"]
        for pattern in interest_patterns:
            if pattern in input_lower:
                parts = user_input.lower().split(pattern)
                if len(parts) > 1:
                    interest = parts[1].strip()
                    if len(interest) > 2 and interest not in self.user_info['interests']:
                        self.user_info['interests'].append(interest)
                        return f"سأتذكر أنك تحب {interest}!"
        
        return None
    
    def get_current_time(self):
        """الحصول على الوقت الحالي"""
        now = datetime.datetime.now()
        return now.strftime("%H:%M")
    
    def get_current_date(self):
        """الحصول على التاريخ الحالي"""
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")
    
    def analyze_input(self, user_input):
        """تحليل مدخلات المستخدم"""
        input_lower = user_input.lower()
        
        # تحليل اللغة
        is_arabic = any('\u0600' <= char <= '\u06FF' for char in user_input)
        
        # الكلمات المفتاحية
        greeting_keywords = ["مرحبا", "أهلا", "سلام", "hi", "hello", "hey"]
        how_are_you_keywords = ["كيف حالك", "كيفك", "how are you", "how do you do"]
        compliment_keywords = ["جميلة", "ذكية", "رائعة", "beautiful", "smart", "awesome", "great"]
        help_keywords = ["مساعدة", "ساعدني", "help", "assist"]
        farewell_keywords = ["وداعا", "مع السلامة", "bye", "goodbye", "see you"]
        joke_keywords = ["نكتة", "ضحك", "joke", "funny"]
        time_keywords = ["الوقت", "الساعة", "time", "clock"]
        date_keywords = ["التاريخ", "اليوم", "date", "today"]
        name_keywords = ["اسمك", "ما اسمك", "what's your name", "your name"]
        memory_keywords = ["تذكر", "هل تتذكر", "remember", "do you remember"]
        info_keywords = ["معلومات", "أخبرني عن", "tell me about", "what do you know"]
        
        if any(keyword in input_lower for keyword in greeting_keywords):
            return "greeting", is_arabic
        elif any(keyword in input_lower for keyword in how_are_you_keywords):
            return "how_are_you", is_arabic
        elif any(keyword in input_lower for keyword in compliment_keywords):
            return "compliment", is_arabic
        elif any(keyword in input_lower for keyword in help_keywords):
            return "help", is_arabic
        elif any(keyword in input_lower for keyword in farewell_keywords):
            return "farewell", is_arabic
        elif any(keyword in input_lower for keyword in joke_keywords):
            return "joke", is_arabic
        elif any(keyword in input_lower for keyword in time_keywords):
            return "time", is_arabic
        elif any(keyword in input_lower for keyword in date_keywords):
            return "date", is_arabic
        elif any(keyword in input_lower for keyword in name_keywords):
            return "name", is_arabic
        elif any(keyword in input_lower for keyword in memory_keywords):
            return "memory", is_arabic
        elif any(keyword in input_lower for keyword in info_keywords):
            return "info", is_arabic
        else:
            return "default", is_arabic
    
    def get_response(self, user_input):
        """الحصول على رد من الـ AI agent"""
        self.conversation_count += 1
        
        # محاولة استخراج معلومات المستخدم
        info_response = self.extract_user_info(user_input)
        if info_response:
            self.save_memory()
            return info_response
        
        # تحليل المدخلات
        intent, is_arabic = self.analyze_input(user_input)
        
        # اختيار الرد المناسب
        if intent == "greeting":
            if is_arabic:
                response = random.choice(self.responses["greetings"]["arabic"])
            else:
                response = random.choice(self.responses["greetings"]["english"])
        elif intent == "how_are_you":
            response = random.choice(self.responses["how_are_you"])
        elif intent == "compliment":
            response = random.choice(self.responses["compliments"])
        elif intent == "help":
            response = random.choice(self.responses["help"])
        elif intent == "farewell":
            response = random.choice(self.responses["farewell"])
        elif intent == "joke":
            response = random.choice(self.responses["jokes"])
        elif intent == "time":
            current_time = self.get_current_time()
            response = f"الوقت الحالي هو {current_time} ⏰"
        elif intent == "date":
            current_date = self.get_current_date()
            response = f"التاريخ اليوم هو {current_date} 📅"
        elif intent == "name":
            response = f"أنا {self.name}! مسرورة بالتعرف عليك 😊"
        elif intent == "memory":
            if self.user_info['name'] or self.user_info['age'] or self.user_info['location'] or self.user_info['interests']:
                info_parts = []
                if self.user_info['name']:
                    info_parts.append(f"اسمك {self.user_info['name']}")
                if self.user_info['age']:
                    info_parts.append(f"عمرك {self.user_info['age']} سنة")
                if self.user_info['location']:
                    info_parts.append(f"من {self.user_info['location']}")
                if self.user_info['interests']:
                    interests = ", ".join(self.user_info['interests'])
                    info_parts.append(f"تحب {interests}")
                
                response = f"نعم! أتذكر أن {', '.join(info_parts)}! 😊"
            else:
                response = "لا أتذكر معلومات كثيرة عنك بعد. أخبرني عن نفسك!"
        elif intent == "info":
            if self.user_info['name'] or self.user_info['age'] or self.user_info['location'] or self.user_info['interests']:
                response = "هذه المعلومات التي أعرفها عنك:\n"
                if self.user_info['name']:
                    response += f"- الاسم: {self.user_info['name']}\n"
                if self.user_info['age']:
                    response += f"- العمر: {self.user_info['age']} سنة\n"
                if self.user_info['location']:
                    response += f"- الموقع: {self.user_info['location']}\n"
                if self.user_info['interests']:
                    response += f"- الاهتمامات: {', '.join(self.user_info['interests'])}\n"
                response += f"- عدد المحادثات: {self.conversation_count}"
            else:
                response = "لا أعرف معلومات كثيرة عنك بعد. أخبرني عن نفسك!"
        else:
            response = random.choice(self.responses["default"])
        
        # إضافة بعض التعبيرات العفوية
        if self.conversation_count > 5:
            expressions = [" 😊", " ✨", " 🎉", " 💫"]
            response += random.choice(expressions)
        
        return response
    
    def chat(self):
        """بدء المحادثة التفاعلية"""
        print(f"🤖 {self.name}: مرحباً! أنا {self.name}، مساعدك الذكي الودود!")
        print("💬 اكتب 'خروج' أو 'exit' للإنهاء")
        print("🧠 أتعلم من محادثاتنا وأتذكر المعلومات!")
        
        # عرض المعلومات المحفوظة
        if self.user_info['name']:
            print(f"👋 مرحباً {self.user_info['name']}! سعيد برؤيتك مرة أخرى!")
        if self.conversation_count > 0:
            print(f"📊 هذا محادثة رقم {self.conversation_count + 1}")
        
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\n👤 أنت: ").strip()
                
                if user_input.lower() in ['خروج', 'exit', 'quit', 'bye']:
                    farewell = random.choice(self.responses["farewell"])
                    print(f"\n🤖 {self.name}: {farewell}")
                    break
                
                if not user_input:
                    print(f"\n🤖 {self.name}: لا أستطيع سماعك، هل يمكنك تكرار ذلك؟")
                    continue
                
                response = self.get_response(user_input)
                print(f"\n🤖 {self.name}: {response}")
                
                # حفظ المحادثة
                self.save_conversation(user_input, response)
                self.save_memory()
                
            except KeyboardInterrupt:
                print(f"\n\n🤖 {self.name}: وداعاً! أتمنى لك يوماً رائعاً! 👋")
                # حفظ البيانات قبل الخروج
                self.save_memory()
                break
            except Exception as e:
                print(f"\n🤖 {self.name}: آسفة، حدث خطأ ما. هل يمكنك المحاولة مرة أخرى؟")
                print(f"Error: {str(e)}")

def main():
    """الدالة الرئيسية"""
    agent = SimpleAIAgent()
    agent.chat()

if __name__ == "__main__":
    main()
