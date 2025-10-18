from flask import Flask, render_template, request, jsonify
from ai_agent import SimpleAIAgent
import json

app = Flask(__name__)
agent = SimpleAIAgent()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Process chat messages"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message is empty'}), 400
        
        # Generate response from agent
        response = agent.generate_response(user_message)
        
        return jsonify({
            'response': response,
            'timestamp': agent.conversations[-1]['timestamp'] if agent.conversations else None
        })
        
    except Exception as e:
        return jsonify({'error': f'Processing error: {str(e)}'}), 500

@app.route('/stats')
def stats():
    """Get conversation statistics"""
    try:
        stats = agent.get_conversation_stats()
        return jsonify({'stats': stats})
    except Exception as e:
        return jsonify({'error': f'Error fetching stats: {str(e)}'}), 500

@app.route('/clear')
def clear_conversations():
    """Clear conversation history"""
    try:
        agent.conversations = []
        agent.save_conversations()
        return jsonify({'message': 'Conversations cleared successfully'})
    except Exception as e:
        return jsonify({'error': f'Error clearing conversations: {str(e)}'}), 500

if __name__ == '__main__':
    print("🚀 Starting Aya-Ali AI Agent...")
    print("📱 You can access the app at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
