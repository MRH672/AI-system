@echo off
cd /d "%~dp0"
echo ========================================
echo    Reset Memory for Aya - AI Agent
echo ========================================
echo.
echo ⚠️ Warning: All saved information will be deleted!
echo.
echo 📋 Files that will be deleted:
echo    - aya_gpt_memory.json
echo    - aya_gpt_conversations.json
echo    - aya_gpt_personality.json
echo    - aya_enhanced_memory.json
echo    - aya_enhanced_conversations.json
echo    - aya_enhanced_personality.json
echo.
echo ========================================
echo.
set /p confirm="Are you sure you want to reset memory? (y/n): "

if /i "%confirm%"=="y" (
    echo.
    echo 🗑️ Starting to delete memory files...
    echo.
    
    if exist "aya_gpt_memory.json" (
        del "aya_gpt_memory.json"
        echo ✅ Deleted aya_gpt_memory.json
    ) else (
        echo ⚠️ aya_gpt_memory.json does not exist
    )
    
    if exist "aya_gpt_conversations.json" (
        del "aya_gpt_conversations.json"
        echo ✅ Deleted aya_gpt_conversations.json
    ) else (
        echo ⚠️ aya_gpt_conversations.json does not exist
    )
    
    if exist "aya_gpt_personality.json" (
        del "aya_gpt_personality.json"
        echo ✅ Deleted aya_gpt_personality.json
    ) else (
        echo ⚠️ aya_gpt_personality.json does not exist
    )
    
    if exist "aya_enhanced_memory.json" (
        del "aya_enhanced_memory.json"
        echo ✅ Deleted aya_enhanced_memory.json
    ) else (
        echo ⚠️ aya_enhanced_memory.json does not exist
    )
    
    if exist "aya_enhanced_conversations.json" (
        del "aya_enhanced_conversations.json"
        echo ✅ Deleted aya_enhanced_conversations.json
    ) else (
        echo ⚠️ aya_enhanced_conversations.json does not exist
    )
    
    if exist "aya_enhanced_personality.json" (
        del "aya_enhanced_personality.json"
        echo ✅ Deleted aya_enhanced_personality.json
    ) else (
        echo ⚠️ aya_enhanced_personality.json does not exist
    )
    
    echo.
    echo ✅ Memory reset successfully!
    echo.
    echo 🚀 You can now run Aya with fresh memory:
    echo    - Double-click START_HERE.bat
    echo    - Or use one of the available launcher files
) else (
    echo.
    echo ❌ Operation cancelled.
)

echo.
pause
