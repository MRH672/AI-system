#!/usr/bin/env python3
"""
ملف تشغيل AI Agent مع واجهة تفاعلية
"""

import sys
import os
import subprocess
import webbrowser
import time
import threading

# إضافة مجلد src إلى المسار
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

def check_dependencies():
    """التحقق من المتطلبات"""
    print("🔍 التحقق من المتطلبات...")
    
    required_packages = ['flask', 'numpy', 'scikit-learn', 'nltk']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ المتطلبات الناقصة: {', '.join(missing_packages)}")
        print("📦 تثبيت المتطلبات...")
        
        try:
            requirements_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])
            print("✅ تم تثبيت المتطلبات بنجاح!")
        except subprocess.CalledProcessError:
            print("❌ فشل في تثبيت المتطلبات")
            return False
    
    return True

def download_nltk_data():
    """تحميل بيانات NLTK المطلوبة"""
    print("📚 تحميل بيانات NLTK...")
    
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✅ تم تحميل بيانات NLTK بنجاح!")
    except Exception as e:
        print(f"⚠️ تحذير: لم يتم تحميل بيانات NLTK: {e}")

def open_browser():
    """فتح المتصفح بعد تأخير قصير"""
    time.sleep(3)
    webbrowser.open('http://localhost:5000')

def main():
    """الدالة الرئيسية"""
    print("🤖 AI Agent - الذكي الذي يتعلم")
    print("=" * 50)
    print()
    
    # التحقق من المتطلبات
    if not check_dependencies():
        print("❌ لا يمكن المتابعة بدون المتطلبات")
        input("اضغط Enter للخروج...")
        return
    
    # تحميل بيانات NLTK
    download_nltk_data()
    
    print()
    print("🌐 بدء تشغيل واجهة الويب...")
    print("📱 سيتم فتح المتصفح تلقائياً خلال 3 ثوانٍ")
    print("🔗 أو انتقل يدوياً إلى: http://localhost:5000")
    print()
    print("⏹️ اضغط Ctrl+C لإيقاف الخادم")
    print("-" * 50)
    
    # فتح المتصفح في thread منفصل
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    try:
        # تشغيل الخادم
        from app import app
        app.run(debug=False, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n\n👋 تم إيقاف الخادم بواسطة المستخدم")
    except Exception as e:
        print(f"\n❌ خطأ في تشغيل الخادم: {e}")
        input("اضغط Enter للخروج...")

if __name__ == "__main__":
    main()
