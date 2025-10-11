#!/usr/bin/env python3
"""
ملف تشغيل AI Agent
يمكن تشغيل الـ Agent في وضعين:
1. وضع سطر الأوامر (CLI)
2. وضع واجهة الويب
"""

import sys
import os
import argparse

# إضافة مجلد src إلى المسار
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ai_agent import AIAgent

def run_cli():
    """تشغيل الـ Agent في وضع سطر الأوامر"""
    print("🤖 مرحباً! أنا AI Agent أتعلم من تفاعلي معك.")
    print("اكتب 'exit' للخروج، 'stats' لرؤية الإحصائيات، 'reset' لإعادة تعيين الذاكرة")
    print("-" * 60)
    
    agent = AIAgent()
    
    while True:
        try:
            user_input = input("\nأنت: ").strip()
            
            if user_input.lower() == 'exit':
                print("شكراً لك! وداعاً!")
                break
            elif user_input.lower() == 'stats':
                stats = agent.get_learning_stats()
                print(f"\n📊 إحصائيات التعلم:")
                print(f"• عدد المحادثات: {stats['total_conversations']}")
                print(f"• الأنماط المتعلمة: {stats['learned_patterns']}")
                print(f"• تفضيلات المستخدم: {stats['user_preferences']}")
                print(f"• المواضيع الأخيرة: {', '.join(stats['recent_topics'])}")
                print(f"• توزيع المشاعر:")
                print(f"  - إيجابي: {stats['sentiment_distribution']['positive']}")
                print(f"  - سلبي: {stats['sentiment_distribution']['negative']}")
                print(f"  - محايد: {stats['sentiment_distribution']['neutral']}")
                continue
            elif user_input.lower() == 'reset':
                confirm = input("هل أنت متأكد من إعادة تعيين الذاكرة؟ (y/n): ").strip().lower()
                if confirm == 'y':
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
                
        except KeyboardInterrupt:
            print("\n\nتم إيقاف البرنامج بواسطة المستخدم.")
            break
        except Exception as e:
            print(f"\nحدث خطأ: {e}")

def run_web():
    """تشغيل الـ Agent في وضع واجهة الويب"""
    try:
        from app import app
        print("🌐 بدء تشغيل واجهة الويب...")
        print("افتح المتصفح وانتقل إلى: http://localhost:5000")
        print("اضغط Ctrl+C لإيقاف الخادم")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except ImportError:
        print("❌ خطأ: Flask غير مثبت. قم بتثبيت المتطلبات أولاً:")
        print("pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ خطأ في تشغيل واجهة الويب: {e}")

def main():
    parser = argparse.ArgumentParser(description='AI Agent - الذكي الذي يتعلم')
    parser.add_argument('--mode', choices=['cli', 'web'], default='web',
                       help='وضع التشغيل: cli (سطر الأوامر) أو web (واجهة الويب)')
    
    args = parser.parse_args()
    
    if args.mode == 'cli':
        run_cli()
    else:
        run_web()

if __name__ == "__main__":
    main()
