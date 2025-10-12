@echo off
chcp 65001 >nul
title نوران AI Agent - البداية هنا

echo.
echo ================================================
echo    🎯 نوران AI Agent - البداية هنا
echo ================================================
echo.
echo اختر طريقة التشغيل:
echo.
echo 1. واجهة سطر الأوامر (Console)
echo 2. واجهة الويب (Web Interface)
echo 3. خروج
echo.

set /p choice="اختر رقم (1-3): "

if "%choice%"=="1" (
    echo.
    echo 🚀 تشغيل واجهة سطر الأوامر...
    call run_console.bat
) else if "%choice%"=="2" (
    echo.
    echo 🌐 تشغيل واجهة الويب...
    call run_web.bat
) else if "%choice%"=="3" (
    echo.
    echo 👋 وداعاً!
    exit /b 0
) else (
    echo.
    echo ❌ اختيار غير صحيح. حاول مرة أخرى.
    pause
    goto :eof
)

pause
