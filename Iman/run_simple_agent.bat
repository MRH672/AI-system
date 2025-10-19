@echo off
setlocal ENABLEDELAYEDEXPANSION

REM Determine script directory
set SCRIPT_DIR=%~dp0
pushd "%SCRIPT_DIR%"

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
        pause
        popd
        exit /b 1
    )
)

popd
endlocal
exit /b %ERRORLEVEL%


