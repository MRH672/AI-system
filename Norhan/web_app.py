#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Interface for AI Agent - واجهة ويب للوكيل الذكي
"""

from flask import Flask, render_template, request, jsonify
from ai_agent import AIAgent
import json
import os

app = Flask(__name__)
agent = AIAgent()

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """معالجة رسائل الدردشة"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'response': 'يرجى كتابة رسالة', 'error': True})
        
        # معالجة الرسالة
        response = agent.process_request(user_message)
        
        return jsonify({
            'response': response,
            'error': False,
            'timestamp': agent.conversation_history[-1]['timestamp'] if agent.conversation_history else None
        })
        
    except Exception as e:
        return jsonify({'response': f'حدث خطأ: {str(e)}', 'error': True})

@app.route('/capabilities')
def get_capabilities():
    """الحصول على قدرات الوكيل"""
    return jsonify({
        'capabilities': agent.capabilities,
        'name': agent.name,
        'version': agent.version
    })

@app.route('/history')
def get_history():
    """الحصول على تاريخ المحادثة"""
    return jsonify({
        'history': agent.conversation_history[-10:],  # آخر 10 رسائل
        'total': len(agent.conversation_history)
    })

@app.route('/save', methods=['POST'])
def save_conversation():
    """حفظ المحادثة"""
    try:
        result = agent.save_conversation()
        return jsonify({'message': result, 'success': True})
    except Exception as e:
        return jsonify({'message': f'خطأ في الحفظ: {str(e)}', 'success': False})

@app.route('/clear', methods=['POST'])
def clear_conversation():
    """مسح المحادثة"""
    try:
        agent.conversation_history = []
        return jsonify({'message': 'تم مسح المحادثة بنجاح', 'success': True})
    except Exception as e:
        return jsonify({'message': f'خطأ في المسح: {str(e)}', 'success': False})

if __name__ == '__main__':
    # إنشاء مجلد القوالب إذا لم يكن موجوداً
    os.makedirs('templates', exist_ok=True)
    
    print("🚀 بدء تشغيل نوران AI Agent...")
    print("📱 افتح المتصفح واذهب إلى: http://localhost:5000")
    print("⏹️  اضغط Ctrl+C لإيقاف الخادم")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
