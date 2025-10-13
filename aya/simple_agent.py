#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import datetime

class SimpleAIAgent:
    def __init__(self):
        self.name = "آية"
        self.conversation_count = 0
        
        # قاعدة بيانات الردود
        self.responses = {
            "greetings": {
                "arabic": [
                    "مرحبا! أنا آية، مسرورة بالتعرف عليك!",
                    "أهلا وسهلا! كيف حالك اليوم؟",
                    "مرحبا بك! أنا آية، كيف يمكنني مساعدتك؟",
                    "أهلا! مسرورة جدا برؤيتك!"
                ],
                "english": [
                    "Hello there! I'm Aya, nice to meet you!",
                    "Hi! How are you doing today?",
                    "Hello! I'm Aya, how can I help you?",
                    "Hey! Great to see you!"
                ]
            },
            "how_are_you": [
                "أنا بخير، شكرا لك! أنا سعيدة لأنني أستطيع التحدث معك",
                "الحمد لله، أنا بخير! وأنت كيف حالك؟",
                "ممتاز! اليوم رائع، خاصة وأنني أتحدث معك!",
                "أنا رائعة! شكرا لسؤالك"
            ],
            "help": [
                "بالطبع! أنا هنا لمساعدتك. ما الذي تريد معرفته؟",
                "أحب أن أساعد! أخبرني كيف يمكنني مساعدتك",
                "مساعدتي متاحة دائما! ما الذي تحتاجه؟",
                "أنا هنا من أجلك! اسألني عن أي شيء"
            ],
            "farewell": [
                "وداعا! كان رائعا التحدث معك",
                "إلى اللقاء! أتمنى لك يوما رائعا",
                "مع السلامة! أتطلع لرؤيتك مرة أخرى",
                "وداعا! استمتع بوقتك"
            ],
            "jokes": [
                "لماذا لا يلعب الكمبيوتر الورق؟ لأنه يخشى من البوكر!",
                "ما هو أسرع حيوان في الغابة؟ السلحفاة... عندما تجري خلف الذئب!",
                "لماذا الشمس لا تذهب للمدرسة؟ لأنها ذكية جدا!",
                "ما هو الطائر الوحيد الذي لا يطير؟ البطريق... لأنه يفضل السباحة!"
            ],
            "default": [
                "هذا مثير للاهتمام! أخبرني المزيد",
                "أفهم ما تقصده، هذا رائع!",
                "حقا؟ هذا جديد علي!",
                "أحب هذا النوع من المحادثات!",
                "هذا مثير! هل يمكنك توضيح المزيد؟"
            ]
        }
    
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
        help_keywords = ["مساعدة", "ساعدني", "help", "assist"]
        farewell_keywords = ["وداعا", "مع السلامة", "bye", "goodbye", "see you"]
        joke_keywords = ["نكتة", "ضحك", "joke", "funny"]
        time_keywords = ["الوقت", "الساعة", "time", "clock"]
        date_keywords = ["التاريخ", "اليوم", "date", "today"]
        name_keywords = ["اسمك", "ما اسمك", "what's your name", "your name"]
        
        if any(keyword in input_lower for keyword in greeting_keywords):
            return "greeting", is_arabic
        elif any(keyword in input_lower for keyword in how_are_you_keywords):
            return "how_are_you", is_arabic
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
        else:
            return "default", is_arabic
    
    def get_response(self, user_input):
        """الحصول على رد من الـ AI agent"""
        self.conversation_count += 1
        
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
        elif intent == "help":
            response = random.choice(self.responses["help"])
        elif intent == "farewell":
            response = random.choice(self.responses["farewell"])
        elif intent == "joke":
            response = random.choice(self.responses["jokes"])
        elif intent == "time":
            current_time = self.get_current_time()
            response = f"الوقت الحالي هو {current_time}"
        elif intent == "date":
            current_date = self.get_current_date()
            response = f"التاريخ اليوم هو {current_date}"
        elif intent == "name":
            response = f"أنا {self.name}! مسرورة بالتعرف عليك"
        else:
            response = random.choice(self.responses["default"])
        
        return response
    
    def chat(self):
        """بدء المحادثة التفاعلية"""
        print(f"AI Agent: مرحبا! أنا {self.name}، مساعدك الذكي الودود!")
        print("اكتب 'خروج' أو 'exit' للإنهاء")
        print("=" * 50)
        
        while True:
            try:
                user_input = input("\nأنت: ").strip()
                
                if user_input.lower() in ['خروج', 'exit', 'quit', 'bye']:
                    farewell = random.choice(self.responses["farewell"])
                    print(f"\n{self.name}: {farewell}")
                    break
                
                if not user_input:
                    print(f"\n{self.name}: لا أستطيع سماعك، هل يمكنك تكرار ذلك؟")
                    continue
                
                response = self.get_response(user_input)
                print(f"\n{self.name}: {response}")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: وداعا! أتمنى لك يوما رائعا!")
                break
            except Exception as e:
                print(f"\n{self.name}: آسفة، حدث خطأ ما. هل يمكنك المحاولة مرة أخرى؟")

def main():
    """الدالة الرئيسية"""
    agent = SimpleAIAgent()
    agent.chat()

if __name__ == "__main__":
    main()
