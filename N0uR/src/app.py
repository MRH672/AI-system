"""
خادم Flask لواجهة الويب
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from .ai_agent import AIAgent
import json

app = Flask(__name__)
CORS(app)

# إنشاء instance من AI Agent
agent = AIAgent()

@app.route('/')
def index():
    """الصفحة الرئيسية"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """API endpoint للدردشة مع الـ Agent"""
    try:
        data = request.get_json()
        user_input = data.get('message', '').strip()
        feedback = data.get('feedback', '').strip()
        
        if not user_input:
            return jsonify({'error': 'الرسالة فارغة'}), 400
        
        # التفاعل مع الـ Agent
        response = agent.interact(user_input, feedback)
        
        # الحصول على إحصائيات التعلم
        stats = agent.get_learning_stats()
        
        return jsonify({
            'response': response,
            'stats': stats,
            'success': True
        })
        
    except Exception as e:
        return jsonify({'error': f'خطأ في المعالجة: {str(e)}'}), 500

@app.route('/stats', methods=['GET'])
def get_stats():
    """API endpoint للحصول على إحصائيات التعلم"""
    try:
        stats = agent.get_learning_stats()
        return jsonify({
            'stats': stats,
            'success': True
        })
    except Exception as e:
        return jsonify({'error': f'خطأ في الحصول على الإحصائيات: {str(e)}'}), 500

@app.route('/reset', methods=['POST'])
def reset_memory():
    """API endpoint لإعادة تعيين الذاكرة"""
    try:
        agent.reset_memory()
        return jsonify({
            'message': 'تم إعادة تعيين الذاكرة بنجاح',
            'success': True
        })
    except Exception as e:
        return jsonify({'error': f'خطأ في إعادة تعيين الذاكرة: {str(e)}'}), 500

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """API endpoint لإرسال ردود الفعل"""
    try:
        data = request.get_json()
        user_input = data.get('user_input', '')
        agent_response = data.get('agent_response', '')
        feedback = data.get('feedback', '')
        
        if not all([user_input, agent_response, feedback]):
            return jsonify({'error': 'بيانات ناقصة'}), 400
        
        # التعلم من ردود الفعل
        agent._learn_from_feedback(user_input, agent_response, feedback)
        
        return jsonify({
            'message': 'تم حفظ ردود الفعل بنجاح',
            'success': True
        })
        
    except Exception as e:
        return jsonify({'error': f'خطأ في حفظ ردود الفعل: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
