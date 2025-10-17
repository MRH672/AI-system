@echo off
setlocal

cd /d "%~dp0"

echo 📦 Installing requirements...
where pip >nul 2>nul
if errorlevel 1 (
    echo pip not found. Trying: py -m pip
    py -m pip install -r requirements.txt || goto :pipfail
) else (
    pip install -r requirements.txt || goto :pipfail
)

echo ✅ Starting web server on http://localhost:5000
start "SimpleAgent" http://localhost:5000

where python >nul 2>nul
if errorlevel 1 (
    echo Python not found. Trying: py
    py app.py
) else (
    python app.py
)
goto :eof

:pipfail
echo ❌ Failed to install requirements.
pause
exit /b 1


