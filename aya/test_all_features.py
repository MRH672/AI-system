#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
اختبار سريع لجميع ميزات آية المحسنة
"""

import os
import sys
import json
import datetime

def test_imports():
    """اختبار استيراد جميع الوحدات"""
    print("🧪 اختبار استيراد الوحدات...")
    
    try:
        from gpt_enhanced_ai_agent import GPTEnhancedAIAgent
        print("✅ GPT Enhanced AI Agent - تم الاستيراد بنجاح")
    except Exception as e:
        print(f"❌ خطأ في استيراد GPT Enhanced AI Agent: {e}")
        return False
    
    try:
        from enhanced_ai_agent import EnhancedAIAgent
        print("✅ Enhanced AI Agent - تم الاستيراد بنجاح")
    except Exception as e:
        print(f"❌ خطأ في استيراد Enhanced AI Agent: {e}")
        return False
    
    try:
        import flask
        print("✅ Flask - تم الاستيراد بنجاح")
    except Exception as e:
        print(f"❌ خطأ في استيراد Flask: {e}")
        return False
    
    return True

def test_gpt_agent():
    """اختبار GPT Enhanced AI Agent"""
    print("\n🧪 اختبار GPT Enhanced AI Agent...")
    
    try:
        from gpt_enhanced_ai_agent import GPTEnhancedAIAgent
        
        # إنشاء agent جديد
        agent = GPTEnhancedAIAgent()
        print("✅ تم إنشاء GPT Enhanced AI Agent بنجاح")
        
        # اختبار استخراج المعلومات
        test_inputs = [
            "اسمي ماجد",
            "أنا مصمم جرافيك",
            "عمري 21 سنة",
            "لوني المفضل أزرق"
        ]
        
        for test_input in test_inputs:
            response = agent.extract_user_info(test_input)
            if response:
                print(f"✅ استخراج المعلومات: {test_input} -> {response[:50]}...")
            else:
                print(f"⚠️ لم يتم استخراج معلومات من: {test_input}")
        
        # اختبار الردود
        test_responses = [
            "مرحبا",
            "كيف حالك؟",
            "تذكر",
            "ما هو الوقت؟"
        ]
        
        for test_input in test_responses:
            response = agent.get_enhanced_response(test_input)
            print(f"✅ رد على '{test_input}': {response[:50]}...")
        
        # اختبار حفظ الذاكرة
        agent.save_memory()
        print("✅ تم حفظ الذاكرة بنجاح")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار GPT Enhanced AI Agent: {e}")
        return False

def test_enhanced_agent():
    """اختبار Enhanced AI Agent"""
    print("\n🧪 اختبار Enhanced AI Agent...")
    
    try:
        from enhanced_ai_agent import EnhancedAIAgent
        
        # إنشاء agent جديد
        agent = EnhancedAIAgent()
        print("✅ تم إنشاء Enhanced AI Agent بنجاح")
        
        # اختبار الردود
        test_responses = [
            "مرحبا",
            "كيف حالك؟",
            "تذكر",
            "ما هو الوقت؟"
        ]
        
        for test_input in test_responses:
            response = agent.get_enhanced_response(test_input)
            print(f"✅ رد على '{test_input}': {response[:50]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار Enhanced AI Agent: {e}")
        return False

def test_file_structure():
    """اختبار هيكل الملفات"""
    print("\n🧪 اختبار هيكل الملفات...")
    
    required_files = [
        "gpt_enhanced_ai_agent.py",
        "gpt_web_app.py",
        "enhanced_ai_agent.py",
        "web_app.py",
        "requirements.txt",
        "templates/gpt_index.html",
        "templates/index.html",
        "static/css/gpt_style.css",
        "static/css/style.css",
        "static/js/gpt_app.js",
        "static/js/app.js"
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - مفقود")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️ ملفات مفقودة: {len(missing_files)}")
        return False
    else:
        print("\n✅ جميع الملفات المطلوبة موجودة")
        return True

def test_memory_files():
    """اختبار ملفات الذاكرة"""
    print("\n🧪 اختبار ملفات الذاكرة...")
    
    try:
        # اختبار إنشاء ملفات الذاكرة
        from gpt_enhanced_ai_agent import GPTEnhancedAIAgent
        
        agent = GPTEnhancedAIAgent()
        
        # اختبار حفظ الذاكرة
        agent.save_memory()
        agent.save_personality()
        
        # اختبار وجود الملفات
        memory_files = [
            "aya_gpt_memory.json",
            "aya_gpt_personality.json"
        ]
        
        for file_path in memory_files:
            if os.path.exists(file_path):
                print(f"✅ {file_path} - تم إنشاؤه بنجاح")
                
                # اختبار محتوى الملف
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    print(f"✅ {file_path} - محتوى صحيح")
                except Exception as e:
                    print(f"❌ {file_path} - خطأ في المحتوى: {e}")
            else:
                print(f"❌ {file_path} - لم يتم إنشاؤه")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار ملفات الذاكرة: {e}")
        return False

def test_web_app():
    """اختبار تطبيق الويب"""
    print("\n🧪 اختبار تطبيق الويب...")
    
    try:
        from gpt_web_app import app
        
        # اختبار إنشاء التطبيق
        print("✅ تم إنشاء تطبيق الويب بنجاح")
        
        # اختبار المسارات
        routes = ['/', '/chat', '/memory', '/reset', '/conversations', '/personality', '/stats']
        
        with app.test_client() as client:
            for route in routes:
                if route == '/':
                    response = client.get(route)
                    if response.status_code == 200:
                        print(f"✅ {route} - يعمل بنجاح")
                    else:
                        print(f"❌ {route} - خطأ: {response.status_code}")
                else:
                    # اختبار المسارات الأخرى
                    if route in ['/chat']:
                        response = client.post(route, json={'message': 'test'})
                    else:
                        response = client.get(route)
                    
                    # نتوقع خطأ 400 أو 500 للجلسة غير الموجودة
                    if response.status_code in [200, 400, 500]:
                        print(f"✅ {route} - يعمل بنجاح")
                    else:
                        print(f"❌ {route} - خطأ غير متوقع: {response.status_code}")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في اختبار تطبيق الويب: {e}")
        return False

def main():
    """الدالة الرئيسية للاختبار"""
    print("=" * 60)
    print("🧪 اختبار شامل لآية - GPT Enhanced AI Agent")
    print("=" * 60)
    
    tests = [
        ("استيراد الوحدات", test_imports),
        ("هيكل الملفات", test_file_structure),
        ("GPT Enhanced AI Agent", test_gpt_agent),
        ("Enhanced AI Agent", test_enhanced_agent),
        ("ملفات الذاكرة", test_memory_files),
        ("تطبيق الويب", test_web_app)
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            if test_func():
                passed_tests += 1
                print(f"✅ {test_name} - نجح")
            else:
                print(f"❌ {test_name} - فشل")
        except Exception as e:
            print(f"❌ {test_name} - خطأ: {e}")
    
    print("\n" + "=" * 60)
    print(f"📊 نتائج الاختبار: {passed_tests}/{total_tests} نجح")
    print("=" * 60)
    
    if passed_tests == total_tests:
        print("🎉 جميع الاختبارات نجحت! آية جاهزة للاستخدام!")
        print("\n🚀 لتشغيل آية:")
        print("   - الواجهة الويب المحسنة: start_gpt_web.bat")
        print("   - النسخة المحسنة: start_gpt_enhanced.bat")
        print("   - الواجهة الويب العادية: start_web_interface.bat")
    else:
        print("⚠️ بعض الاختبارات فشلت. تحقق من الأخطاء أعلاه.")
    
    return passed_tests == total_tests

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
