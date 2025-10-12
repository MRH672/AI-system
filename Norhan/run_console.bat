@echo off
chcp 65001 >nul
title نوران AI Agent - واجهة سطر الأوامر

echo.
echo ================================================
echo    🤖 نوران AI Agent - مساعد ذكي صغير
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
echo 🚀 بدء تشغيل نوران AI Agent...
echo.

REM تشغيل الوكيل
python ai_agent.py

pause
