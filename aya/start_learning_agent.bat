@echo off
cd /d "%~dp0"
echo Starting Learning AI Agent - Aya...
echo This agent learns and remembers information!
echo.
echo Files will be saved in this directory:
echo - aya_memory.json (your information)
echo - aya_conversations.json (conversation history)
echo.
python learning_ai_agent.py
echo.
echo Agent has been stopped.
pause
