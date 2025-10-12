# Simple AI Agent 🤖

A simple conversational AI agent built with Python that can respond to user input in both Arabic and English.

## Features

- **Multilingual Support**: Responds in Arabic and English
- **Conversation History**: Keeps track of all conversations
- **Interactive Mode**: Command-line interface for easy interaction
- **Statistics**: View conversation stats and agent information
- **Simple Commands**: Built-in help, stats, and clear commands

## Quick Start

### 1. Run the Agent
```bash
python ai_agent.py
```

### 2. Available Commands
- `help` - Show available commands
- `stats` - Display conversation statistics
- `clear` - Clear conversation history
- `exit` or `quit` - Exit the program

### 3. Example Conversation
```
أنت: مرحبا
Simple AI Agent: مرحباً! كيف يمكنني مساعدتك اليوم؟

أنت: ما اسمك؟
Simple AI Agent: أنا Simple AI Agent - نسخة 1.0.0

أنت: كيف حالك؟
Simple AI Agent: أنا بخير، شكراً لك! كيف حالك أنت؟
```

## Code Structure

- `SimpleAIAgent` class: Main agent class
- `process_input()`: Processes user input and generates responses
- `get_conversation_history()`: Returns conversation history
- `get_stats()`: Returns agent statistics

## Customization

You can easily customize the agent by:
1. Adding new response patterns in the `responses` dictionary
2. Modifying the keyword matching logic in `process_input()`
3. Adding new features to the agent class

## Requirements

No external dependencies required! The agent uses only Python standard library.

## License

This is a simple educational project. Feel free to use and modify as needed.
