#!/usr/bin/env python3
"""
اختبار سريع لـ AI Agent
"""

import sys
import os

# إضافة المجلد الحالي إلى المسار
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ai_agent import AIAgent

def quick_test():
    """اختبار سريع للـ Agent"""
    print("🚀 اختبار سريع لـ AI Agent")
    print("=" * 40)
    
    # إنشاء Agent
    agent = AIAgent("quick_test.db")
    
    # اختبارات سريعة
    test_inputs = [
        "Hello!",
        "I love programming",
        "I'm feeling sad today",
        "What's the weather like?",
        "Tell me about food"
    ]
    
    for i, user_input in enumerate(test_inputs, 1):
        print(f"\n{i}. المستخدم: {user_input}")
        response = agent.interact(user_input)
        print(f"   AI Agent: {response}")
        
        # إعطاء ردود فعل إيجابية
        agent._learn_from_feedback(user_input, response, "good")
    
    # عرض الإحصائيات
    print(f"\n📊 الإحصائيات النهائية:")
    stats = agent.get_learning_stats()
    print(f"• المحادثات: {stats['total_conversations']}")
    print(f"• الأنماط المتعلمة: {stats['learned_patterns']}")
    print(f"• التفضيلات: {stats['user_preferences']}")
    
    # تنظيف
    if os.path.exists("quick_test.db"):
        os.remove("quick_test.db")
    
    print("\n✅ تم الاختبار بنجاح!")

if __name__ == "__main__":
    quick_test()
