@echo off
cd /d "%~dp0"
echo ========================================
echo    Test Enhanced Learning AI Agent
echo ========================================
echo.
echo 🧪 Starting quick test for Enhanced Learning AI Agent...
echo.
python test_enhanced_learning.py
echo.
echo ========================================
echo.
if %errorlevel%==0 (
    echo 🎉 Enhanced Learning AI Agent test passed!
    echo.
    echo 🚀 To run the agent:
    echo    - Double-click QUICK_START_LEARNING.bat
    echo    - Or choose option 5 in START_HERE.bat
) else (
    echo ⚠️ Some tests failed. Check the errors above.
)
echo.
pause
