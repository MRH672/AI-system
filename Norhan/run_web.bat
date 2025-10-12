@echo off
chcp 65001 >nul
title نوران AI Agent - واجهة الويب

echo.
echo ================================================
echo    🌐 نوران AI Agent - واجهة الويب
echo ================================================
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ خطأ: Python غير مثبت على النظام
    echo يرجى تثبيت Python من: https://python.org
    pause
    exit /b 1
)

REM تثبيت المتطلبات
echo 📦 تثبيت المتطلبات...
pip install -r requirements.txt

echo.
echo 🚀 بدء تشغيل خادم الويب...
echo 📱 افتح المتصفح واذهب إلى: http://localhost:5000
echo ⏹️  اضغط Ctrl+C لإيقاف الخادم
echo.

REM تشغيل خادم الويب
python web_app.py

pause
