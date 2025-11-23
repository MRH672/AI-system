@echo off
cd /d "%~dp0"
title Aya AI Agent - مساعد آية الذكي
color 0A

echo.
echo ========================================
echo    Aya - Intelligent AI Agent
echo    Enhanced AI Agent System
echo ========================================
echo.

REM التحقق من وجود Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ خطأ: Python غير مثبت أو غير موجود في PATH
    echo يرجى تثبيت Python 3.7 أو أحدث من: https://python.org
    echo.
    pause
    exit /b 1
)

echo ✅ Python موجود
echo.

echo 📋 الإصدارات المتاحة:
echo.
echo 1. GPT Enhanced Web Interface (موصى به) 🌟
echo    - واجهة ويب جميلة مع ردود بنمط ChatGPT
echo    - ذاكرة قوية وشخصية مميزة
echo    - إحصائيات مفصلة وميزات متقدمة
echo.
echo 2. GPT Enhanced Console Version
echo    - نسخة وحدة التحكم مع ردود بنمط ChatGPT
echo    - ذاكرة قوية وشخصية مميزة
echo.
echo 3. Enhanced Web Interface
echo    - واجهة ويب جميلة مع ذاكرة قوية
echo    - شخصية فريدة ومتطورة
echo.
echo 4. Enhanced Console Version
echo    - نسخة وحدة التحكم مع ذاكرة قوية
echo    - شخصية فريدة ومتطورة
echo.
echo 5. Enhanced Learning Agent
echo    - نسخة وحدة التحكم مع ذاكرة مستمرة
echo    - يتذكر كل شيء بين الجلسات
echo.
echo 6. Learning AI Agent (بسيط)
echo    - نسخة بسيطة للتعلم والاختبار
echo.
echo 7. Test All Features
echo    - اختبار شامل لجميع الإصدارات والميزات
echo.
echo 8. خروج
echo.
echo ========================================
echo.

:menu
set /p choice="اختر الإصدار الذي تريد تشغيله (1-8): "

if "%choice%"=="" (
    echo.
    echo ❌ لم تقم بإدخال اختيار. يرجى المحاولة مرة أخرى.
    echo.
    goto menu
)

if "%choice%"=="1" (
    echo.
    echo 🚀 بدء تشغيل GPT Enhanced Web Interface...
    echo 🌐 الواجهة ستكون متاحة على: http://localhost:5000
    echo.
    if exist "gpt_web_app.py" (
        start http://localhost:5000
        python gpt_web_app.py
    ) else (
        echo ❌ خطأ: ملف gpt_web_app.py غير موجود
        echo.
        pause
        goto menu
    )
) else if "%choice%"=="2" (
    echo.
    echo 🚀 بدء تشغيل GPT Enhanced Console Version...
    echo.
    if exist "gpt_enhanced_ai_agent.py" (
        python gpt_enhanced_ai_agent.py
    ) else (
        echo ❌ خطأ: ملف gpt_enhanced_ai_agent.py غير موجود
        echo.
        pause
        goto menu
    )
) else if "%choice%"=="3" (
    echo.
    echo 🚀 بدء تشغيل Enhanced Web Interface...
    echo 🌐 الواجهة ستكون متاحة على: http://localhost:5000
    echo.
    if exist "web_app.py" (
        start http://localhost:5000
        python web_app.py
    ) else (
        echo ❌ خطأ: ملف web_app.py غير موجود
        echo.
        pause
        goto menu
    )
) else if "%choice%"=="4" (
    echo.
    echo 🚀 بدء تشغيل Enhanced Console Version...
    echo.
    if exist "enhanced_ai_agent.py" (
        python enhanced_ai_agent.py
    ) else (
        echo ❌ خطأ: ملف enhanced_ai_agent.py غير موجود
        echo.
        pause
        goto menu
    )
) else if "%choice%"=="5" (
    echo.
    echo 🚀 بدء تشغيل Enhanced Learning Agent...
    echo.
    if exist "enhanced_learning_ai_agent.py" (
        python enhanced_learning_ai_agent.py
    ) else (
        echo ❌ خطأ: ملف enhanced_learning_ai_agent.py غير موجود
        echo.
        pause
        goto menu
    )
) else if "%choice%"=="6" (
    echo.
    echo 🚀 بدء تشغيل Learning AI Agent...
    echo.
    if exist "learning_ai_agent.py" (
        python learning_ai_agent.py
    ) else (
        echo ❌ خطأ: ملف learning_ai_agent.py غير موجود
        echo.
        pause
        goto menu
    )
) else if "%choice%"=="7" (
    echo.
    echo 🧪 بدء اختبار شامل لجميع الميزات...
    echo.
    if exist "test_all_features.py" (
        python test_all_features.py
    ) else (
        echo ❌ خطأ: ملف test_all_features.py غير موجود
        echo.
        pause
        goto menu
    )
) else if "%choice%"=="8" (
    echo.
    echo 👋 وداعاً! أتمنى لك يوماً رائعاً!
    echo.
    exit /b 0
) else (
    echo.
    echo ❌ اختيار غير صحيح. يرجى اختيار رقم من 1 إلى 8.
    echo.
    pause
    goto menu
)

echo.
echo ========================================
echo البرنامج تم إغلاقه.
echo ========================================
echo.
pause
