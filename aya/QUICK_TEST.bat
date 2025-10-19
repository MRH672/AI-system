@echo off
cd /d "%~dp0"
echo ========================================
echo    Quick Test for Aya - AI Agent
echo ========================================
echo.
echo 🧪 Starting comprehensive testing of all features...
echo.
python test_all_features.py
echo.
echo ========================================
echo.
if %errorlevel%==0 (
    echo 🎉 All tests passed! Aya is ready to use!
    echo.
    echo 🚀 To run Aya:
    echo    - Double-click START_HERE.bat
    echo    - Or use one of the available launcher files
) else (
    echo ⚠️ Some tests failed. Check the errors above.
)
echo.
pause
