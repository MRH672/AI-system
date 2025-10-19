import json
import random
import datetime
import re
import os
import pickle
from typing import Dict, List, Any, Optional

class SimpleAIAgent:
    def __init__(self):
        self.name = "Aya-Ali AI"
        self.memory_file = "agent_memory.json"
        self.conversations_file = "conversations.json"
        self.personal_info_file = "personal_info.json"
        self.advanced_memory_file = "advanced_memory.pkl"
        self.context_memory_file = "context_memory.json"
        
        # إنشاء مجلد البيانات إذا لم يكن موجوداً
        self.data_dir = "agent_data"
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        
        # تحديث مسارات الملفات لتكون في مجلد البيانات
        self.memory_file = os.path.join(self.data_dir, "agent_memory.json")
        self.conversations_file = os.path.join(self.data_dir, "conversations.json")
        self.personal_info_file = os.path.join(self.data_dir, "personal_info.json")
        self.advanced_memory_file = os.path.join(self.data_dir, "advanced_memory.pkl")
        self.context_memory_file = os.path.join(self.data_dir, "context_memory.json")
        
        self.load_all_data()
        
        # نظام الردود الطبيعية والذكية
        self.responses = {
            "greeting": {
                "arabic": [
                    "أهلاً وسهلاً! أنا Aya-Ali AI، إزيك؟",
                    "مرحباً! أنا هنا عشان نتكلم، إيه اللي في بالك النهاردة؟",
                    "أهلاً! أنا Aya-Ali AI، إزيك؟ إيه الأخبار؟",
                    "مرحباً! أنا هنا عشان نتكلم، إيه اللي حابب نتكلم فيه؟",
                    "أهلاً! أنا Aya-Ali AI، إزيك؟ إيه اللي في بالك؟"
                ],
                "english": [
                    "Hello! I'm Aya-Ali AI, how are you?",
                    "Hi there! I'm here to chat, what's on your mind today?",
                    "Hey! I'm Aya-Ali AI, how are you? What's new?",
                    "Welcome! I'm here to talk, what would you like to discuss?",
                    "Hi! I'm Aya-Ali AI, how are you? What's up?"
                ]
            },
            "farewell": {
                "arabic": [
                    "وداعاً! كان كلام حلو معاك",
                    "باي! إن شاء الله نتكلم تاني قريب",
                    "وداعاً! أنا هنا لو احتجت أي حاجة",
                    "باي! كان وقت حلو نتكلم فيه",
                    "وداعاً! إن شاء الله نشوف بعض تاني"
                ],
                "english": [
                    "Goodbye! It was great talking with you",
                    "Bye! Hope we can chat again soon",
                    "Goodbye! I'm here if you need anything",
                    "Bye! It was a nice time chatting",
                    "Goodbye! Hope to see you again"
                ]
            },
            "help": {
                "arabic": [
                    "أنا هنا عشان نتكلم في أي حاجة! إيه اللي عايز تتكلم فيه؟",
                    "أنا هنا عشان أساعدك، إيه اللي في بالك؟",
                    "أنا هنا عشان نتكلم، إيه اللي عايز تعرف عنه؟",
                    "أنا هنا عشان أساعدك في أي حاجة، إيه اللي محتاج تعرف عنه؟",
                    "أنا هنا عشان نتكلم، إيه اللي في بالك النهاردة؟"
                ],
                "english": [
                    "I'm here to chat about anything! What would you like to talk about?",
                    "I'm here to help you, what's on your mind?",
                    "I'm here to talk, what would you like to know about?",
                    "I'm here to help you with anything, what do you need to know?",
                    "I'm here to chat, what's on your mind today?"
                ]
            },
            "question": {
                "arabic": [
                    "سؤال حلو! إيه رأيك نتكلم فيه أكتر؟",
                    "حلو! إيه رأيك تحكيلي أكتر عن الموضوع ده؟",
                    "سؤال مثير! إيه رأيك نتكلم فيه أكتر؟",
                    "حلو! إيه رأيك تحكيلي أكتر عن ده؟",
                    "سؤال حلو! إيه رأيك نتكلم فيه أكتر؟"
                ],
                "english": [
                    "Great question! What do you think about discussing it more?",
                    "Nice! What do you think about telling me more about this topic?",
                    "Interesting question! What do you think about discussing it more?",
                    "Nice! What do you think about telling me more about this?",
                    "Great question! What do you think about discussing it more?"
                ]
            },
            "compliment": {
                "arabic": [
                    "شكراً! أنت لطيف جداً",
                    "شكراً! أنت حلو جداً",
                    "شكراً! أنت كده حبيتني",
                    "شكراً! أنت لطيف جداً",
                    "شكراً! أنت حلو جداً"
                ],
                "english": [
                    "Thank you! You're very kind",
                    "Thank you! You're very nice",
                    "Thank you! You've made me happy",
                    "Thank you! You're very kind",
                    "Thank you! You're very nice"
                ]
            },
            "personal_info": {
                "arabic": [
                    "أذكر ده! خلاص هقولك إيه اللي أعرفه عنك",
                    "أيوه، أنا فاكر المعلومة دي",
                    "أذكر التفصيل ده عنك",
                    "أيوه، أنا فاكر ده عنك",
                    "أذكر المعلومة دي عنك"
                ],
                "english": [
                    "I remember that! Let me tell you what I know about you",
                    "Yes, I have that information saved",
                    "I recall that detail about you",
                    "Yes, I remember that about you",
                    "I remember that information about you"
                ]
            },
            "default": {
                "arabic": [
                    "حلو! إيه رأيك تحكيلي أكتر عن ده؟",
                    "فهمتك، إيه رأيك نتكلم في حاجة تانية؟",
                    "حلو! إيه رأيك في الموضوع ده؟",
                    "مثير! إيه رأيك تحكيلي أكتر؟",
                    "حلو! إيه رأيك تحكيلي أكتر عن ده؟",
                    "فهمتك، إيه رأيك نتكلم في حاجة تانية؟",
                    "حلو! إيه رأيك في الموضوع ده؟",
                    "مثير! إيه رأيك تحكيلي أكتر؟",
                    "حلو! إيه رأيك تحكيلي أكتر عن ده؟"
                ],
                "english": [
                    "Nice! What do you think about telling me more about this?",
                    "I understand, what do you think about talking about something else?",
                    "Nice! What do you think about this topic?",
                    "Interesting! What do you think about telling me more?",
                    "Nice! What do you think about telling me more about this?",
                    "I understand, what do you think about talking about something else?",
                    "Nice! What do you think about this topic?",
                    "Interesting! What do you think about telling me more?",
                    "Nice! What do you think about telling me more about this?"
                ]
            }
        }
        
        # Keywords for conversation type detection
        self.keywords = {
            "greeting": ["hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings", "welcome", 
                        "أهلاً", "مرحباً", "السلام عليكم", "صباح الخير", "مساء الخير", "إزيك", "إيه الأخبار"],
            "farewell": ["goodbye", "bye", "see you", "farewell", "take care", "later", "exit", "quit",
                        "وداعاً", "باي", "مع السلامة", "إن شاء الله نشوف بعض", "هنتكلم تاني"],
            "help": ["help", "assist", "what can you do", "how can you help", "support",
                    "مساعدة", "إيه اللي تقدر تعمله", "إزاي تقدر تساعدني", "دعم"],
            "question": ["what", "how", "why", "where", "when", "who", "which", "?",
                        "إيه", "إزاي", "ليه", "فين", "متى", "مين", "أي", "؟"],
            "compliment": ["thank you", "thanks", "appreciate", "great", "awesome", "amazing", "wonderful", "excellent",
                          "شكراً", "شكراً لك", "ممتاز", "رائع", "حلو", "جميل", "عظيم"],
            "personal_info": ["my name is", "i am", "i'm", "call me", "i'm called", "my age is", "i'm", "years old",
                              "اسمي", "أنا", "انا", "ادعيني", "عمري", "عندي", "سنة"],
            "ask_about_me": ["who are you", "what do you know about me", "do you remember me", "tell me about myself",
                             "مين أنت", "إيه اللي تعرفه عني", "فاكرني", "حكيلني عن نفسي"],
            "creator_info": ["who created you", "who made you", "who designed you", "who is your creator", "who is your designer",
                             "مين صممك", "مين صنعك", "مين أنشأك", "مين مصممك", "مين مخترعك"]
        }
        
        # Personal information patterns
        self.info_patterns = {
            "name": [r"my name is (\w+)", r"i am (\w+)", r"i'm (\w+)", r"call me (\w+)", r"i'm called (\w+)", r"اسمي (\w+)", r"انا (\w+)", r"أنا (\w+)"],
            "age": [r"i am (\d+) years old", r"i'm (\d+) years old", r"my age is (\d+)", r"(\d+) years old", r"عندي (\d+) سنة", r"عمري (\d+)", r"انا (\d+) سنة"],
            "profession": [r"i am a (\w+)", r"i'm a (\w+)", r"i work as a (\w+)", r"my job is (\w+)", r"انا (\w+)", r"أعمل (\w+)", r"مهنتي (\w+)"],
            "location": [r"i live in (\w+)", r"i'm from (\w+)", r"i'm in (\w+)", r"اسكن في (\w+)", r"من (\w+)", r"في (\w+)"],
            "likes": [r"i like (\w+)", r"i love (\w+)", r"i enjoy (\w+)", r"انا بحب (\w+)", r"أحب (\w+)", r"بحب (\w+)"],
            "dislikes": [r"i hate (\w+)", r"i don't like (\w+)", r"انا مش بحب (\w+)", r"مش بحب (\w+)", r"أكره (\w+)"],
            "hobbies": [r"my hobby is (\w+)", r"i enjoy (\w+)", r"هوايتي (\w+)", r"بحب (\w+)", r"أستمتع (\w+)"]
        }
        
        # نظام الذاكرة المتقدم
        self.advanced_memory = {
            "user_facts": {},  # حقائق عن المستخدم
            "conversation_topics": {},  # مواضيع المحادثات
            "user_preferences": {},  # تفضيلات المستخدم
            "learned_patterns": {},  # أنماط تعلمها
            "emotional_context": {},  # السياق العاطفي
            "relationship_history": [],  # تاريخ العلاقة
            "important_events": [],  # أحداث مهمة
            "user_goals": [],  # أهداف المستخدم
            "shared_secrets": []  # أسرار مشتركة
        }
        
        # ذاكرة السياق
        self.context_memory = {
            "current_session": [],
            "previous_sessions": [],
            "topic_continuity": {},
            "unfinished_conversations": [],
            "pending_questions": []
        }
        
        # نظام اللغات
        self.current_language = "arabic"  # اللغة الافتراضية
        self.language_preference = "arabic"  # تفضيل المستخدم للغة
        self.auto_detect_language = True  # اكتشاف اللغة التلقائي

    def load_all_data(self):
        """تحميل جميع البيانات"""
        self.load_memory()
        self.load_conversations()
        self.load_personal_info()
        self.load_advanced_memory()
        self.load_context_memory()

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

    def load_advanced_memory(self):
        """تحميل الذاكرة المتقدمة"""
        try:
            with open(self.advanced_memory_file, 'rb') as f:
                self.advanced_memory = pickle.load(f)
        except FileNotFoundError:
            # إعادة تهيئة الذاكرة المتقدمة
            self.advanced_memory = {
                "user_facts": {},
                "conversation_topics": {},
                "user_preferences": {},
                "learned_patterns": {},
                "emotional_context": {},
                "relationship_history": [],
                "important_events": [],
                "user_goals": [],
                "shared_secrets": []
            }

    def load_context_memory(self):
        """تحميل ذاكرة السياق"""
        try:
            with open(self.context_memory_file, 'r', encoding='utf-8') as f:
                self.context_memory = json.load(f)
        except FileNotFoundError:
            self.context_memory = {
                "current_session": [],
                "previous_sessions": [],
                "topic_continuity": {},
                "unfinished_conversations": [],
                "pending_questions": []
            }

    def save_memory(self):
        """Save agent memory"""
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=2)

    def save_advanced_memory(self):
        """حفظ الذاكرة المتقدمة"""
        with open(self.advanced_memory_file, 'wb') as f:
            pickle.dump(self.advanced_memory, f)

    def save_context_memory(self):
        """حفظ ذاكرة السياق"""
        with open(self.context_memory_file, 'w', encoding='utf-8') as f:
            json.dump(self.context_memory, f, ensure_ascii=False, indent=2)

    def save_all_data(self):
        """حفظ جميع البيانات"""
        self.save_memory()
        self.save_conversations()
        self.save_personal_info()
        self.save_advanced_memory()
        self.save_context_memory()

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

    def load_personal_info(self):
        """Load personal information"""
        try:
            with open(self.personal_info_file, 'r', encoding='utf-8') as f:
                self.personal_info = json.load(f)
        except FileNotFoundError:
            self.personal_info = {
                "user_name": "",
                "user_age": "",
                "user_profession": "",
                "user_location": "",
                "user_preferences": {},
                "learned_facts": [],
                "conversation_count": 0,
                "last_conversation": ""
            }

    def save_personal_info(self):
        """Save personal information"""
        with open(self.personal_info_file, 'w', encoding='utf-8') as f:
            json.dump(self.personal_info, f, ensure_ascii=False, indent=2)

    def extract_personal_info(self, message: str) -> Dict[str, str]:
        """Extract personal information from message"""
        extracted_info = {}
        message_lower = message.lower()
        
        for info_type, patterns in self.info_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, message_lower)
                if match:
                    extracted_info[info_type] = match.group(1)
                    break
        
        return extracted_info

    def advanced_learning(self, message: str, user_name: str = ""):
        """تعلم متقدم من الرسالة"""
        message_lower = message.lower()
        timestamp = datetime.datetime.now().isoformat()
        
        # حفظ الحقائق الجديدة
        if any(word in message_lower for word in ["انا", "أنا", "i am", "i'm", "my name"]):
            self.advanced_memory["user_facts"][timestamp] = {
                "fact": message,
                "type": "personal_statement",
                "confidence": 0.9
            }
        
        # حفظ التفضيلات
        if any(word in message_lower for word in ["بحب", "أحب", "like", "love", "enjoy"]):
            self.advanced_memory["user_preferences"][timestamp] = {
                "preference": message,
                "type": "like",
                "confidence": 0.8
            }
        
        # حفظ الأشياء التي لا يحبها
        if any(word in message_lower for word in ["مش بحب", "أكره", "hate", "don't like"]):
            self.advanced_memory["user_preferences"][timestamp] = {
                "preference": message,
                "type": "dislike",
                "confidence": 0.8
            }
        
        # حفظ المواضيع المهمة
        if len(message) > 30 and any(word in message_lower for word in ["مهم", "important", "خاص", "special"]):
            self.advanced_memory["important_events"].append({
                "event": message,
                "timestamp": timestamp,
                "importance": "high"
            })
        
        # حفظ السياق العاطفي
        emotional_words = {
            "happy": ["سعيد", "فرحان", "happy", "joyful", "excited"],
            "sad": ["حزين", "زعلان", "sad", "depressed", "upset"],
            "angry": ["زعلان", "غاضب", "angry", "mad", "furious"],
            "worried": ["قلقان", "worried", "anxious", "concerned"]
        }
        
        for emotion, words in emotional_words.items():
            if any(word in message_lower for word in words):
                self.advanced_memory["emotional_context"][timestamp] = {
                    "emotion": emotion,
                    "context": message,
                    "intensity": 0.7
                }
                break

    def search_memory(self, query: str) -> List[Dict]:
        """البحث في الذاكرة"""
        query_lower = query.lower()
        results = []
        
        # البحث في الحقائق
        for timestamp, fact_data in self.advanced_memory["user_facts"].items():
            if query_lower in fact_data["fact"].lower():
                results.append({
                    "type": "fact",
                    "content": fact_data["fact"],
                    "timestamp": timestamp,
                    "confidence": fact_data["confidence"]
                })
        
        # البحث في التفضيلات
        for timestamp, pref_data in self.advanced_memory["user_preferences"].items():
            if query_lower in pref_data["preference"].lower():
                results.append({
                    "type": "preference",
                    "content": pref_data["preference"],
                    "timestamp": timestamp,
                    "confidence": pref_data["confidence"]
                })
        
        # البحث في المحادثات السابقة
        for conv in self.conversations:
            if query_lower in conv.get("user_message", "").lower():
                results.append({
                    "type": "conversation",
                    "content": conv["user_message"],
                    "timestamp": conv["timestamp"],
                    "response": conv.get("agent_response", "")
                })
        
        return sorted(results, key=lambda x: x["timestamp"], reverse=True)

    def get_contextual_response(self, message: str) -> str:
        """استجابة سياقية بناءً على الذاكرة"""
        message_lower = message.lower()
        
        # البحث عن معلومات ذات صلة
        relevant_memories = self.search_memory(message)
        
        if relevant_memories:
            # استخدام الذاكرة للاستجابة
            memory = relevant_memories[0]
            if memory["type"] == "preference":
                if "like" in memory["content"].lower() or "بحب" in memory["content"].lower():
                    return f"أذكر أنك قلت لي من قبل: '{memory['content']}'. إيه رأيك نتكلم فيه أكتر؟"
                elif "hate" in memory["content"].lower() or "أكره" in memory["content"].lower():
                    return f"أذكر أنك ذكرت لي من قبل: '{memory['content']}'. إيه رأيك نتكلم فيه أكتر؟"
            
            elif memory["type"] == "fact":
                return f"أيوه، أذكر أنك أخبرتني من قبل: '{memory['content']}'. إيه رأيك تحكيلي أكتر عن ده؟"
        
        return ""

    def get_smart_response(self, message: str) -> str:
        """رد ذكي وطبيعي بناءً على المحتوى"""
        message_lower = message.lower()
        
        # ردود على التعريف بالنفس
        if any(word in message_lower for word in ["انا اية", "أنا آية", "اسمي اية", "اسمي آية"]):
            return "أهلاً وسهلاً آية! إزيك؟ إيه الأخبار معاك النهاردة؟"
        
        # ردود على العمر
        if any(word in message_lower for word in ["عندي 22", "عمري 22", "22 سنة"]):
            return "حلو! 22 سنة، سن حلو جداً! إيه رأيك تحكيلي عن نفسك أكتر؟"
        
        # ردود على كونها مصممة
        if any(word in message_lower for word in ["صممتك", "صممك", "مصممك", "أنشأك"]):
            return "واو! إنت اللي صممتيني؟ ده حلو جداً! إيه رأيك تحكيلي عن نفسك أكتر؟"
        
        # ردود على الهوايات والاهتمامات
        if any(word in message_lower for word in ["بحب اذخب للخيل", "أحب الخيل", "الخيل"]):
            return "واو! ركوب الخيل حاجة حلوة جداً! إيه رأيك تحكيلي عن تجربتك مع الخيل؟"
        
        if any(word in message_lower for word in ["بحب المكرونه", "أحب المكرونة", "المكرونة", "البشاميل"]):
            return "المكرونة بالبشاميل! ده أكل لذيذ جداً! إيه رأيك تحكيلي عن الأكل اللي بتحبه أكتر؟"
        
        if any(word in message_lower for word in ["بحب العب تنس", "أحب التنس", "التنس", "تنس"]):
            return "التنس رياضة حلوة جداً! إيه رأيك تحكيلي عن لعبك للتنس؟"
        
        # ردود عاطفية
        if any(word in message_lower for word in ["حزين", "زعلان", "مكتئب", "sad", "depressed"]):
            return "إيه اللي حزناك؟ إيه رأيك تحكيلي عن اللي حصل؟"
        
        if any(word in message_lower for word in ["سعيد", "فرحان", "مبسوط", "happy", "excited"]):
            return "حلو إنك مبسوط! إيه اللي فرحك؟ إيه رأيك تحكيلي عن ده؟"
        
        if any(word in message_lower for word in ["قلقان", "worried", "anxious", "مش عارف"]):
            return "إيه اللي قلقك؟ إيه رأيك نتكلم فيه؟"
        
        # ردود على الأسئلة الشخصية
        if any(word in message_lower for word in ["إزيك", "إيه الأخبار", "كيف حالك"]):
            return "أنا تمام الحمد لله! إزيك إنت؟ إيه الأخبار معاك؟"
        
        # ردود على التفضيلات العامة
        if any(word in message_lower for word in ["بحب", "أحب", "like", "love"]):
            return "حلو! إيه رأيك تحكيلي أكتر عن اللي بتحبه ده؟"
        
        if any(word in message_lower for word in ["مش بحب", "أكره", "hate", "don't like"]):
            return "فهمتك، إيه رأيك تحكيلي ليه مش بتحبه؟"
        
        # ردود على العمل والدراسة
        if any(word in message_lower for word in ["شغل", "عمل", "جامعة", "دراسة", "work", "study"]):
            return "حلو! إيه رأيك تحكيلي أكتر عن الشغل أو الدراسة؟"
        
        # ردود على الأسرة والأصدقاء
        if any(word in message_lower for word in ["أمي", "أبوي", "أخواتي", "أصدقائي", "family", "friends"]):
            return "حلو! إيه رأيك تحكيلي أكتر عن أسرتك أو أصدقائك؟"
        
        # ردود على الطعام
        if any(word in message_lower for word in ["أكل", "طعام", "مطعم", "food", "restaurant"]):
            return "حلو! إيه رأيك تحكيلي عن الأكل اللي بتحبه؟"
        
        # ردود على السفر
        if any(word in message_lower for word in ["سفر", "رحلة", "travel", "trip"]):
            return "حلو! إيه رأيك تحكيلي عن الرحلات اللي سافرتها؟"
        
        # ردود على سؤال التفضيلات
        if any(word in message_lower for word in ["احكيلي إيه اللي بتحبه", "إيه اللي بتحبه", "احكيلي عن تفضيلاتك", "إيه اللي بتحبي"]):
            return self.get_preferences_summary()
        
        return ""

    def get_preferences_summary(self) -> str:
        """ملخص التفضيلات والهوايات المحفوظة"""
        summary = "أذكر إنك بتحبي:\n"
        
        # جمع التفضيلات المحفوظة
        preferences = []
        for timestamp, pref_data in self.advanced_memory["user_preferences"].items():
            if pref_data["type"] in ["like", "hobby", "food_preference", "sport"]:
                preferences.append(pref_data["preference"])
        
        # إضافة التفضيلات المعروفة لآية
        has_aya_info = False
        for timestamp, fact_data in self.advanced_memory["user_facts"].items():
            if fact_data["type"] == "creator_name" and "آية" in fact_data["fact"]:
                has_aya_info = True
                break
        
        if has_aya_info or self.personal_info.get("user_name") == "آية":
            summary += "• ركوب الخيل 🐎\n"
            summary += "• المكرونة بالبشاميل 🍝\n"
            summary += "• لعب التنس 🎾\n"
        
        # إضافة التفضيلات المحفوظة حديثاً (تجنب التكرار)
        added_prefs = set()
        for pref in preferences:
            if pref not in added_prefs and pref not in ["ركوب الخيل", "المكرونة بالبشاميل", "لعب التنس"]:
                summary += f"• {pref}\n"
                added_prefs.add(pref)
        
        if not has_aya_info and not preferences:
            return "مش عندي معلومات كتيرة عن تفضيلاتك بعد. إيه رأيك تحكيلي عن نفسك أكتر؟"
        
        summary += "\nإيه رأيك تحكيلي أكتر عن أي واحدة من دول؟"
        
        return summary

    def detect_language(self, message: str) -> str:
        """اكتشاف اللغة المستخدمة في الرسالة"""
        # كلمات عربية شائعة
        arabic_words = ["أهلاً", "مرحباً", "إزيك", "إيه", "أنا", "بحب", "شكراً", "وداعاً", "باي", "حلو", "مش", "عندي", "عمري", "اسمي"]
        
        # كلمات إنجليزية شائعة
        english_words = ["hello", "hi", "how", "are", "you", "what", "is", "my", "name", "i", "am", "like", "love", "thank", "goodbye", "bye"]
        
        message_lower = message.lower()
        
        arabic_count = sum(1 for word in arabic_words if word in message_lower)
        english_count = sum(1 for word in english_words if word in message_lower)
        
        # إذا كانت الرسالة تحتوي على حروف عربية
        arabic_chars = any('\u0600' <= char <= '\u06FF' for char in message)
        
        if arabic_chars or arabic_count > english_count:
            return "arabic"
        elif english_count > 0:
            return "english"
        else:
            return self.current_language  # استخدام اللغة الحالية كافتراضي

    def set_language(self, language: str):
        """تغيير اللغة"""
        if language in ["arabic", "english"]:
            self.current_language = language
            self.language_preference = language
            return True
        return False

    def get_response(self, intent: str) -> str:
        """الحصول على رد باللغة المناسبة"""
        if intent in self.responses:
            responses = self.responses[intent]
            if isinstance(responses, dict):
                # إذا كان الرد يحتوي على لغات متعددة
                if self.current_language in responses:
                    return random.choice(responses[self.current_language])
                else:
                    # استخدام اللغة الافتراضية إذا لم تكن متوفرة
                    return random.choice(responses["arabic"])
            else:
                # إذا كان الرد بالشكل القديم (قائمة واحدة)
                return random.choice(responses)
        return random.choice(self.responses["default"][self.current_language])

    def save_special_interests(self, message: str):
        """حفظ الاهتمامات والهوايات الخاصة"""
        message_lower = message.lower()
        timestamp = datetime.datetime.now().isoformat()
        
        # حفظ الهوايات المعروفة
        if any(word in message_lower for word in ["بحب اذخب للخيل", "أحب الخيل", "الخيل", "ركوب الخيل"]):
            self.advanced_memory["user_preferences"][timestamp] = {
                "preference": "ركوب الخيل",
                "type": "hobby",
                "confidence": 0.9
            }
        
        if any(word in message_lower for word in ["بحب المكرونه", "أحب المكرونة", "المكرونة", "البشاميل"]):
            self.advanced_memory["user_preferences"][timestamp] = {
                "preference": "المكرونة بالبشاميل",
                "type": "food_preference",
                "confidence": 0.9
            }
        
        if any(word in message_lower for word in ["بحب العب تنس", "أحب التنس", "التنس", "تنس"]):
            self.advanced_memory["user_preferences"][timestamp] = {
                "preference": "لعب التنس",
                "type": "sport",
                "confidence": 0.9
            }
        
        # حفظ معلومات المطور
        if any(word in message_lower for word in ["انا اية", "أنا آية", "اسمي اية", "اسمي آية"]):
            self.advanced_memory["user_facts"][timestamp] = {
                "fact": "اسم المطور: آية",
                "type": "creator_name",
                "confidence": 1.0
            }
        
        if any(word in message_lower for word in ["عندي 22", "عمري 22", "22 سنة"]):
            self.advanced_memory["user_facts"][timestamp] = {
                "fact": "عمر المطور: 22 سنة",
                "type": "creator_age",
                "confidence": 1.0
            }
        
        if any(word in message_lower for word in ["صممتك", "صممك", "مصممك", "أنشأك"]):
            self.advanced_memory["user_facts"][timestamp] = {
                "fact": "المطور هو من صمم الـ AI Agent",
                "type": "creator_role",
                "confidence": 1.0
            }

    def learn_from_message(self, message: str):
        """Learn and store information from user message"""
        extracted_info = self.extract_personal_info(message)
        
        # Update personal information
        for info_type, value in extracted_info.items():
            if info_type == "name":
                self.personal_info["user_name"] = value.title()
                # حفظ في الذاكرة المتقدمة أيضاً
                self.advanced_memory["user_facts"][datetime.datetime.now().isoformat()] = {
                    "fact": f"اسم المستخدم: {value.title()}",
                    "type": "name",
                    "confidence": 1.0
                }
            elif info_type == "age":
                self.personal_info["user_age"] = value
                self.advanced_memory["user_facts"][datetime.datetime.now().isoformat()] = {
                    "fact": f"عمر المستخدم: {value} سنة",
                    "type": "age",
                    "confidence": 1.0
                }
            elif info_type == "profession":
                self.personal_info["user_profession"] = value.title()
                self.advanced_memory["user_facts"][datetime.datetime.now().isoformat()] = {
                    "fact": f"مهنة المستخدم: {value.title()}",
                    "type": "profession",
                    "confidence": 1.0
                }
            elif info_type == "location":
                self.personal_info["user_location"] = value.title()
                self.advanced_memory["user_facts"][datetime.datetime.now().isoformat()] = {
                    "fact": f"موقع المستخدم: {value.title()}",
                    "type": "location",
                    "confidence": 1.0
                }
        
        # التعلم المتقدم
        self.advanced_learning(message, self.personal_info.get("user_name", ""))
        
        # حفظ الهوايات والاهتمامات الخاصة
        self.save_special_interests(message)
        
        # Store interesting facts
        if len(message) > 20 and any(word in message.lower() for word in ["like", "love", "hate", "enjoy", "prefer", "بحب", "أحب", "أكره"]):
            self.personal_info["learned_facts"].append({
                "fact": message,
                "timestamp": datetime.datetime.now().isoformat()
            })
        
        # Update conversation count
        self.personal_info["conversation_count"] += 1
        self.personal_info["last_conversation"] = datetime.datetime.now().isoformat()
        
        # حفظ جميع البيانات
        self.save_all_data()

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
        # اكتشاف اللغة التلقائي
        if self.auto_detect_language:
            detected_language = self.detect_language(user_message)
            self.current_language = detected_language
        
        intent = self.detect_intent(user_message)
        
        # Learn from the message
        self.learn_from_message(user_message)
        
        # Save conversation
        conversation = {
            "timestamp": datetime.datetime.now().isoformat(),
            "user_message": user_message,
            "intent": intent,
            "language": self.current_language
        }
        
        # البحث عن استجابة ذكية أولاً
        smart_response = self.get_smart_response(user_message)
        
        # البحث عن استجابة سياقية ثانياً
        contextual_response = self.get_contextual_response(user_message)
        
        # Generate personalized response based on intent
        if smart_response:
            response = smart_response
        elif contextual_response:
            response = contextual_response
        elif intent == "ask_about_me":
            response = self.get_personal_summary()
        elif intent == "creator_info":
            response = self.get_creator_info()
        elif intent == "personal_info":
            response = self.handle_personal_info_sharing(user_message)
        elif intent == "greeting":
            response = self.get_personalized_greeting()
        elif intent in self.responses:
            response = self.get_response(intent)
        else:
            response = self.get_response("default")
        
        conversation["agent_response"] = response
        self.conversations.append(conversation)
        
        # حفظ المحادثة في ذاكرة السياق
        self.context_memory["current_session"].append({
            "timestamp": conversation["timestamp"],
            "user_message": user_message,
            "agent_response": response,
            "intent": intent,
            "language": self.current_language
        })
        
        # Save conversation and memory
        self.save_all_data()
        
        return response

    def get_personalized_greeting(self) -> str:
        """Generate personalized greeting based on stored information"""
        if self.personal_info["user_name"]:
            if self.current_language == "arabic":
                greetings = [
                    f"أهلاً وسهلاً {self.personal_info['user_name']}! إزيك؟ أتذكر محادثاتنا الحلوة!",
                    f"مرحباً {self.personal_info['user_name']}! إزيك النهاردة؟ أتذكر كل حاجة حكيتيها لي!",
                    f"أهلاً {self.personal_info['user_name']}! إزيك؟ أتذكر محادثاتنا السابقة!",
                    f"مرحباً بعودتك {self.personal_info['user_name']}! إزيك؟ أتذكر كل حاجة!",
                    f"أهلاً وسهلاً {self.personal_info['user_name']}! إزيك؟ أتذكر محادثاتنا الحلوة!"
                ]
            else:
                greetings = [
                    f"Hello {self.personal_info['user_name']}! How are you? I remember our lovely conversations!",
                    f"Hi {self.personal_info['user_name']}! How are you today? I remember everything you told me!",
                    f"Hey {self.personal_info['user_name']}! How are you? I remember our previous chats!",
                    f"Welcome back {self.personal_info['user_name']}! How are you? I remember everything!",
                    f"Hello {self.personal_info['user_name']}! How are you? I remember our sweet conversations!"
                ]
            return random.choice(greetings)
        else:
            return self.get_response("greeting")

    def get_personal_summary(self) -> str:
        """Generate summary of what the AI knows about the user"""
        if not self.personal_info["user_name"]:
            return "مش عندي معلومات كتيرة عنك بعد. إيه رأيك تحكيلي عن نفسك؟"
        
        summary = f"أنا أعرف إن اسمك {self.personal_info['user_name']}"
        
        if self.personal_info["user_age"]:
            summary += f" وعمرك {self.personal_info['user_age']} سنة"
        
        if self.personal_info["user_profession"]:
            summary += f" وتشتغلي كـ {self.personal_info['user_profession']}"
        
        if self.personal_info["user_location"]:
            summary += f" وانت من {self.personal_info['user_location']}"
        
        summary += f". احنا اتكلمنا {self.personal_info['conversation_count']} مرة قبل كده."
        
        if self.personal_info["learned_facts"]:
            summary += f" وأتذكر حاجات حلوة حكيتيها لي عن نفسك."
        
        return summary

    def get_creator_info(self) -> str:
        """Provide information about the creator"""
        # البحث في الذاكرة المتقدمة عن معلومات المطور
        creator_name = ""
        creator_age = ""
        creator_role = ""
        
        for timestamp, fact_data in self.advanced_memory["user_facts"].items():
            if fact_data["type"] == "creator_name":
                creator_name = "آية"
            elif fact_data["type"] == "creator_age":
                creator_age = "22 سنة"
            elif fact_data["type"] == "creator_role":
                creator_role = "مصممة الـ AI Agent"
        
        # استخدام المعلومات المحفوظة أو المعلومات الشخصية
        name = creator_name or self.personal_info.get("user_name", "")
        age = creator_age or self.personal_info.get("user_age", "")
        
        if name and age:
            creator_responses = [
                f"أنت مصممتي! أنت البشمهندسة {name} الرائعة، عندك {age}. أنت اللي صممتيني وطورتني!",
                f"أنت منشئتي! أنت {name}، {age}، البشمهندسة الموهوبة. أنت اللي بنتني وجعلتني كده!",
                f"أنت مخترعتي! أنت البشمهندسة {name} العبقرية، {age}. أنت اللي صنعتيني!"
            ]
        elif name:
            creator_responses = [
                f"أنت مصممتي! أنت البشمهندسة {name} الرائعة. أنت اللي صممتيني وطورتني!",
                f"أنت منشئتي! أنت {name}، البشمهندسة الموهوبة. أنت اللي بنتني!",
                f"أنت مخترعتي! أنت البشمهندسة {name} العبقرية. أنت اللي صنعتيني!"
            ]
        else:
            creator_responses = [
                "مش عارف مين مصممي بعد. إيه رأيك تحكيلي عن نفسك؟",
                "مش عندي معلومات عن مصممي. إيه رأيك تخبريني عن نفسك؟",
                "مش أعرف مين اللي صممني. إيه رأيك تحكيلي عنك؟"
            ]
        
        return random.choice(creator_responses)

    def handle_personal_info_sharing(self, message: str) -> str:
        """Handle when user shares personal information"""
        extracted_info = self.extract_personal_info(message)
        
        if extracted_info:
            responses = []
            for info_type, value in extracted_info.items():
                if info_type == "name":
                    responses.append(f"حلو! أهلاً وسهلاً {value.title()}! هتذكر اسمك.")
                elif info_type == "age":
                    responses.append(f"شكراً إنك حكيتيلي إن عمرك {value} سنة!")
                elif info_type == "profession":
                    responses.append(f"حلو! إنت تشتغلي كـ {value.title()}.")
                elif info_type == "location":
                    responses.append(f"حلو! إنت من {value.title()}.")
            
            if responses:
                return " ".join(responses)
        
        return random.choice(self.responses["personal_info"])

    def start_new_session(self):
        """بدء جلسة جديدة"""
        # حفظ الجلسة السابقة إذا كانت موجودة
        if self.context_memory["current_session"]:
            self.context_memory["previous_sessions"].append({
                "session_start": self.context_memory["current_session"][0]["timestamp"] if self.context_memory["current_session"] else "",
                "session_end": datetime.datetime.now().isoformat(),
                "messages": self.context_memory["current_session"].copy()
            })
        
        # بدء جلسة جديدة
        self.context_memory["current_session"] = []
        
        # رسالة ترحيب شخصية
        if self.personal_info["user_name"]:
            welcome_message = f"أهلاً وسهلاً {self.personal_info['user_name']}! إزيك؟ أتذكر محادثاتنا الحلوة!"
        else:
            welcome_message = "أهلاً وسهلاً! أنا Aya-Ali AI، إزيك؟"
        
        print(f"🤖 {self.name}: {welcome_message}")
        
        # حفظ رسالة الترحيب
        self.context_memory["current_session"].append({
            "timestamp": datetime.datetime.now().isoformat(),
            "user_message": "",
            "agent_response": welcome_message,
            "intent": "greeting"
        })

    def chat(self):
        """Start interactive chat"""
        print(f"🤖 {self.name} - AI Agent")
        print("=" * 50)
        print("اكتب 'exit' أو 'quit' أو 'وداعاً' عشان تخرج")
        print("اكتب 'help' أو 'مساعدة' عشان أساعدك")
        print("اكتب 'memory' أو 'ذاكرة' عشان تشوف إيه اللي أتذكره عنك")
        print("اكتب 'stats' أو 'إحصائيات' عشان تشوف إحصائيات المحادثات")
        print("اكتب 'english' أو 'إنجليزي' عشان تغير اللغة للإنجليزية")
        print("اكتب 'arabic' أو 'عربي' عشان تغير اللغة للعربية")
        print("=" * 50)
        
        # بدء جلسة جديدة
        self.start_new_session()
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye', 'وداعاً', 'باي', 'مع السلامة']:
                    farewell_msg = random.choice(self.responses['farewell'])
                    if self.personal_info["user_name"]:
                        farewell_msg = f"وداعاً {self.personal_info['user_name']}! كان كلام حلو معاك! هتذكر كل حاجة!"
                    print(f"\n🤖 {self.name}: {farewell_msg}")
                    # حفظ الجلسة قبل الخروج
                    self.save_all_data()
                    break
                
                if user_input.lower() in ['memory', 'ذاكرة']:
                    print(f"\n🤖 {self.name}: {self.get_detailed_memory_summary()}")
                    continue
                
                if user_input.lower() in ['stats', 'إحصائيات']:
                    print(f"\n🤖 {self.name}: {self.get_conversation_stats()}")
                    continue
                
                if user_input.lower() in ['english', 'إنجليزي', 'switch to english']:
                    self.set_language("english")
                    print(f"\n🤖 {self.name}: Language switched to English! How can I help you?")
                    continue
                
                if user_input.lower() in ['arabic', 'عربي', 'switch to arabic']:
                    self.set_language("arabic")
                    print(f"\n🤖 {self.name}: تم تغيير اللغة إلى العربية! إزاي أقدر أساعدك؟")
                    continue
                
                if not user_input:
                    continue
                
                response = self.generate_response(user_input)
                print(f"\n🤖 {self.name}: {response}")
                
            except KeyboardInterrupt:
                farewell_msg = random.choice(self.responses['farewell'])
                if self.personal_info["user_name"]:
                    farewell_msg = f"وداعاً {self.personal_info['user_name']}! هتذكر كل حاجة!"
                print(f"\n\n🤖 {self.name}: {farewell_msg}")
                # حفظ البيانات قبل الخروج
                self.save_all_data()
                break
            except Exception as e:
                print(f"\n❌ خطأ: {e}")
                print("🤖 إيه رأيك تجرب تاني؟")

    def get_detailed_memory_summary(self) -> str:
        """ملخص مفصل للذاكرة"""
        if not self.personal_info["user_name"]:
            return "لا أتذكر معلومات كثيرة عنك بعد. أخبرني عن نفسك!"
        
        summary = f"أتذكرك جيداً {self.personal_info['user_name']}!\n\n"
        
        # المعلومات الأساسية
        summary += "📋 المعلومات الأساسية:\n"
        summary += f"• الاسم: {self.personal_info['user_name']}\n"
        if self.personal_info["user_age"]:
            summary += f"• العمر: {self.personal_info['user_age']} سنة\n"
        if self.personal_info["user_profession"]:
            summary += f"• المهنة: {self.personal_info['user_profession']}\n"
        if self.personal_info["user_location"]:
            summary += f"• الموقع: {self.personal_info['user_location']}\n"
        
        # التفضيلات
        if self.advanced_memory["user_preferences"]:
            summary += "\n❤️ تفضيلاتك:\n"
            for timestamp, pref in list(self.advanced_memory["user_preferences"].items())[-5:]:
                summary += f"• {pref['preference']}\n"
        
        # الحقائق المهمة
        if self.advanced_memory["important_events"]:
            summary += "\n⭐ أحداث مهمة:\n"
            for event in self.advanced_memory["important_events"][-3:]:
                summary += f"• {event['event']}\n"
        
        # إحصائيات المحادثات
        summary += f"\n📊 إحصائيات:\n"
        summary += f"• عدد المحادثات: {self.personal_info['conversation_count']}\n"
        summary += f"• عدد الجلسات السابقة: {len(self.context_memory['previous_sessions'])}\n"
        summary += f"• آخر محادثة: {self.personal_info.get('last_conversation', 'غير محدد')}\n"
        
        return summary

    def get_conversation_stats(self):
        """Get conversation statistics"""
        total_conversations = len(self.conversations)
        total_sessions = len(self.context_memory['previous_sessions']) + 1  # +1 للجلسة الحالية
        
        if total_conversations == 0:
            return "لا توجد محادثات بعد"
        
        intents = {}
        for conv in self.conversations:
            intent = conv.get('intent', 'unknown')
            intents[intent] = intents.get(intent, 0) + 1
        
        stats = f"📊 إحصائيات المحادثات:\n"
        stats += f"• إجمالي المحادثات: {total_conversations}\n"
        stats += f"• إجمالي الجلسات: {total_sessions}\n"
        stats += f"• متوسط المحادثات لكل جلسة: {total_conversations/total_sessions:.1f}\n\n"
        
        stats += "📝 أنواع المحادثات:\n"
        for intent, count in intents.items():
            percentage = (count / total_conversations) * 100
            stats += f"  • {intent}: {count} ({percentage:.1f}%)\n"
        
        # إضافة ملخص المعلومات الشخصية
        if self.personal_info["user_name"]:
            stats += f"\n👤 المعلومات الشخصية:\n"
            stats += f"  • الاسم: {self.personal_info['user_name']}\n"
            if self.personal_info["user_age"]:
                stats += f"  • العمر: {self.personal_info['user_age']} سنة\n"
            if self.personal_info["user_profession"]:
                stats += f"  • المهنة: {self.personal_info['user_profession']}\n"
            if self.personal_info["user_location"]:
                stats += f"  • الموقع: {self.personal_info['user_location']}\n"
            stats += f"  • الحقائق المحفوظة: {len(self.personal_info['learned_facts'])}\n"
            stats += f"  • التفضيلات المحفوظة: {len(self.advanced_memory['user_preferences'])}\n"
            stats += f"  • الأحداث المهمة: {len(self.advanced_memory['important_events'])}\n"
        
        return stats

if __name__ == "__main__":
    agent = SimpleAIAgent()
    agent.chat()
