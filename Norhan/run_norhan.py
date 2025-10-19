#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick runner for Norhan AI Agent
This file provides an easy way to run the agent
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from ai_agent import main
    print("Starting Norhan AI Agent...")
    main()
except ImportError as e:
    print(f"Error importing AI agent: {e}")
    print("Make sure ai_agent.py is in the same directory")
except Exception as e:
    print(f"Error running agent: {e}")
