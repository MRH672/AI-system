@echo off
echo ========================================
echo    Aya-Ali AI Agent - Setup and Run
echo ========================================
echo.
echo Installing required libraries...
pip install -r requirements.txt
echo.
echo Libraries installed successfully!
echo.
echo Choose running mode:
echo 1. Run Web Application (Recommended)
echo 2. Run Console Mode
echo.
set /p choice="Choose number (1 or 2): "

if "%choice%"=="1" (
    echo.
    echo Starting Web Application...
    echo You can access the app at: http://localhost:5000
    echo Press Ctrl+C to stop the program
    echo.
    python web_app.py
) else if "%choice%"=="2" (
    echo.
    echo Starting Console Mode...
    echo Press Ctrl+C to stop the program
    echo.
    python ai_agent.py
) else (
    echo.
    echo Invalid choice!
)

pause
