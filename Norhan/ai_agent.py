#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI Agent - مساعد ذكي صغير
يمكنه التفاعل مع المستخدم لأي مهمة
"""

import json
import random
import datetime
import os
import sys
from typing import Dict, List, Any, Optional

class AIAgent:
    def __init__(self):
        self.name = "نوران AI"
        self.version = "1.0.0"
        self.conversation_history = []
        self.user_preferences = {}
        self.capabilities = [
            "الرد على الأسئلة العامة",
            "حل المسائل الرياضية",
            "كتابة النصوص",
            "ترجمة النصوص",
            "توليد الأفكار",
            "مساعدة في البرمجة",
            "تحليل البيانات",
            "التخطيط للمهام",
            "الكتابة الإبداعية",
            "المساعدة في التعلم"
        ]
        
    def greet(self) -> str:
        """تحية المستخدم"""
        greetings = [
            f"مرحباً! أنا {self.name}، مساعدك الذكي. كيف يمكنني مساعدتك اليوم؟",
            f"أهلاً وسهلاً! أنا {self.name}. ما الذي تود العمل عليه؟",
            f"مرحباً بك! أنا {self.name}، جاهز لمساعدتك في أي مهمة.",
            f"أهلاً! أنا {self.name}. أخبرني كيف يمكنني مساعدتك؟"
        ]
        return random.choice(greetings)
    
    def get_capabilities(self) -> str:
        """عرض قدرات الوكيل"""
        capabilities_text = "يمكنني مساعدتك في:\n"
        for i, capability in enumerate(self.capabilities, 1):
            capabilities_text += f"{i}. {capability}\n"
        return capabilities_text
    
    def process_math(self, expression: str) -> str:
        """حل المسائل الرياضية البسيطة"""
        try:
            # تنظيف التعبير الرياضي
            expression = expression.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            return f"النتيجة: {result}"
        except:
            return "عذراً، لا يمكنني حل هذا التعبير الرياضي. تأكد من كتابته بشكل صحيح."
    
    def generate_ideas(self, topic: str) -> str:
        """توليد أفكار حول موضوع معين"""
        idea_templates = [
            f"فكرة 1: يمكنك إنشاء مشروع {topic} باستخدام التكنولوجيا الحديثة",
            f"فكرة 2: تطوير تطبيق {topic} يخدم المجتمع",
            f"فكرة 3: تنظيم ورشة عمل حول {topic}",
            f"فكرة 4: كتابة مقال أو مدونة عن {topic}",
            f"فكرة 5: إنشاء فيديو تعليمي عن {topic}"
        ]
        return "\n".join(idea_templates)
    
    def help_with_programming(self, language: str, task: str) -> str:
        """مساعدة في البرمجة"""
        if language.lower() in ['python', 'باثون']:
            return f"""
إليك مساعدة في Python:
- للمبتدئين: ابدأ بـ print("Hello World")
- للوظائف: def function_name():
- للحلقات: for i in range(10):
- للشروط: if condition:
- للمهام: {task}
"""
        elif language.lower() in ['javascript', 'جافا سكريبت']:
            return f"""
إليك مساعدة في JavaScript:
- للمبتدئين: console.log("Hello World")
- للوظائف: function functionName() {{}}
- للحلقات: for(let i = 0; i < 10; i++)
- للشروط: if (condition) {{}}
- للمهام: {task}
"""
        else:
            return f"يمكنني مساعدتك في البرمجة. ما هي اللغة التي تريد استخدامها؟"
    
    def translate_text(self, text: str, target_lang: str = "arabic") -> str:
        """ترجمة النصوص (مبسطة)"""
        # ترجمة بسيطة للكلمات الشائعة
        translations = {
            "hello": "مرحباً",
            "world": "عالم",
            "thank you": "شكراً لك",
            "good morning": "صباح الخير",
            "good evening": "مساء الخير",
            "how are you": "كيف حالك",
            "i love you": "أحبك",
            "yes": "نعم",
            "no": "لا"
        }
        
        text_lower = text.lower()
        if text_lower in translations:
            return f"الترجمة: {translations[text_lower]}"
        else:
            return f"عذراً، لا يمكنني ترجمة '{text}' حالياً. جرب كلمات أخرى."
    
    def create_plan(self, task: str) -> str:
        """إنشاء خطة للمهمة"""
        plan = f"""
خطة لـ: {task}

الخطوة 1: فهم المطلوب بوضوح
الخطوة 2: جمع المعلومات والموارد اللازمة
الخطوة 3: تقسيم المهمة إلى أجزاء صغيرة
الخطوة 4: البدء بالأجزاء الأسهل
الخطوة 5: مراجعة التقدم بانتظام
الخطوة 6: إكمال المهمة ومراجعتها
الخطوة 7: الاحتفال بالإنجاز! 🎉
"""
        return plan
    
    def get_current_time(self) -> str:
        """الحصول على الوقت الحالي"""
        now = datetime.datetime.now()
        return f"الوقت الحالي: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    
    def process_request(self, user_input: str) -> str:
        """معالجة طلب المستخدم"""
        user_input = user_input.strip().lower()
        
        # حفظ المحادثة
        self.conversation_history.append({
            "user": user_input,
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        # معالجة الطلبات المختلفة
        if any(word in user_input for word in ['مرحبا', 'أهلا', 'hello', 'hi']):
            return self.greet()
        
        elif any(word in user_input for word in ['قدرات', 'capabilities', 'ماذا تستطيع']):
            return self.get_capabilities()
        
        elif any(word in user_input for word in ['وقت', 'time', 'الساعة']):
            return self.get_current_time()
        
        elif any(word in user_input for word in ['+', '-', '*', '/', '×', '÷', 'حساب', 'math']):
            return self.process_math(user_input)
        
        elif any(word in user_input for word in ['فكرة', 'ideas', 'أفكار']):
            topic = user_input.replace('فكرة', '').replace('ideas', '').strip()
            return self.generate_ideas(topic if topic else "عام")
        
        elif any(word in user_input for word in ['برمجة', 'programming', 'كود', 'code']):
            return self.help_with_programming("python", user_input)
        
        elif any(word in user_input for word in ['ترجمة', 'translate', 'ترجم']):
            text = user_input.replace('ترجمة', '').replace('translate', '').strip()
            return self.translate_text(text)
        
        elif any(word in user_input for word in ['خطة', 'plan', 'خطط']):
            task = user_input.replace('خطة', '').replace('plan', '').strip()
            return self.create_plan(task if task else "مهمة عامة")
        
        elif any(word in user_input for word in ['شكرا', 'thank you', 'thanks']):
            return "العفو! سعيد لمساعدتك. هل هناك شيء آخر يمكنني فعله؟"
        
        else:
            # رد عام ذكي
            responses = [
                "هذا مثير للاهتمام! هل يمكنك توضيح المزيد؟",
                "أفهم أنك تريد مساعدة في هذا. كيف يمكنني مساعدتك تحديداً؟",
                "ممتاز! أخبرني المزيد عن ما تريد تحقيقه.",
                "هذا سؤال جيد! دعني أفكر في أفضل طريقة لمساعدتك.",
                "أقدر ثقتك بي. ما هي الخطوة التالية التي تود اتخاذها؟"
            ]
            return random.choice(responses)
    
    def save_conversation(self, filename: str = "conversation_history.json"):
        """حفظ تاريخ المحادثة"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, ensure_ascii=False, indent=2)
            return f"تم حفظ المحادثة في {filename}"
        except Exception as e:
            return f"خطأ في حفظ المحادثة: {str(e)}"
    
    def load_conversation(self, filename: str = "conversation_history.json"):
        """تحميل تاريخ المحادثة"""
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    self.conversation_history = json.load(f)
                return f"تم تحميل المحادثة من {filename}"
            else:
                return "لم يتم العثور على ملف المحادثة"
        except Exception as e:
            return f"خطأ في تحميل المحادثة: {str(e)}"

def main():
    """الدالة الرئيسية لتشغيل الوكيل"""
    print("=" * 50)
    print("🤖 نوران AI Agent - مساعد ذكي صغير")
    print("=" * 50)
    
    agent = AIAgent()
    print(agent.greet())
    print("\nاكتب 'خروج' أو 'exit' للإنهاء")
    print("اكتب 'قدرات' لرؤية ما يمكنني فعله")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\nأنت: ").strip()
            
            if user_input.lower() in ['خروج', 'exit', 'quit', 'bye']:
                print(f"\n{agent.name}: وداعاً! كان من دواعي سروري مساعدتك. 👋")
                break
            
            if not user_input:
                continue
                
            response = agent.process_request(user_input)
            print(f"\n{agent.name}: {response}")
            
        except KeyboardInterrupt:
            print(f"\n\n{agent.name}: وداعاً! 👋")
            break
        except Exception as e:
            print(f"\n{agent.name}: عذراً، حدث خطأ: {str(e)}")

if __name__ == "__main__":
    main()
