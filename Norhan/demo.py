#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Demo Script for نوران AI Agent
عرض سريع لقدرات الوكيل الذكي
"""

from ai_agent import AIAgent
import time

def run_demo():
    """تشغيل عرض توضيحي للوكيل"""
    print("🎬 عرض توضيحي لنوران AI Agent")
    print("=" * 50)
    
    agent = AIAgent()
    
    # قائمة المهام التوضيحية
    demo_tasks = [
        "مرحبا",
        "قدرات",
        "2 + 3 * 4",
        "فكرة تطبيق ذكي",
        "برمجة Python",
        "ترجمة hello",
        "خطة مشروع جديد",
        "وقت",
        "شكرا"
    ]
    
    print(f"🤖 {agent.greet()}")
    print("\n📋 سأعرض عليك بعض القدرات:")
    time.sleep(2)
    
    for i, task in enumerate(demo_tasks, 1):
        print(f"\n--- المهمة {i}: {task} ---")
        print(f"👤 أنت: {task}")
        
        response = agent.process_request(task)
        print(f"🤖 {agent.name}: {response}")
        
        time.sleep(1)  # توقف قصير للوضوح
    
    print(f"\n🎉 انتهى العرض التوضيحي!")
    print("💡 يمكنك الآن تشغيل الوكيل باستخدام:")
    print("   - START_HERE.bat (للبدء السريع)")
    print("   - python ai_agent.py (واجهة سطر الأوامر)")
    print("   - python web_app.py (واجهة الويب)")

if __name__ == "__main__":
    run_demo()
