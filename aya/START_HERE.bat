@echo off
cd /d "%~dp0"
echo ========================================
echo    Aya - Intelligent AI Agent
echo    Enhanced AI Agent System
echo ========================================
echo.
echo 🎉 Welcome to Aya's Intelligent System!
echo.
echo 📋 Available Versions:
echo.
echo 1. GPT Enhanced Web Interface (Recommended)
echo    - Beautiful web interface with ChatGPT-style responses
echo    - Strong memory and unique personality
echo    - Detailed statistics and advanced features
echo.
echo 2. GPT Enhanced Console Version
echo    - Console version with ChatGPT-style responses
echo    - Strong memory and unique personality
echo.
echo 3. Enhanced Web Interface
echo    - Beautiful web interface with strong memory
echo    - Unique and evolving personality
echo.
echo 4. Enhanced Console Version
echo    - Console version with strong memory
echo    - Unique and evolving personality
echo.
echo 5. Enhanced Learning Agent (NEW!)
echo    - Console version with persistent memory
echo    - Remembers everything between sessions
echo    - Perfect for learning and testing
echo.
echo 6. Test All Features
echo    - Comprehensive testing of all versions and features
echo.
echo ========================================
echo.
set /p choice="Choose the version you want to run (1-6): "

if "%choice%"=="1" (
    echo.
    echo 🚀 Starting GPT Enhanced Web Interface...
    echo 🌐 Interface will be available at: http://localhost:5000
    echo.
    python gpt_web_app.py
) else if "%choice%"=="2" (
    echo.
    echo 🚀 Starting GPT Enhanced Console Version...
    echo.
    python gpt_enhanced_ai_agent.py
) else if "%choice%"=="3" (
    echo.
    echo 🚀 Starting Enhanced Web Interface...
    echo 🌐 Interface will be available at: http://localhost:5000
    echo.
    python web_app.py
) else if "%choice%"=="4" (
    echo.
    echo 🚀 Starting Enhanced Console Version...
    echo.
    python enhanced_ai_agent.py
) else if "%choice%"=="5" (
    echo.
    echo 🚀 Starting Enhanced Learning Agent...
    echo.
    python enhanced_learning_ai_agent.py
) else if "%choice%"=="6" (
    echo.
    echo 🧪 Starting comprehensive testing of all features...
    echo.
    python test_all_features.py
) else (
    echo.
    echo ❌ Invalid choice. Please choose a number from 1 to 6.
    echo.
    pause
    goto :eof
)

echo.
echo Program has been closed.
pause
