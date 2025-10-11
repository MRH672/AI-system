#!/bin/bash

echo "🤖 بدء تشغيل AI Agent..."
echo

# التحقق من وجود Python
if ! command -v python3 &> /dev/null; then
    echo "❌ خطأ: Python3 غير مثبت"
    echo "يرجى تثبيت Python3 أولاً"
    exit 1
fi

# التحقق من وجود المتطلبات
if [ ! -f "requirements.txt" ]; then
    echo "❌ خطأ: ملف requirements.txt غير موجود"
    exit 1
fi

echo "📦 تثبيت المتطلبات..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ خطأ في تثبيت المتطلبات"
    exit 1
fi

echo
echo "✅ تم تثبيت المتطلبات بنجاح!"
echo
echo "🌐 بدء تشغيل واجهة الويب..."
echo "افتح المتصفح وانتقل إلى: http://localhost:5000"
echo "اضغط Ctrl+C لإيقاف الخادم"
echo

python3 run.py --mode web
