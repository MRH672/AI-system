@echo off
setlocal ENABLEDELAYEDEXPANSION
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

REM Determine script directory
set SCRIPT_DIR=%~dp0
pushd "%SCRIPT_DIR%"

echo ========================================
echo    AI Agent Interactive - إيمان
echo    AI Agent متفاعل يتعلم ويتذكر
echo ========================================
echo.

REM Prefer python if on PATH
where python >nul 2>nul
if %ERRORLEVEL%==0 (
    python "%SCRIPT_DIR%simple_agent.py"
) else (
    where py >nul 2>nul
    if %ERRORLEVEL%==0 (
        py "%SCRIPT_DIR%simple_agent.py"
    ) else (
        echo Python is not installed or not on PATH.
        echo Please install Python 3.8+ from https://www.python.org/downloads/
        echo.
        pause
        popd
        exit /b 1
    )
)

echo.
echo تم إغلاق البرنامج. اضغط أي مفتاح للخروج...
pause >nul
popd

