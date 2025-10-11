@echo off
echo 🤖 بدء تشغيل AI Agent...
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ خطأ: Python غير مثبت أو غير موجود في PATH
    echo يرجى تثبيت Python من https://python.org
    pause
    exit /b 1
)

REM التحقق من وجود المتطلبات
if not exist "requirements.txt" (
    echo ❌ خطأ: ملف requirements.txt غير موجود
    pause
    exit /b 1
)

echo 📦 تثبيت المتطلبات...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ خطأ في تثبيت المتطلبات
    pause
    exit /b 1
)

echo.
echo ✅ تم تثبيت المتطلبات بنجاح!
echo.
echo 🌐 بدء تشغيل واجهة الويب...
echo افتح المتصفح وانتقل إلى: http://localhost:5000
echo اضغط Ctrl+C لإيقاف الخادم
echo.

python run.py --mode web

pause
