#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify, session
import json
import datetime
import os
import uuid
from enhanced_ai_agent import EnhancedAIAgent

app = Flask(__name__)
app.secret_key = 'aya_enhanced_ai_secret_key_2024'

# إنشاء مجلد القوالب إذا لم يكن موجوداً
templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
os.makedirs(templates_dir, exist_ok=True)

# إنشاء مجلد الملفات الثابتة
static_dir = os.path.join(os.path.dirname(__file__), 'static')
os.makedirs(static_dir, exist_ok=True)

# إنشاء مجلد CSS
css_dir = os.path.join(static_dir, 'css')
os.makedirs(css_dir, exist_ok=True)

# إنشاء مجلد JS
js_dir = os.path.join(static_dir, 'js')
os.makedirs(js_dir, exist_ok=True)

# إنشاء مجلد الصور
images_dir = os.path.join(static_dir, 'images')
os.makedirs(images_dir, exist_ok=True)

# متغيرات عامة
agents = {}  # لتخزين الـ agents لكل جلسة

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """معالجة رسائل المحادثة"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'الرسالة فارغة'}), 400
        
        # إنشاء أو استرجاع الـ agent للجلسة الحالية
        session_id = session.get('session_id')
        if not session_id:
            session_id = str(uuid.uuid4())
            session['session_id'] = session_id
        
        if session_id not in agents:
            agents[session_id] = EnhancedAIAgent()
        
        agent = agents[session_id]
        
        # الحصول على الرد
        response = agent.get_enhanced_response(user_message)
        
        # حفظ المحادثة
        agent.save_conversation(user_message, response)
        agent.save_memory()
        agent.save_personality()
        
        # إرجاع الرد
        return jsonify({
            'response': response,
            'user_name': agent.user_name,
            'conversation_count': agent.conversation_count,
            'relationship_level': agent.user_info.get('relationship_level', 'جديد'),
            'timestamp': datetime.datetime.now().strftime('%H:%M')
        })
        
    except Exception as e:
        return jsonify({'error': f'خطأ في معالجة الرسالة: {str(e)}'}), 500

@app.route('/memory', methods=['GET'])
def get_memory():
    """الحصول على معلومات الذاكرة"""
    try:
        session_id = session.get('session_id')
        if not session_id or session_id not in agents:
            return jsonify({'error': 'لا توجد جلسة نشطة'}), 400
        
        agent = agents[session_id]
        
        return jsonify({
            'user_info': agent.user_info,
            'conversation_count': agent.conversation_count,
            'relationship_level': agent.user_info.get('relationship_level', 'جديد'),
            'personality': agent.personality
        })
        
    except Exception as e:
        return jsonify({'error': f'خطأ في الحصول على الذاكرة: {str(e)}'}), 500

@app.route('/reset', methods=['POST'])
def reset_memory():
    """إعادة تعيين الذاكرة"""
    try:
        session_id = session.get('session_id')
        if session_id and session_id in agents:
            del agents[session_id]
        
        # إنشاء جلسة جديدة
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
        agents[session_id] = EnhancedAIAgent()
        
        return jsonify({'message': 'تم إعادة تعيين الذاكرة بنجاح'})
        
    except Exception as e:
        return jsonify({'error': f'خطأ في إعادة تعيين الذاكرة: {str(e)}'}), 500

@app.route('/conversations', methods=['GET'])
def get_conversations():
    """الحصول على تاريخ المحادثات"""
    try:
        session_id = session.get('session_id')
        if not session_id or session_id not in agents:
            return jsonify({'error': 'لا توجد جلسة نشطة'}), 400
        
        agent = agents[session_id]
        
        # تحميل المحادثات من الملف
        conversations = []
        if os.path.exists(agent.conversation_file):
            with open(agent.conversation_file, 'r', encoding='utf-8') as f:
                conversations = json.load(f)
        
        # إرجاع آخر 50 محادثة فقط
        return jsonify({'conversations': conversations[-50:]})
        
    except Exception as e:
        return jsonify({'error': f'خطأ في الحصول على المحادثات: {str(e)}'}), 500

if __name__ == '__main__':
    print("🚀 بدء تشغيل Enhanced AI Agent Web Interface...")
    print("🌐 الواجهة متاحة على: http://localhost:5000")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)
