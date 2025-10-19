#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration file for Norhan AI Agent
"""

# Agent Configuration
AGENT_CONFIG = {
    "name_arabic": "نورهان",
    "name_english": "Norhan",
    "version": "1.0.0",
    "description": "AI Agent for user interaction in Arabic and English",
    "author": "Norhan"
}

# Response Configuration
RESPONSE_CONFIG = {
    "max_response_length": 200,
    "enable_memory": True,
    "enable_personalization": True,
    "conversation_threshold": 3  # Start personalizing after 3 conversations
}

# File Configuration
FILE_CONFIG = {
    "memory_file": "conversation_memory.json",
    "log_file": "agent_log.txt",
    "backup_interval": 10  # Save memory every 10 conversations
}

# Language Configuration
LANGUAGE_CONFIG = {
    "default_language": "arabic",
    "supported_languages": ["arabic", "english"],
    "auto_detect_language": True
}

# UI Configuration
UI_CONFIG = {
    "show_emojis": True,
    "show_timestamps": False,
    "show_conversation_count": True,
    "welcome_message": True
}

# Debug Configuration
DEBUG_CONFIG = {
    "debug_mode": False,
    "verbose_logging": False,
    "save_debug_logs": False
}
