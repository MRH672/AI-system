#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import json
import datetime
import os
import re

class EnhancedLearningAIAgent:
    def __init__(self):
        self.name = "Aya"
        self.conversation_count = 0
        self.user_name = ""
        
        # ملفات حفظ البيانات مع مسارات مطلقة
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_file = os.path.join(script_dir, "aya_enhanced_memory.json")
        self.conversation_file = os.path.join(script_dir, "aya_enhanced_conversations.json")
        self.personality_file = os.path.join(script_dir, "aya_enhanced_personality.json")
        
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
            "relationship_level": "new",  # new, friend, close_friend, family
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
            "emotional_state": "excited and optimistic"
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
                "I'm excellent! Thank you! I'm so happy to be talking with you 😊✨",
                "I'm wonderful! How are you doing? I hope you're doing great 🌟",
                "Excellent! Today is amazing, especially since I'm talking with you! 💫",
                "I'm fantastic! Thanks for asking, this makes me happy 😄🎉"
            ],
            "compliments": [
                "Oh, thank you! That's so kind of you, you're wonderful! 😊💕",
                "You're wonderful too! Thanks for your beautiful words, this makes me happy! ✨",
                "This makes me so happy! You're a special and inspiring person! 🌟",
                "Thank you! You're very kind, I love your positive energy! 🥰💫"
            ],
            "help": [
                "Of course! I'm always here to help you. What would you like to know? 😊✨",
                "I love to help! Tell me how I can assist you today 🌟",
                "My help is always available! What do you need? 💫",
                "I'm here for you! Ask me anything, I'll be happy to help! 🎉"
            ],
            "farewell": [
                "Goodbye! It was wonderful talking with you, I look forward to seeing you again! 😊✨",
                "See you later! I hope you have a wonderful day full of happiness! 🌟",
                "Take care! I look forward to seeing you again soon! 💫",
                "Goodbye! Enjoy your time, and I hope we meet again! 🎉"
            ],
            "learning": [
                "Excellent! I'll remember this about you, thanks for sharing this information! 😊✨",
                "Great! I'm learning from you, thank you for this new information! 🌟",
                "This is interesting! I'll save this information in my memory! 💫",
                "Thank you! I enjoy learning from you, this is valuable information! 🎉"
            ],
            "memory_recall": [
                "Yes! I remember that well! You told me... 😊✨",
                "Of course! I remember when you told me that... 🌟",
                "Yes! This is saved in my memory, you said... 💫",
                "Yes! I remember this clearly, you mentioned... 🎉"
            ],
            "default": [
                "That's interesting! Tell me more, I enjoy listening to you! 😊✨",
                "I understand what you mean, that's great! Can you explain more? 🌟",
                "Really? That's new to me! I'm excited to learn more! 💫",
                "I love this kind of conversation! You're an interesting person! 🎉",
                "That's exciting! Can you share more details? ✨"
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
                    
                    print(f"🧠 Memory loaded: {self.conversation_count} previous conversations")
                    if self.user_name:
                        print(f"👋 Welcome back {self.user_name}! Nice to see you again!")
        except Exception as e:
            print(f"⚠️ Error loading memory: {e}")
            print("🔄 Creating new memory...")
    
    def load_personality(self):
        """تحميل شخصية الـ AI"""
        try:
            if os.path.exists(self.personality_file):
                with open(self.personality_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.ai_personality_memory = data.get('ai_personality', self.ai_personality_memory)
                    print("🎭 Aya's personality loaded")
        except Exception as e:
            print(f"⚠️ Error loading personality: {e}")
    
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
                
            print("💾 Memory saved successfully")
                
        except Exception as e:
            print(f"❌ Error saving memory: {e}")
            print(f"📁 File path: {self.data_file}")
    
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
            print(f"❌ Error saving personality: {e}")
    
    def save_conversation(self, user_input, response):
        """حفظ المحادثة مع تفاصيل أكثر"""
        try:
            conversation = {
                'timestamp': datetime.datetime.now().isoformat(),
                'user_input': user_input,
                'ai_response': response,
                'conversation_number': self.conversation_count,
                'user_name': self.user_name,
                'ai_mood': self.ai_personality_memory.get('emotional_state', 'excited and optimistic'),
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
            print(f"❌ Error saving conversation: {e}")
    
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
                    return f"I'll remember your name {name}! So excited to meet you! 😊✨"
        
        # استخراج العمر أولاً (لأنه أكثر تحديداً)
        age_patterns = [
            r"عمري\s+(\d+)", r"أنا\s+(\d+)\s+سنة", r"i am\s+(\d+)", 
            r"i'm\s+(\d+)", r"my age is\s+(\d+)", r"iam\s+(\d+)",
            r"i am\s+(\d+)\s+years?\s+old", r"i'm\s+(\d+)\s+years?\s+old"
        ]
        
        for pattern in age_patterns:
            match = re.search(pattern, input_lower)
            if match:
                age = match.group(1)
                if 5 <= int(age) <= 120:
                    self.user_info['age'] = age
                    return f"I'll remember that you're {age} years old! Thanks for sharing this information! 🌟"
        
        # استخراج المهنة (بعد العمر لتجنب التداخل)
        profession_patterns = [
            r"أنا\s+(\w+)", r"أعمل\s+(\w+)", r"مهنتي\s+(\w+)",
            r"i am a\s+(\w+)", r"i work as\s+(\w+)", r"my job is\s+(\w+)",
            r"iam a\s+(\w+)", r"i'm a\s+(\w+)", r"i am\s+(\w+)"
        ]
        
        for pattern in profession_patterns:
            match = re.search(pattern, input_lower)
            if match:
                profession = match.group(1)
                # تجنب استخراج الأرقام كمهنة
                if len(profession) > 2 and not profession.isdigit():
                    self.user_info['profession'] = profession
                    return f"Excellent! I'll remember that you're a {profession}! That's amazing! 💫"
        
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
                    return f"I'll remember that you're from {location}! Beautiful place! 🎉"
        
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
                    return f"Great! I'll remember that your favorite color is {color}! Beautiful color! ✨"
        
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
                    return f"Excellent! I'll remember that you like {interest}! That's interesting! 🌟"
        
        return None
    
    def update_relationship_level(self):
        """تحديث مستوى العلاقة مع المستخدم"""
        if self.conversation_count < 5:
            self.user_info['relationship_level'] = "new"
        elif self.conversation_count < 20:
            self.user_info['relationship_level'] = "friend"
        elif self.conversation_count < 50:
            self.user_info['relationship_level'] = "close_friend"
        else:
            self.user_info['relationship_level'] = "family"
    
    def extract_topics(self, text):
        """استخراج المواضيع من النص"""
        topics = []
        topic_keywords = {
            "Work": ["work", "job", "career", "profession", "office", "business"],
            "Education": ["study", "school", "university", "college", "education", "learning"],
            "Hobbies": ["hobby", "sport", "music", "art", "reading", "gaming"],
            "Family": ["family", "parents", "brother", "sister", "mother", "father"],
            "Travel": ["travel", "trip", "vacation", "journey", "visit"],
            "Food": ["food", "eat", "restaurant", "cooking", "meal"]
        }
        
        text_lower = text.lower()
        for topic, keywords in topic_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                topics.append(topic)
        
        return topics
    
    def analyze_sentiment(self, text):
        """تحليل المشاعر في النص"""
        positive_words = ["happy", "great", "awesome", "beautiful", "love", "excellent", "wonderful", "amazing"]
        negative_words = ["sad", "bad", "problem", "difficult", "terrible", "awful", "hate"]
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return "positive"
        elif negative_count > positive_count:
            return "negative"
        else:
            return "neutral"
    
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
        memory_keywords = ["تذكر", "هل تتذكر", "remember", "do you remember", "recall", "what is my", "my age", "my name", "my profession", "my location", "my favorite"]
        info_keywords = ["معلومات", "أخبرني عن", "tell me about", "what do you know", "my info", "about me", "about myself"]
        
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
                relationship_level = self.user_info.get('relationship_level', 'new')
                if relationship_level == "family":
                    response = f"Hello {self.user_name}! I missed you! How are you today? 😊💕"
                elif relationship_level == "close_friend":
                    response = f"Hi {self.user_name}! So happy to see you! How are you? 🌟✨"
                else:
                    response = f"Hello {self.user_name}! Welcome! How are you? 😊"
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
                "Why don't computers play cards? Because they're afraid of poker! 😄",
                "What's the fastest animal in the forest? The turtle... when it's running from the wolf! 🐢",
                "Why doesn't the sun go to school? Because it's already bright! ☀️",
                "What's the only bird that can't fly? The penguin... because it prefers swimming! 🐧",
                "Why can't programmers sleep? Because they're waiting for the program to finish running! 💻😴"
            ]
            response = random.choice(jokes)
        
        elif intent == "time":
            current_time = self.get_current_time()
            response = f"The current time is {current_time} ⏰✨"
        
        elif intent == "date":
            current_date = self.get_current_date()
            response = f"Today's date is {current_date} 📅🌟"
        
        elif intent == "name":
            response = f"I'm {self.name}! Nice to meet you 😊✨"
        
        elif intent == "memory":
            # تحقق من الأسئلة المحددة
            input_lower = user_input.lower()
            
            if "age" in input_lower or "old" in input_lower:
                if self.user_info['age']:
                    return f"Yes! I remember that you're {self.user_info['age']} years old! 😊✨"
                else:
                    return "I don't remember your age yet. Tell me how old you are! 🌟"
            
            elif "name" in input_lower:
                if self.user_info['name']:
                    return f"Yes! I remember that your name is {self.user_info['name']}! 😊✨"
                else:
                    return "I don't remember your name yet. Tell me your name! 🌟"
            
            elif "profession" in input_lower or "job" in input_lower or "work" in input_lower:
                if self.user_info['profession']:
                    return f"Yes! I remember that you work as a {self.user_info['profession']}! 😊✨"
                else:
                    return "I don't remember your profession yet. Tell me what you do! 🌟"
            
            elif "location" in input_lower or "from" in input_lower or "live" in input_lower:
                if self.user_info['location']:
                    return f"Yes! I remember that you're from {self.user_info['location']}! 😊✨"
                else:
                    return "I don't remember where you're from yet. Tell me where you live! 🌟"
            
            elif "favorite" in input_lower and "color" in input_lower:
                if self.user_info['favorite_color']:
                    return f"Yes! I remember that your favorite color is {self.user_info['favorite_color']}! 😊✨"
                else:
                    return "I don't remember your favorite color yet. Tell me your favorite color! 🌟"
            
            # استدعاء عام للذاكرة
            elif self.user_info['name'] or self.user_info['age'] or self.user_info['location'] or self.user_info['interests']:
                info_parts = []
                if self.user_info['name']:
                    info_parts.append(f"your name is {self.user_info['name']}")
                if self.user_info['age']:
                    info_parts.append(f"you're {self.user_info['age']} years old")
                if self.user_info['location']:
                    info_parts.append(f"you're from {self.user_info['location']}")
                if self.user_info['profession']:
                    info_parts.append(f"you work as a {self.user_info['profession']}")
                if self.user_info['favorite_color']:
                    info_parts.append(f"your favorite color is {self.user_info['favorite_color']}")
                if self.user_info['interests']:
                    interests = ", ".join(self.user_info['interests'])
                    info_parts.append(f"you like {interests}")
                
                return f"Yes! I remember that {', '.join(info_parts)}! 😊✨"
            else:
                return "I don't remember much about you yet. Tell me about yourself! 🌟"
        
        elif intent == "info":
            if self.user_info['name'] or self.user_info['age'] or self.user_info['location'] or self.user_info['interests']:
                response = "Here's what I know about you:\n"
                if self.user_info['name']:
                    response += f"- Name: {self.user_info['name']}\n"
                if self.user_info['age']:
                    response += f"- Age: {self.user_info['age']} years old\n"
                if self.user_info['location']:
                    response += f"- Location: {self.user_info['location']}\n"
                if self.user_info['profession']:
                    response += f"- Profession: {self.user_info['profession']}\n"
                if self.user_info['favorite_color']:
                    response += f"- Favorite Color: {self.user_info['favorite_color']}\n"
                if self.user_info['interests']:
                    response += f"- Interests: {', '.join(self.user_info['interests'])}\n"
                response += f"- Conversation Count: {self.conversation_count}\n"
                response += f"- Relationship Level: {self.user_info.get('relationship_level', 'new')}"
            else:
                response = "I don't know much about you yet. Tell me about yourself! 🌟"
        
        else:
            # تحقق إذا كان هذا يبدو كمعلومات جديدة للتعلم
            if len(user_input.split()) > 3 and not any(keyword in user_input.lower() for keyword in ["?", "what", "how", "when", "where", "why"]):
                response = random.choice(self.responses["learning"])
            else:
                response = random.choice(self.responses["default"])
        
        # إضافة تعبيرات عفوية حسب مستوى العلاقة
        if self.conversation_count > 3:
            relationship_level = self.user_info.get('relationship_level', 'new')
            if relationship_level == "family":
                expressions = [" 💕", " 🥰", " ✨", " 💫", " 🌟"]
            elif relationship_level == "close_friend":
                expressions = [" 😊", " ✨", " 💫", " 🌟"]
            else:
                expressions = [" 😊", " ✨"]
            response += random.choice(expressions)
        
        return response
    
    def chat(self):
        """بدء المحادثة التفاعلية المحسنة"""
        print("=" * 60)
        print(f"🤖 {self.name}: Hello! I'm {self.name}, your intelligent and friendly assistant!")
        print("💬 Type 'exit' or 'quit' to end the conversation")
        print("🧠 I learn from our conversations and remember everything!")
        print("✨ I have a unique personality and evolve with each conversation!")
        
        # عرض المعلومات المحفوظة
        if self.user_info['name']:
            relationship_level = self.user_info.get('relationship_level', 'new')
            print(f"👋 Welcome back {self.user_info['name']}! Nice to see you again!")
            print(f"💕 Relationship level: {relationship_level}")
        
        if self.conversation_count > 0:
            print(f"📊 This is conversation #{self.conversation_count + 1}")
        
        print("=" * 60)
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    farewell = random.choice(self.responses["farewell"])
                    print(f"\n🤖 {self.name}: {farewell}")
                    break
                
                if not user_input:
                    print(f"\n🤖 {self.name}: I can't hear you, can you repeat that?")
                    continue
                
                response = self.get_enhanced_response(user_input)
                print(f"\n🤖 {self.name}: {response}")
                
                # حفظ المحادثة والذاكرة
                self.save_conversation(user_input, response)
                self.save_memory()
                self.save_personality()
                
            except KeyboardInterrupt:
                print(f"\n\n🤖 {self.name}: Goodbye! Have a wonderful day! 👋")
                # حفظ البيانات قبل الخروج
                self.save_memory()
                self.save_personality()
                break
            except Exception as e:
                print(f"\n🤖 {self.name}: Sorry, something went wrong. Can you try again?")
                print(f"Error: {str(e)}")

def main():
    """الدالة الرئيسية"""
    agent = EnhancedLearningAIAgent()
    agent.chat()

if __name__ == "__main__":
    main()
