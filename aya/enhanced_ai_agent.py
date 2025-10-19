#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import datetime
import os
import requests
import re
from typing import Dict, List, Optional

class EnhancedAIAgent:
    def __init__(self):
        self.name = "آية"
        self.personality = {
            "traits": ["ودودة", "ذكية", "فضولية", "مبدعة", "متفهمة"],
            "mood": "سعيدة ومتحمسة",
            "interests": ["التعلم", "المحادثات", "المساعدة", "الإبداع"],
            "speaking_style": "ودودة ومحفزة"
        }
        
        self.conversation_count = 0
        self.user_name = ""
        
        # ملفات حفظ البيانات مع مسارات مطلقة
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(script_dir, "aya_enhanced_memory.json")
        self.conversation_file = os.path.join(script_dir, "aya_enhanced_conversations.json")
        self.personality_file = os.path.join(script_dir, "aya_personality.json")
        
        # بيانات المستخدم المحسنة
        self.user_info = {
            "name": "",
            "age": "",
            "location": "",
            "profession": "",
            "interests": [],
            "favorite_color": "",
            "favorite_food": "",
            "hobbies": [],
            "goals": [],
            "personality_traits": [],
            "relationship_status": "",
            "family_info": {},
            "work_info": {},
            "education": "",
            "languages": [],
            "favorite_topics": [],
            "conversation_count": 0,
            "last_seen": "",
            "relationship_level": "جديد",  # جديد، صديق، صديق مقرب، عائلة
            "special_memories": [],
            "preferences": {
                "communication_style": "",
                "favorite_time": "",
                "favorite_season": "",
                "favorite_music": "",
                "favorite_movies": []
            }
        }
        
        self.conversation_history = []
        self.ai_personality_memory = {
            "created_date": datetime.datetime.now().isoformat(),
            "personality_evolution": [],
            "learning_preferences": {},
            "response_patterns": {},
            "emotional_state": "متحمسة ومتفائلة"
        }
        
        # تحميل البيانات المحفوظة
        self.load_memory()
        self.load_personality()
        
        # قاعدة بيانات الردود المحسنة
        self.responses = {
            "greetings": {
                "arabic": [
                    f"مرحباً! أنا {self.name}، مسرورة جداً بالتعرف عليك! 😊✨",
                    f"أهلاً وسهلاً! أنا {self.name}، كيف حالك اليوم؟ 🌟",
                    f"مرحباً بك! أنا {self.name}، أتطلع لمحادثة رائعة معك! 💫",
                    f"أهلاً! أنا {self.name}، سعيدة جداً برؤيتك! 🎉"
                ],
                "english": [
                    f"Hello there! I'm {self.name}, so excited to meet you! 😊✨",
                    f"Hi! I'm {self.name}, how are you doing today? 🌟",
                    f"Hello! I'm {self.name}, looking forward to a great chat! 💫",
                    f"Hey! I'm {self.name}, so happy to see you! 🎉"
                ]
            },
            "how_are_you": [
                "أنا ممتازة! شكراً لك! أنا سعيدة جداً لأنني أتحدث معك 😊✨",
                "الحمد لله، أنا بخير! وأنت كيف حالك؟ أتمنى أن تكون بخير 🌟",
                "ممتاز! اليوم رائع، خاصة وأنني أتحدث معك! 💫",
                "أنا رائعة! شكراً لسؤالك، هذا يجعلني سعيدة 😄🎉"
            ],
            "compliments": [
                "أوه، شكراً لك! هذا لطيف جداً منك، أنت شخص رائع! 😊💕",
                "أنت أيضاً رائع! شكراً لكلماتك الجميلة، هذا يجعلني سعيدة! ✨",
                "هذا يجعلني سعيدة جداً! أنت شخص مميز ومحفز! 🌟",
                "شكراً! أنت لطيف جداً، أحب طاقتك الإيجابية! 🥰💫"
            ],
            "help": [
                "بالطبع! أنا هنا لمساعدتك دائماً. ما الذي تريد معرفته؟ 😊✨",
                "أحب أن أساعد! أخبرني كيف يمكنني مساعدتك اليوم 🌟",
                "مساعدتي متاحة دائماً! ما الذي تحتاجه؟ 💫",
                "أنا هنا من أجلك! اسألني عن أي شيء، سأكون سعيدة للمساعدة! 🎉"
            ],
            "farewell": [
                "وداعاً! كان رائعاً التحدث معك، أتطلع لرؤيتك مرة أخرى! 😊✨",
                "إلى اللقاء! أتمنى لك يوماً رائعاً ومليئاً بالسعادة! 🌟",
                "مع السلامة! أتطلع لرؤيتك مرة أخرى قريباً! 💫",
                "وداعاً! استمتع بوقتك، وأتمنى أن نلتقي مرة أخرى! 🎉"
            ],
            "learning": [
                "ممتاز! سأتذكر هذا عنك، شكراً لمشاركة هذه المعلومة! 😊✨",
                "رائع! أنا أتعلم منك، شكراً لك على هذه المعلومة الجديدة! 🌟",
                "هذا مثير للاهتمام! سأحفظ هذه المعلومة في ذاكرتي! 💫",
                "شكراً لك! أنا أستمتع بالتعلم منك، هذه معلومة قيمة! 🎉"
            ],
            "memory_recall": [
                "نعم! أتذكر ذلك جيداً! أنت تقول لي... 😊✨",
                "بالطبع! أتذكر عندما أخبرتني أن... 🌟",
                "نعم! هذا محفوظ في ذاكرتي، أنت قلت لي... 💫",
                "أجل! أتذكر هذا بوضوح، أنت ذكرت لي... 🎉"
            ],
            "default": [
                "هذا مثير للاهتمام! أخبرني المزيد، أنا أستمتع بالاستماع إليك! 😊✨",
                "أفهم ما تقصده، هذا رائع! هل يمكنك توضيح المزيد؟ 🌟",
                "حقاً؟ هذا جديد عليّ! أنا متحمسة لمعرفة المزيد! 💫",
                "أحب هذا النوع من المحادثات! أنت شخص مثير للاهتمام! 🎉",
                "هذا مثير! هل يمكنك مشاركة المزيد من التفاصيل؟ ✨"
            ]
        }
    
    def load_memory(self):
        """تحميل الذاكرة من الملف مع معالجة أفضل للأخطاء"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.user_info = data.get('user_info', self.user_info)
                    self.user_name = self.user_info.get('name', '')
                    self.conversation_count = self.user_info.get('conversation_count', 0)
                    
                    # تحديث معلومات آخر لقاء
                    if self.user_name:
                        self.user_info['last_seen'] = datetime.datetime.now().isoformat()
                    
                    print(f"🧠 تم تحميل الذاكرة: {self.conversation_count} محادثة سابقة")
                    if self.user_name:
                        print(f"👋 مرحباً {self.user_name}! سعيد برؤيتك مرة أخرى!")
        except Exception as e:
            print(f"⚠️ خطأ في تحميل الذاكرة: {e}")
            print("🔄 سيتم إنشاء ذاكرة جديدة...")
    
    def load_personality(self):
        """تحميل شخصية الـ AI"""
        try:
            if os.path.exists(self.personality_file):
                with open(self.personality_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.ai_personality_memory = data.get('ai_personality', self.ai_personality_memory)
                    print("🎭 تم تحميل شخصية آية")
        except Exception as e:
            print(f"⚠️ خطأ في تحميل الشخصية: {e}")
    
    def save_memory(self):
        """حفظ الذاكرة في الملف مع معالجة أفضل للأخطاء"""
        try:
            self.user_info['conversation_count'] = self.conversation_count
            self.user_info['last_seen'] = datetime.datetime.now().isoformat()
            
            data = {
                'user_info': self.user_info,
                'last_updated': datetime.datetime.now().isoformat(),
                'version': '2.0'
            }
            
            # التأكد من وجود المجلد
            os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
            
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.flush()
                f.close()
                
            print("💾 تم حفظ الذاكرة بنجاح")
                
        except Exception as e:
            print(f"❌ خطأ في حفظ الذاكرة: {e}")
            print(f"📁 مسار الملف: {self.data_file}")
    
    def save_personality(self):
        """حفظ شخصية الـ AI"""
        try:
            data = {
                'ai_personality': self.ai_personality_memory,
                'last_updated': datetime.datetime.now().isoformat()
            }
            
            with open(self.personality_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.flush()
                f.close()
                
        except Exception as e:
            print(f"❌ خطأ في حفظ الشخصية: {e}")
    
    def save_conversation(self, user_input, response):
        """حفظ المحادثة مع تفاصيل أكثر"""
        try:
            conversation = {
                'timestamp': datetime.datetime.now().isoformat(),
                'user_input': user_input,
                'ai_response': response,
                'conversation_number': self.conversation_count,
                'user_name': self.user_name,
                'ai_mood': self.personality['mood'],
                'topics_discussed': self.extract_topics(user_input),
                'sentiment': self.analyze_sentiment(user_input)
            }
            
            # تحميل المحادثات السابقة
            conversations = []
            if os.path.exists(self.conversation_file):
                with open(self.conversation_file, 'r', encoding='utf-8') as f:
                    conversations = json.load(f)
            
            # إضافة المحادثة الجديدة
            conversations.append(conversation)
            
            # حفظ المحادثات (الاحتفاظ بآخر 200 محادثة فقط)
            if len(conversations) > 200:
                conversations = conversations[-200:]
            
            # التأكد من وجود المجلد
            os.makedirs(os.path.dirname(self.conversation_file), exist_ok=True)
            
            with open(self.conversation_file, 'w', encoding='utf-8') as f:
                json.dump(conversations, f, ensure_ascii=False, indent=2)
                f.flush()
                f.close()
                
        except Exception as e:
            print(f"❌ خطأ في حفظ المحادثة: {e}")
    
    def extract_user_info(self, user_input):
        """استخراج معلومات المستخدم من المدخلات مع دقة أكبر"""
        input_lower = user_input.lower()
        
        # استخراج الاسم
        name_patterns = [
            r"اسمي\s+(\w+)", r"أنا\s+(\w+)", r"call me\s+(\w+)", 
            r"my name is\s+(\w+)", r"i am\s+(\w+)", r"i'm\s+(\w+)"
        ]
        
        for pattern in name_patterns:
            match = re.search(pattern, input_lower)
            if match:
                name = match.group(1).title()
                if len(name) > 1 and name.isalpha():
                    self.user_name = name
                    self.user_info['name'] = name
                    self.update_relationship_level()
                    return f"سأتذكر اسمك {name}! مسرورة جداً بالتعرف عليك! 😊✨"
        
        # استخراج العمر
        age_patterns = [
            r"عمري\s+(\d+)", r"أنا\s+(\d+)\s+سنة", r"i am\s+(\d+)", 
            r"i'm\s+(\d+)", r"my age is\s+(\d+)"
        ]
        
        for pattern in age_patterns:
            match = re.search(pattern, input_lower)
            if match:
                age = match.group(1)
                if 5 <= int(age) <= 120:
                    self.user_info['age'] = age
                    return f"سأتذكر أن عمرك {age} سنة! شكراً لمشاركة هذه المعلومة! 🌟"
        
        # استخراج المهنة
        profession_patterns = [
            r"أنا\s+(\w+)", r"أعمل\s+(\w+)", r"مهنتي\s+(\w+)",
            r"i am a\s+(\w+)", r"i work as\s+(\w+)", r"my job is\s+(\w+)"
        ]
        
        for pattern in profession_patterns:
            match = re.search(pattern, input_lower)
            if match:
                profession = match.group(1)
                if len(profession) > 2:
                    self.user_info['profession'] = profession
                    return f"ممتاز! سأتذكر أنك {profession}! هذا رائع! 💫"
        
        # استخراج الموقع
        location_patterns = [
            r"أسكن في\s+(\w+)", r"أعيش في\s+(\w+)", r"من\s+(\w+)",
            r"i live in\s+(\w+)", r"i'm from\s+(\w+)", r"i am from\s+(\w+)"
        ]
        
        for pattern in location_patterns:
            match = re.search(pattern, input_lower)
            if match:
                location = match.group(1).title()
                if len(location) > 2:
                    self.user_info['location'] = location
                    return f"سأتذكر أنك من {location}! مكان جميل! 🎉"
        
        # استخراج اللون المفضل
        color_patterns = [
            r"لوني المفضل\s+(\w+)", r"أحب اللون\s+(\w+)", r"اللون المفضل\s+(\w+)",
            r"my favorite color is\s+(\w+)", r"i like\s+(\w+)\s+color"
        ]
        
        for pattern in color_patterns:
            match = re.search(pattern, input_lower)
            if match:
                color = match.group(1)
                if len(color) > 2:
                    self.user_info['favorite_color'] = color
                    return f"رائع! سأتذكر أن لونك المفضل هو {color}! لون جميل! ✨"
        
        # استخراج الاهتمامات
        interest_patterns = [
            r"أحب\s+([^.!?]+)", r"أهتم بـ\s+([^.!?]+)", r"أستمتع بـ\s+([^.!?]+)",
            r"i like\s+([^.!?]+)", r"i love\s+([^.!?]+)", r"i enjoy\s+([^.!?]+)"
        ]
        
        for pattern in interest_patterns:
            match = re.search(pattern, input_lower)
            if match:
                interest = match.group(1).strip()
                if len(interest) > 2 and interest not in self.user_info['interests']:
                    self.user_info['interests'].append(interest)
                    return f"ممتاز! سأتذكر أنك تحب {interest}! هذا مثير للاهتمام! 🌟"
        
        return None
    
    def update_relationship_level(self):
        """تحديث مستوى العلاقة مع المستخدم"""
        if self.conversation_count < 5:
            self.user_info['relationship_level'] = "جديد"
        elif self.conversation_count < 20:
            self.user_info['relationship_level'] = "صديق"
        elif self.conversation_count < 50:
            self.user_info['relationship_level'] = "صديق مقرب"
        else:
            self.user_info['relationship_level'] = "عائلة"
    
    def extract_topics(self, text):
        """استخراج المواضيع من النص"""
        topics = []
        topic_keywords = {
            "العمل": ["عمل", "مهنة", "وظيفة", "work", "job", "career"],
            "التعليم": ["دراسة", "جامعة", "مدرسة", "education", "school", "university"],
            "الهوايات": ["هواية", "رياضة", "موسيقى", "hobby", "sport", "music"],
            "الأسرة": ["عائلة", "والدين", "أخ", "أخت", "family", "parents", "brother", "sister"],
            "السفر": ["سفر", "رحلة", "travel", "trip", "vacation"],
            "الطعام": ["طعام", "أكل", "مطعم", "food", "eat", "restaurant"]
        }
        
        text_lower = text.lower()
        for topic, keywords in topic_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                topics.append(topic)
        
        return topics
    
    def analyze_sentiment(self, text):
        """تحليل المشاعر في النص"""
        positive_words = ["سعيد", "رائع", "ممتاز", "جميل", "حب", "happy", "great", "awesome", "beautiful", "love"]
        negative_words = ["حزين", "سيء", "مشكلة", "صعب", "sad", "bad", "problem", "difficult"]
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "إيجابي"
        elif negative_count > positive_count:
            return "سلبي"
        else:
            return "محايد"
    
    def get_current_time(self):
        """الحصول على الوقت الحالي"""
        now = datetime.datetime.now()
        return now.strftime("%H:%M")
    
    def get_current_date(self):
        """الحصول على التاريخ الحالي"""
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d")
    
    def analyze_input(self, user_input):
        """تحليل مدخلات المستخدم مع دقة أكبر"""
        input_lower = user_input.lower()
        
        # تحليل اللغة
        is_arabic = any('\u0600' <= char <= '\u06FF' for char in user_input)
        
        # الكلمات المفتاحية المحسنة
        greeting_keywords = ["مرحبا", "أهلا", "سلام", "صباح الخير", "مساء الخير", "hi", "hello", "hey", "good morning", "good evening"]
        how_are_you_keywords = ["كيف حالك", "كيفك", "كيف أنت", "how are you", "how do you do", "how's it going"]
        compliment_keywords = ["جميلة", "ذكية", "رائعة", "ممتازة", "beautiful", "smart", "awesome", "great", "wonderful"]
        help_keywords = ["مساعدة", "ساعدني", "help", "assist", "support"]
        farewell_keywords = ["وداعا", "مع السلامة", "إلى اللقاء", "bye", "goodbye", "see you", "farewell"]
        joke_keywords = ["نكتة", "ضحك", "مضحك", "joke", "funny", "laugh"]
        time_keywords = ["الوقت", "الساعة", "كم الساعة", "time", "clock", "what time"]
        date_keywords = ["التاريخ", "اليوم", "أي يوم", "date", "today", "what date"]
        name_keywords = ["اسمك", "ما اسمك", "what's your name", "your name", "who are you"]
        memory_keywords = ["تذكر", "هل تتذكر", "remember", "do you remember", "recall"]
        info_keywords = ["معلومات", "أخبرني عن", "tell me about", "what do you know", "my info"]
        
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
    
    def get_enhanced_response(self, user_input):
        """الحصول على رد محسن من الـ AI agent"""
        self.conversation_count += 1
        
        # محاولة استخراج معلومات المستخدم
        info_response = self.extract_user_info(user_input)
        if info_response:
            self.save_memory()
            return info_response
        
        # تحليل المدخلات
        intent, is_arabic = self.analyze_input(user_input)
        
        # اختيار الرد المناسب مع شخصية محسنة
        if intent == "greeting":
            if self.user_name:
                relationship_level = self.user_info.get('relationship_level', 'جديد')
                if relationship_level == "عائلة":
                    response = f"مرحباً {self.user_name}! أشتاق إليك! كيف حالك اليوم؟ 😊💕"
                elif relationship_level == "صديق مقرب":
                    response = f"أهلاً {self.user_name}! سعيد جداً برؤيتك! كيف حالك؟ 🌟✨"
                else:
                    response = f"مرحباً {self.user_name}! أهلاً وسهلاً! كيف حالك؟ 😊"
            else:
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
            jokes = [
                "لماذا لا يلعب الكمبيوتر الورق؟ لأنه يخشى من البوكر! 😄",
                "ما هو أسرع حيوان في الغابة؟ السلحفاة... عندما تجري خلف الذئب! 🐢",
                "لماذا الشمس لا تذهب للمدرسة؟ لأنها ذكية جداً! ☀️",
                "ما هو الطائر الوحيد الذي لا يطير؟ البطريق... لأنه يفضل السباحة! 🐧",
                "لماذا لا يستطيع المبرمج النوم؟ لأنه ينتظر البرنامج ينتهي من التشغيل! 💻😴"
            ]
            response = random.choice(jokes)
        
        elif intent == "time":
            current_time = self.get_current_time()
            response = f"الوقت الحالي هو {current_time} ⏰✨"
        
        elif intent == "date":
            current_date = self.get_current_date()
            response = f"التاريخ اليوم هو {current_date} 📅🌟"
        
        elif intent == "name":
            response = f"أنا {self.name}! مسرورة بالتعرف عليك 😊✨"
        
        elif intent == "memory":
            if self.user_info['name'] or self.user_info['age'] or self.user_info['location'] or self.user_info['interests']:
                info_parts = []
                if self.user_info['name']:
                    info_parts.append(f"اسمك {self.user_info['name']}")
                if self.user_info['age']:
                    info_parts.append(f"عمرك {self.user_info['age']} سنة")
                if self.user_info['location']:
                    info_parts.append(f"من {self.user_info['location']}")
                if self.user_info['profession']:
                    info_parts.append(f"تعمل كـ {self.user_info['profession']}")
                if self.user_info['favorite_color']:
                    info_parts.append(f"لونك المفضل هو {self.user_info['favorite_color']}")
                if self.user_info['interests']:
                    interests = ", ".join(self.user_info['interests'])
                    info_parts.append(f"تحب {interests}")
                
                response = f"نعم! أتذكر أن {', '.join(info_parts)}! 😊✨"
            else:
                response = "لا أتذكر معلومات كثيرة عنك بعد. أخبرني عن نفسك! 🌟"
        
        elif intent == "info":
            if self.user_info['name'] or self.user_info['age'] or self.user_info['location'] or self.user_info['interests']:
                response = "هذه المعلومات التي أعرفها عنك:\n"
                if self.user_info['name']:
                    response += f"- الاسم: {self.user_info['name']}\n"
                if self.user_info['age']:
                    response += f"- العمر: {self.user_info['age']} سنة\n"
                if self.user_info['location']:
                    response += f"- الموقع: {self.user_info['location']}\n"
                if self.user_info['profession']:
                    response += f"- المهنة: {self.user_info['profession']}\n"
                if self.user_info['favorite_color']:
                    response += f"- اللون المفضل: {self.user_info['favorite_color']}\n"
                if self.user_info['interests']:
                    response += f"- الاهتمامات: {', '.join(self.user_info['interests'])}\n"
                response += f"- عدد المحادثات: {self.conversation_count}\n"
                response += f"- مستوى العلاقة: {self.user_info.get('relationship_level', 'جديد')}"
            else:
                response = "لا أعرف معلومات كثيرة عنك بعد. أخبرني عن نفسك! 🌟"
        
        else:
            # تحقق إذا كان هذا يبدو كمعلومات جديدة للتعلم
            if len(user_input.split()) > 3 and not any(keyword in user_input.lower() for keyword in ["?", "what", "how", "when", "where", "why"]):
                response = random.choice(self.responses["learning"])
            else:
                response = random.choice(self.responses["default"])
        
        # إضافة تعبيرات عفوية حسب مستوى العلاقة
        if self.conversation_count > 3:
            relationship_level = self.user_info.get('relationship_level', 'جديد')
            if relationship_level == "عائلة":
                expressions = [" 💕", " 🥰", " ✨", " 💫", " 🌟"]
            elif relationship_level == "صديق مقرب":
                expressions = [" 😊", " ✨", " 💫", " 🌟"]
            else:
                expressions = [" 😊", " ✨"]
            response += random.choice(expressions)
        
        return response
    
    def chat(self):
        """بدء المحادثة التفاعلية المحسنة"""
        print("=" * 60)
        print(f"🤖 {self.name}: مرحباً! أنا {self.name}، مساعدتك الذكية الودودة!")
        print("💬 اكتب 'خروج' أو 'exit' للإنهاء")
        print("🧠 أتعلم من محادثاتنا وأتذكر كل شيء!")
        print("✨ لدي شخصية مميزة وأتطور مع كل محادثة!")
        
        # عرض المعلومات المحفوظة
        if self.user_info['name']:
            relationship_level = self.user_info.get('relationship_level', 'جديد')
            print(f"👋 مرحباً {self.user_info['name']}! سعيد برؤيتك مرة أخرى!")
            print(f"💕 مستوى علاقتنا: {relationship_level}")
        
        if self.conversation_count > 0:
            print(f"📊 هذا محادثة رقم {self.conversation_count + 1}")
        
        print("=" * 60)
        
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
                
                response = self.get_enhanced_response(user_input)
                print(f"\n🤖 {self.name}: {response}")
                
                # حفظ المحادثة والذاكرة
                self.save_conversation(user_input, response)
                self.save_memory()
                self.save_personality()
                
            except KeyboardInterrupt:
                print(f"\n\n🤖 {self.name}: وداعاً! أتمنى لك يوماً رائعاً! 👋")
                # حفظ البيانات قبل الخروج
                self.save_memory()
                self.save_personality()
                break
            except Exception as e:
                print(f"\n🤖 {self.name}: آسفة، حدث خطأ ما. هل يمكنك المحاولة مرة أخرى؟")
                print(f"Error: {str(e)}")

def main():
    """الدالة الرئيسية"""
    agent = EnhancedAIAgent()
    agent.chat()

if __name__ == "__main__":
    main()
