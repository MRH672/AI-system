#!/usr/bin/env python3
"""
ملف اختبار بسيط لـ AI Agent
"""

from ai_agent import AIAgent

def test_agent():
    """اختبار وظائف الـ Agent الأساسية"""
    print("🧪 بدء اختبار AI Agent...")
    
    # إنشاء instance جديد
    agent = AIAgent("test_memory.db")
    
    # اختبارات أساسية
    test_cases = [
        "Hello, how are you?",
        "I love this weather today!",
        "I'm feeling sad about work",
        "Can you help me with programming?",
        "What's your favorite food?"
    ]
    
    print("\n📝 اختبار التفاعل الأساسي:")
    for i, test_input in enumerate(test_cases, 1):
        print(f"\n--- اختبار {i} ---")
        print(f"المستخدم: {test_input}")
        
        response = agent.interact(test_input)
        print(f"AI Agent: {response}")
        
        # محاكاة ردود الفعل الإيجابية
        agent._learn_from_feedback(test_input, response, "good")
    
    # اختبار الإحصائيات
    print("\n📊 إحصائيات التعلم:")
    stats = agent.get_learning_stats()
    for key, value in stats.items():
        print(f"• {key}: {value}")
    
    # اختبار البحث عن محادثات مشابهة
    print("\n🔍 اختبار البحث عن محادثات مشابهة:")
    similar = agent._find_similar_conversation("Hello there!")
    if similar:
        print(f"وجدت محادثة مشابهة: {similar['user_input']}")
    else:
        print("لم يتم العثور على محادثة مشابهة")
    
    print("\n✅ تم الانتهاء من الاختبار بنجاح!")
    
    # تنظيف ملف الاختبار
    import os
    if os.path.exists("test_memory.db"):
        os.remove("test_memory.db")
        print("🧹 تم حذف ملف قاعدة البيانات التجريبي")

if __name__ == "__main__":
    test_agent()
