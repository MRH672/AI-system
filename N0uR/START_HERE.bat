@echo off
title AI Agent - الذكي الذي يتعلم
color 0A

echo.
echo  █████╗ ██╗    ███████╗██╗ ██████╗ ███████╗███╗   ██╗████████╗
echo ██╔══██╗██║    ██╔════╝██║██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝
echo ███████║██║    █████╗  ██║██║  ███╗█████╗  ██╔██╗ ██║   ██║   
echo ██╔══██║██║    ██╔══╝  ██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   
echo ██║  ██║██║    ██║     ██║╚██████╔╝███████╗██║ ╚████║   ██║   
echo ╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   
echo.
echo                    الذكي الذي يتعلم من كل تفاعل
echo.
echo ================================================================
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ خطأ: Python غير مثبت أو غير موجود في PATH
    echo.
    echo يرجى تثبيت Python من: https://python.org
    echo تأكد من تحديد "Add Python to PATH" أثناء التثبيت
    echo.
    pause
    exit /b 1
)

echo ✅ Python مثبت بنجاح
echo.

REM التحقق من وجود الملفات المطلوبة
if not exist "ai_agent.py" (
    echo ❌ خطأ: ملف ai_agent.py غير موجود
    pause
    exit /b 1
)

if not exist "app.py" (
    echo ❌ خطأ: ملف app.py غير موجود
    pause
    exit /b 1
)

echo ✅ الملفات المطلوبة موجودة
echo.

echo 🚀 بدء تشغيل AI Agent...
echo.
echo 📱 سيتم فتح المتصفح تلقائياً
echo 🌐 أو انتقل يدوياً إلى: http://localhost:5000
echo.
echo ⏹️ اضغط Ctrl+C لإيقاف الخادم
echo.

REM تشغيل AI Agent
python scripts\launch.py

echo.
echo 👋 شكراً لك لاستخدام AI Agent!
pause
