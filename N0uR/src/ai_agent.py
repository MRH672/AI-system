"""
AI Agent - الذكي الذي يتعلم
الملف الرئيسي للـ Agent
"""

import json
import sqlite3
import numpy as np
from datetime import datetime
from typing import Dict, List, Any, Optional
import re
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle

# تحميل البيانات المطلوبة لـ NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class AIAgent:
    """
    AI Agent يتفاعل مع المستخدم ويتعلم منه
    """
    
    def __init__(self, db_path: str = "agent_memory.db"):
        self.db_path = db_path
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        self.conversation_history = []
        self.learned_patterns = {}
        self.user_preferences = {}
        self.knowledge_base = {}
        
        # إعداد قاعدة البيانات
        self._setup_database()
        
        # تحميل البيانات المحفوظة
        self._load_memory()
        
        # إعداد معالج النصوص
        self.stop_words = set(stopwords.words('english'))
        
    def _setup_database(self):
        """إعداد قاعدة البيانات لحفظ الذاكرة"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # جدول المحادثات
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT,
                agent_response TEXT,
                timestamp DATETIME,
                sentiment TEXT,
                topic TEXT
            )
        ''')
        
        # جدول الأنماط المتعلمة
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS learned_patterns (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pattern TEXT,
                response TEXT,
                frequency INTEGER,
                success_rate REAL
            )
        ''')
        
        # جدول تفضيلات المستخدم
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_preferences (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                preference_type TEXT,
                preference_value TEXT,
                confidence REAL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def _load_memory(self):
        """تحميل الذاكرة من قاعدة البيانات"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # تحميل المحادثات
        cursor.execute('SELECT user_input, agent_response, sentiment, topic FROM conversations')
        conversations = cursor.fetchall()
        
        for conv in conversations:
            self.conversation_history.append({
                'user_input': conv[0],
                'agent_response': conv[1],
                'sentiment': conv[2],
                'topic': conv[3]
            })
        
        # تحميل الأنماط المتعلمة
        cursor.execute('SELECT pattern, response, frequency, success_rate FROM learned_patterns')
        patterns = cursor.fetchall()
        
        for pattern in patterns:
            self.learned_patterns[pattern[0]] = {
                'response': pattern[1],
                'frequency': pattern[2],
                'success_rate': pattern[3]
            }
        
        # تحميل تفضيلات المستخدم
        cursor.execute('SELECT preference_type, preference_value, confidence FROM user_preferences')
        preferences = cursor.fetchall()
        
        for pref in preferences:
            self.user_preferences[pref[0]] = {
                'value': pref[1],
                'confidence': pref[2]
            }
        
        conn.close()
    
    def _save_conversation(self, user_input: str, agent_response: str, sentiment: str, topic: str):
        """حفظ المحادثة في قاعدة البيانات"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO conversations (user_input, agent_response, timestamp, sentiment, topic)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_input, agent_response, datetime.now(), sentiment, topic))
        
        conn.commit()
        conn.close()
    
    def _save_pattern(self, pattern: str, response: str, success: bool):
        """حفظ أو تحديث نمط متعلم"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if pattern in self.learned_patterns:
            # تحديث النمط الموجود
            current = self.learned_patterns[pattern]
            new_frequency = current['frequency'] + 1
            new_success_rate = ((current['success_rate'] * current['frequency']) + (1 if success else 0)) / new_frequency
            
            cursor.execute('''
                UPDATE learned_patterns 
                SET frequency = ?, success_rate = ?
                WHERE pattern = ?
            ''', (new_frequency, new_success_rate, pattern))
            
            self.learned_patterns[pattern]['frequency'] = new_frequency
            self.learned_patterns[pattern]['success_rate'] = new_success_rate
        else:
            # إضافة نمط جديد
            cursor.execute('''
                INSERT INTO learned_patterns (pattern, response, frequency, success_rate)
                VALUES (?, ?, 1, ?)
            ''', (pattern, response, 1.0 if success else 0.0))
            
            self.learned_patterns[pattern] = {
                'response': response,
                'frequency': 1,
                'success_rate': 1.0 if success else 0.0
            }
        
        conn.commit()
        conn.close()
    
    def _analyze_sentiment(self, text: str) -> str:
        """تحليل المشاعر في النص"""
        positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'love', 'like', 'happy', 'pleased']
        negative_words = ['bad', 'terrible', 'awful', 'hate', 'dislike', 'angry', 'sad', 'disappointed']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
    
    def _extract_topic(self, text: str) -> str:
        """استخراج الموضوع من النص"""
        # كلمات مفتاحية شائعة للمواضيع
        topic_keywords = {
            'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon'],
            'weather': ['weather', 'rain', 'sunny', 'cloudy', 'temperature'],
            'food': ['food', 'eat', 'restaurant', 'cooking', 'recipe'],
            'work': ['work', 'job', 'office', 'meeting', 'project'],
            'technology': ['computer', 'software', 'programming', 'AI', 'technology'],
            'personal': ['family', 'friend', 'relationship', 'personal', 'life']
        }
        
        text_lower = text.lower()
        for topic, keywords in topic_keywords.items():
            if any(keyword in text_lower for keyword in keywords):
                return topic
        
        return 'general'
    
    def _find_similar_conversation(self, user_input: str) -> Optional[Dict]:
        """البحث عن محادثة مشابهة في التاريخ"""
        if not self.conversation_history:
            return None
        
        # تحضير النصوص للمقارنة
        texts = [conv['user_input'] for conv in self.conversation_history]
        texts.append(user_input)
        
        try:
            # تحويل النصوص إلى متجهات
            tfidf_matrix = self.vectorizer.fit_transform(texts)
            
            # حساب التشابه
            similarities = cosine_similarity(tfidf_matrix[-1:], tfidf_matrix[:-1])
            
            # العثور على أكثر محادثة تشابهاً
            max_similarity_idx = np.argmax(similarities[0])
            max_similarity = similarities[0][max_similarity_idx]
            
            if max_similarity > 0.3:  # عتبة التشابه
                return self.conversation_history[max_similarity_idx]
            
        except Exception as e:
            print(f"خطأ في البحث عن المحادثة المشابهة: {e}")
        
        return None
    
    def _generate_response(self, user_input: str) -> str:
        """توليد رد بناءً على المدخلات"""
        # تحليل المدخلات
        sentiment = self._analyze_sentiment(user_input)
        topic = self._extract_topic(user_input)
        
        # البحث عن محادثة مشابهة
        similar_conv = self._find_similar_conversation(user_input)
        
        # البحث عن أنماط متعلمة
        best_pattern = None
        best_confidence = 0
        
        for pattern, data in self.learned_patterns.items():
            if pattern.lower() in user_input.lower():
                confidence = data['success_rate'] * (1 + data['frequency'] * 0.1)
                if confidence > best_confidence:
                    best_confidence = confidence
                    best_pattern = data
        
        # توليد الرد
        if best_pattern and best_confidence > 0.5:
            response = best_pattern['response']
        elif similar_conv:
            response = f"أفهم أنك تتحدث عن {topic}. بناءً على محادثتنا السابقة، {similar_conv['agent_response']}"
        else:
            # رد عام بناءً على الموضوع والمشاعر
            if topic == 'greeting':
                response = "مرحباً! كيف يمكنني مساعدتك اليوم؟"
            elif topic == 'weather':
                response = "الطقس موضوع مثير للاهتمام. كيف هو الطقس في منطقتك؟"
            elif topic == 'food':
                response = "الطعام رائع! هل تريد التحدث عن وصفة معينة أو مطعم؟"
            elif topic == 'work':
                response = "العمل جزء مهم من حياتنا. كيف تسير الأمور في عملك؟"
            elif topic == 'technology':
                response = "التكنولوجيا تتطور بسرعة! ما الذي يثير اهتمامك في هذا المجال؟"
            elif sentiment == 'positive':
                response = "أشعر أنك في مزاج جيد اليوم! هذا رائع."
            elif sentiment == 'negative':
                response = "يبدو أنك تمر بيوم صعب. هل تريد التحدث عن ما يزعجك؟"
            else:
                response = "هذا مثير للاهتمام. هل يمكنك إعطائي المزيد من التفاصيل؟"
        
        return response
    
    def _learn_from_feedback(self, user_input: str, agent_response: str, feedback: str):
        """التعلم من ردود الفعل"""
        if feedback.lower() in ['good', 'great', 'excellent', 'yes', 'correct']:
            # ردود فعل إيجابية
            pattern = user_input.lower()
            self._save_pattern(pattern, agent_response, True)
            
            # تحديث تفضيلات المستخدم
            topic = self._extract_topic(user_input)
            if topic not in self.user_preferences:
                self.user_preferences[topic] = {'value': agent_response, 'confidence': 0.5}
            else:
                self.user_preferences[topic]['confidence'] = min(1.0, 
                    self.user_preferences[topic]['confidence'] + 0.1)
        
        elif feedback.lower() in ['bad', 'wrong', 'no', 'incorrect']:
            # ردود فعل سلبية
            pattern = user_input.lower()
            self._save_pattern(pattern, agent_response, False)
    
    def interact(self, user_input: str, feedback: Optional[str] = None) -> str:
        """التفاعل الرئيسي مع المستخدم"""
        # توليد الرد
        response = self._generate_response(user_input)
        
        # تحليل المدخلات
        sentiment = self._analyze_sentiment(user_input)
        topic = self._extract_topic(user_input)
        
        # حفظ المحادثة
        self._save_conversation(user_input, response, sentiment, topic)
        self.conversation_history.append({
            'user_input': user_input,
            'agent_response': response,
            'sentiment': sentiment,
            'topic': topic
        })
        
        # التعلم من ردود الفعل إذا كانت متوفرة
        if feedback:
            self._learn_from_feedback(user_input, response, feedback)
        
        return response
    
    def get_learning_stats(self) -> Dict[str, Any]:
        """الحصول على إحصائيات التعلم"""
        return {
            'total_conversations': len(self.conversation_history),
            'learned_patterns': len(self.learned_patterns),
            'user_preferences': len(self.user_preferences),
            'recent_topics': list(set([conv['topic'] for conv in self.conversation_history[-10:]])),
            'sentiment_distribution': {
                'positive': len([c for c in self.conversation_history if c['sentiment'] == 'positive']),
                'negative': len([c for c in self.conversation_history if c['sentiment'] == 'negative']),
                'neutral': len([c for c in self.conversation_history if c['sentiment'] == 'neutral'])
            }
        }
    
    def reset_memory(self):
        """إعادة تعيين الذاكرة"""
        self.conversation_history = []
        self.learned_patterns = {}
        self.user_preferences = {}
        
        # حذف البيانات من قاعدة البيانات
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM conversations')
        cursor.execute('DELETE FROM learned_patterns')
        cursor.execute('DELETE FROM user_preferences')
        conn.commit()
        conn.close()
        
        print("تم إعادة تعيين الذاكرة بنجاح!")

# مثال على الاستخدام
if __name__ == "__main__":
    # إنشاء الـ Agent
    agent = AIAgent()
    
    print("مرحباً! أنا AI Agent أتعلم من تفاعلي معك.")
    print("اكتب 'exit' للخروج، 'stats' لرؤية الإحصائيات، 'reset' لإعادة تعيين الذاكرة")
    print("-" * 50)
    
    while True:
        user_input = input("\nأنت: ").strip()
        
        if user_input.lower() == 'exit':
            print("شكراً لك! وداعاً!")
            break
        elif user_input.lower() == 'stats':
            stats = agent.get_learning_stats()
            print(f"\nإحصائيات التعلم:")
            print(f"عدد المحادثات: {stats['total_conversations']}")
            print(f"الأنماط المتعلمة: {stats['learned_patterns']}")
            print(f"تفضيلات المستخدم: {stats['user_preferences']}")
            print(f"المواضيع الأخيرة: {', '.join(stats['recent_topics'])}")
            print(f"توزيع المشاعر: {stats['sentiment_distribution']}")
            continue
        elif user_input.lower() == 'reset':
            agent.reset_memory()
            continue
        elif not user_input:
            continue
        
        # التفاعل مع المستخدم
        response = agent.interact(user_input)
        print(f"AI Agent: {response}")
        
        # طلب ردود الفعل
        feedback = input("\nهل كان الرد مناسباً؟ (good/bad أو اضغط Enter لتجاهل): ").strip()
        if feedback:
            agent._learn_from_feedback(user_input, response, feedback)
