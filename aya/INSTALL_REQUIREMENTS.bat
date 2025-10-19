@echo off
cd /d "%~dp0"
echo ========================================
echo    Install Requirements for Aya - AI Agent
echo ========================================
echo.
echo 📦 Starting requirements installation...
echo.
echo 📋 Requirements:
echo    Flask==2.3.3
echo    requests==2.31.0
echo    Werkzeug==2.3.7
echo    Jinja2==3.1.2
echo    MarkupSafe==2.1.3
echo    itsdangerous==2.1.2
echo    click==8.1.7
echo    blinker==1.6.3
echo.
echo ========================================
echo.
pip install -r requirements.txt
echo.
echo ========================================
echo.
if %errorlevel%==0 (
    echo ✅ Requirements installed successfully!
    echo.
    echo 🚀 You can now run Aya:
    echo    - Double-click START_HERE.bat
    echo    - Or use one of the available launcher files
) else (
    echo ❌ Error installing requirements.
    echo.
    echo 🔧 Try the following solutions:
    echo    1. Make sure Python is installed
    echo    2. Make sure Python is added to PATH
    echo    3. Try: python -m pip install --upgrade pip
    echo    4. Try: pip install --user -r requirements.txt
)
echo.
pause
