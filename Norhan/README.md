# نورهان AI Agent - Norhan's Interactive Assistant 🤖

A friendly AI agent that can interact with users in both Arabic and English with a personalized touch.

## Features ✨

- 🌍 **Bilingual Support**: Full Arabic and English language support
- 🧠 **Smart Memory**: Remembers conversation history and becomes more personal over time
- 😊 **Friendly Personality**: Warm and engaging responses with emojis
- 🎭 **Multiple Response Types**: Greetings, jokes, help, time, date, and more
- 🔄 **Conversation Memory**: Gets more friendly and personalized after multiple interactions
- 📊 **Statistics**: Track conversation history and engagement

## Supported Interactions 📝

### Arabic (العربية)
- **تحيات**: أهلاً، مرحباً، السلام عليكم
- **السؤال عن الحال**: كيف حالك؟ كيف ألأحوال؟
- **المساعدة**: ساعدني، أحتاج مساعدة
- **الوداع**: وداعاً، مع السلامة، إلى اللقاء
- **النكات**: نكتة، اضحك، نكت
- **المجاملة**: جميل، رائع، ممتاز
- **الاسم**: ما اسمك؟ من أنت؟
- **الوقت**: كم الساعة؟ ما الوقت؟
- **التاريخ**: ما التاريخ؟ اليوم إيه؟

### English
- **Greetings**: hello, hi, hey, good morning
- **How are you**: how are you, how do you do
- **Help**: help, assist, support
- **Farewell**: bye, goodbye, see you
- **Jokes**: joke, funny, tell me a joke
- **Compliments**: beautiful, awesome, great
- **Name**: what's your name, who are you
- **Time**: time, clock, what time
- **Date**: date, today, what date

## How to Run 🚀

### Easy Way - Batch File (Windows)
Double-click `start_norhan.bat` or run:
```batch
start_norhan.bat
```

### Command Line
```bash
python ai_agent.py
```

### Python 3 Required
Make sure you have Python 3.6 or higher installed.

## Example Conversations 💬

### Arabic Example
```
👤 You: أهلاً نورهان
🤖 نورهان: أهلاً وسهلاً! أنا نورهان، مسرورة بلقائك! 🌟

👤 You: كيف حالك؟
🤖 نورهان: أنا بخير، شكراً لك! سعيد لأني أتحدث معك 🌸

👤 You: احكيلي نكتة
🤖 نورهان: لماذا لا تذهب الأسماك إلى المدرسة؟ لأنها تسبح في الماء! 🐟
```

### English Example
```
👤 You: Hello Norhan
🤖 نورهان: Hello there! I'm Norhan, nice to meet you! 🌟

👤 You: How are you?
🤖 نورهان: I'm doing great, thank you! Happy to be talking with you! 🌸

👤 You: Tell me a joke
🤖 نورهان: Why don't fish go to school? Because they're already swimming in water! 🐟
```

## Special Commands 🔧

- `exit` or `quit` - End the conversation
- `stats` or `إحصائيات` - Show conversation statistics
- `bye` or `وداعاً` - Say goodbye

## Files Structure 📁

```
Norhan/
├── ai_agent.py          # Main AI agent file
├── config.py            # Configuration settings
├── requirements.txt     # Dependencies (none required!)
├── start_norhan.bat     # Easy startup for Windows
├── README.md            # This file
├── conversation_memory.json  # Conversation history (auto-created)
└── agent_log.txt        # Debug logs (if enabled)
```

## Memory & Personalization 🧠

The agent automatically:
- Saves conversation history to `conversation_memory.json`
- Becomes more personal after 3+ conversations
- Remembers your interaction patterns
- Provides personalized greetings and responses

## Customization ⚙️

Edit `config.py` to customize:
- Agent name and personality
- Response behavior
- Language settings
- UI preferences
- Debug options

## Technical Details 🔧

- **Language**: Python 3.6+
- **Dependencies**: None (uses only standard library)
- **Encoding**: UTF-8 (full Unicode support)
- **Memory**: JSON-based persistent storage
- **Platform**: Cross-platform (Windows, Mac, Linux)

## Troubleshooting 🛠️

### Common Issues:

1. **Arabic text not displaying properly**
   - Make sure your terminal supports UTF-8
   - Use Windows Terminal or PowerShell for best results

2. **Python not found**
   - Install Python 3.6+ from python.org
   - Make sure Python is in your PATH

3. **Permission errors**
   - Run as administrator if needed
   - Check file permissions in the Norhan folder

### Getting Help:
- Check the console for error messages
- Ensure all files are in the same directory
- Try running `python --version` to verify Python installation

## Future Enhancements 🚀

Planned features:
- Voice interaction support
- Web interface
- More languages
- Advanced AI capabilities
- Integration with external APIs

## Notes 📝

- Type 'exit' or 'quit' to end the conversation
- The agent gets more expressive and personal over time
- All responses are contextually appropriate
- Memory persists between sessions
- Easy to extend with new response types

Enjoy chatting with Norhan! 🤖✨

---

*Created with ❤️ for interactive AI experiences*
