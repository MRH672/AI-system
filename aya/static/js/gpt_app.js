// GPT Enhanced AI Agent - JavaScript Application

class GPTEnhancedAIAgentApp {
    constructor() {
        this.isTyping = false;
        this.messageHistory = [];
        this.currentSession = null;
        this.settings = {
            theme: 'light',
            fontSize: 'medium',
            soundEnabled: true,
            gptModeEnabled: true
        };
        
        this.init();
    }
    
    init() {
        this.loadSettings();
        this.bindEvents();
        this.setupTheme();
        this.setupFontSize();
        this.loadMemory();
        this.showWelcomeMessage();
    }
    
    bindEvents() {
        // Message input events
        const messageInput = document.getElementById('messageInput');
        const sendBtn = document.getElementById('sendBtn');
        
        messageInput.addEventListener('input', () => {
            this.handleInputChange();
            this.updateCharCount();
        });
        
        messageInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
        
        sendBtn.addEventListener('click', () => {
            this.sendMessage();
        });
        
        // Header button events
        document.getElementById('memoryBtn').addEventListener('click', () => {
            this.showMemoryModal();
        });
        
        document.getElementById('statsBtn').addEventListener('click', () => {
            this.showStatsModal();
        });
        
        document.getElementById('personalityBtn').addEventListener('click', () => {
            this.showPersonalityModal();
        });
        
        document.getElementById('resetBtn').addEventListener('click', () => {
            this.resetMemory();
        });
        
        document.getElementById('settingsBtn').addEventListener('click', () => {
            this.showSettingsModal();
        });
        
        // Quick action buttons
        document.querySelectorAll('.quick-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const message = e.target.getAttribute('data-message');
                messageInput.value = message;
                this.handleInputChange();
                this.sendMessage();
            });
        });
        
        // Modal events
        document.querySelectorAll('.modal-close').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.closeModal(e.target.closest('.modal'));
            });
        });
        
        document.querySelectorAll('.modal').forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    this.closeModal(modal);
                }
            });
        });
        
        // Settings events
        document.getElementById('themeSelect').addEventListener('change', (e) => {
            this.changeTheme(e.target.value);
        });
        
        document.getElementById('fontSizeSelect').addEventListener('change', (e) => {
            this.changeFontSize(e.target.value);
        });
        
        document.getElementById('soundToggle').addEventListener('change', (e) => {
            this.toggleSound(e.target.checked);
        });
        
        document.getElementById('gptModeToggle').addEventListener('change', (e) => {
            this.toggleGPTMode(e.target.checked);
        });
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey || e.metaKey) {
                switch(e.key) {
                    case 'k':
                        e.preventDefault();
                        messageInput.focus();
                        break;
                    case 'r':
                        e.preventDefault();
                        this.resetMemory();
                        break;
                    case 'm':
                        e.preventDefault();
                        this.showMemoryModal();
                        break;
                    case 's':
                        e.preventDefault();
                        this.showStatsModal();
                        break;
                    case 'p':
                        e.preventDefault();
                        this.showPersonalityModal();
                        break;
                }
            }
        });
    }
    
    handleInputChange() {
        const messageInput = document.getElementById('messageInput');
        const sendBtn = document.getElementById('sendBtn');
        
        // Auto-resize textarea
        messageInput.style.height = 'auto';
        messageInput.style.height = Math.min(messageInput.scrollHeight, 120) + 'px';
        
        // Enable/disable send button
        const hasText = messageInput.value.trim().length > 0;
        sendBtn.disabled = !hasText;
        
        if (hasText) {
            sendBtn.style.opacity = '1';
        } else {
            sendBtn.style.opacity = '0.5';
        }
    }
    
    updateCharCount() {
        const messageInput = document.getElementById('messageInput');
        const charCount = document.getElementById('charCount');
        const count = messageInput.value.length;
        const maxLength = 1000;
        
        charCount.textContent = `${count}/${maxLength}`;
        
        if (count > maxLength * 0.9) {
            charCount.style.color = 'var(--warning-color)';
        } else if (count > maxLength * 0.8) {
            charCount.style.color = 'var(--accent-color)';
        } else {
            charCount.style.color = 'var(--text-light)';
        }
    }
    
    async sendMessage() {
        const messageInput = document.getElementById('messageInput');
        const message = messageInput.value.trim();
        
        if (!message || this.isTyping) return;
        
        // Clear input and reset
        messageInput.value = '';
        this.handleInputChange();
        
        // Add user message to chat
        this.addMessage(message, 'user');
        
        // Show typing indicator
        this.showTypingIndicator();
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                // Hide typing indicator
                this.hideTypingIndicator();
                
                // Add AI response to chat
                this.addMessage(data.response, 'ai', {
                    user_name: data.user_name,
                    conversation_count: data.conversation_count,
                    relationship_level: data.relationship_level,
                    timestamp: data.timestamp,
                    response_type: data.response_type
                });
                
                // Play sound if enabled
                if (this.settings.soundEnabled) {
                    this.playNotificationSound();
                }
                
                // Update memory info
                this.updateMemoryInfo(data);
                
            } else {
                throw new Error(data.error || 'خطأ في إرسال الرسالة');
            }
            
        } catch (error) {
            console.error('Error sending message:', error);
            this.hideTypingIndicator();
            this.addMessage('آسفة، حدث خطأ في معالجة رسالتك. حاول مرة أخرى.', 'ai');
            this.showNotification('خطأ في إرسال الرسالة', 'error');
        }
    }
    
    addMessage(content, sender, metadata = {}) {
        const chatMessages = document.getElementById('chatMessages');
        
        // Remove welcome message if it exists
        const welcomeMessage = chatMessages.querySelector('.welcome-message');
        if (welcomeMessage) {
            welcomeMessage.remove();
        }
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = sender === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';
        
        const messageContent = document.createElement('div');
        messageContent.className = 'message-content';
        messageContent.innerHTML = this.formatMessage(content);
        
        const messageTime = document.createElement('div');
        messageTime.className = 'message-time';
        messageTime.textContent = metadata.timestamp || new Date().toLocaleTimeString('ar-SA', {
            hour: '2-digit',
            minute: '2-digit'
        });
        
        messageContent.appendChild(messageTime);
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(messageContent);
        
        chatMessages.appendChild(messageDiv);
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        // Store in history
        this.messageHistory.push({
            content,
            sender,
            timestamp: new Date().toISOString(),
            metadata
        });
    }
    
    formatMessage(content) {
        // Convert URLs to links
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        content = content.replace(urlRegex, '<a href="$1" target="_blank" rel="noopener">$1</a>');
        
        // Convert line breaks
        content = content.replace(/\n/g, '<br>');
        
        // Add emoji support
        const emojiRegex = /:([a-z_]+):/g;
        content = content.replace(emojiRegex, (match, emoji) => {
            const emojiMap = {
                'smile': '😊',
                'heart': '❤️',
                'star': '⭐',
                'thumbsup': '👍',
                'fire': '🔥',
                'rocket': '🚀',
                'brain': '🧠',
                'robot': '🤖',
                'gpt': '🚀'
            };
            return emojiMap[emoji] || match;
        });
        
        return content;
    }
    
    showTypingIndicator() {
        const typingIndicator = document.getElementById('typingIndicator');
        typingIndicator.style.display = 'flex';
        
        const chatMessages = document.getElementById('chatMessages');
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        this.isTyping = true;
    }
    
    hideTypingIndicator() {
        const typingIndicator = document.getElementById('typingIndicator');
        typingIndicator.style.display = 'none';
        this.isTyping = false;
    }
    
    showWelcomeMessage() {
        const chatMessages = document.getElementById('chatMessages');
        const welcomeMessage = chatMessages.querySelector('.welcome-message');
        
        if (!welcomeMessage && this.messageHistory.length === 0) {
            // Welcome message is already in HTML, just make sure it's visible
            chatMessages.scrollTop = 0;
        }
    }
    
    async loadMemory() {
        try {
            const response = await fetch('/memory');
            const data = await response.json();
            
            if (response.ok) {
                this.updateMemoryInfo(data);
            }
        } catch (error) {
            console.error('Error loading memory:', error);
        }
    }
    
    updateMemoryInfo(data) {
        // Update conversation count
        const conversationCount = document.getElementById('conversationCount');
        if (conversationCount) {
            conversationCount.textContent = data.conversation_count || 0;
        }
        
        // Update relationship level
        const relationshipLevel = document.getElementById('relationshipLevel');
        if (relationshipLevel) {
            relationshipLevel.textContent = data.relationship_level || 'جديد';
        }
        
        // Update user memory info
        const userMemoryInfo = document.getElementById('userMemoryInfo');
        if (userMemoryInfo && data.user_info) {
            this.displayUserInfo(userMemoryInfo, data.user_info);
        }
    }
    
    displayUserInfo(container, userInfo) {
        if (!userInfo.name && !userInfo.age && !userInfo.location && !userInfo.interests?.length) {
            container.innerHTML = '<p>لا توجد معلومات محفوظة بعد</p>';
            return;
        }
        
        let html = '<div class="user-info-grid">';
        
        if (userInfo.name) {
            html += `<div class="info-item"><strong>الاسم:</strong> ${userInfo.name}</div>`;
        }
        
        if (userInfo.age) {
            html += `<div class="info-item"><strong>العمر:</strong> ${userInfo.age} سنة</div>`;
        }
        
        if (userInfo.location) {
            html += `<div class="info-item"><strong>الموقع:</strong> ${userInfo.location}</div>`;
        }
        
        if (userInfo.profession) {
            html += `<div class="info-item"><strong>المهنة:</strong> ${userInfo.profession}</div>`;
        }
        
        if (userInfo.favorite_color) {
            html += `<div class="info-item"><strong>اللون المفضل:</strong> ${userInfo.favorite_color}</div>`;
        }
        
        if (userInfo.interests && userInfo.interests.length > 0) {
            html += `<div class="info-item"><strong>الاهتمامات:</strong> ${userInfo.interests.join(', ')}</div>`;
        }
        
        html += '</div>';
        container.innerHTML = html;
    }
    
    async loadStats() {
        try {
            const response = await fetch('/stats');
            const data = await response.json();
            
            if (response.ok) {
                this.updateStatsDisplay(data);
            }
        } catch (error) {
            console.error('Error loading stats:', error);
        }
    }
    
    updateStatsDisplay(data) {
        // Update stats cards
        const totalConversations = document.getElementById('totalConversations');
        if (totalConversations) {
            totalConversations.textContent = data.total_conversations || 0;
        }
        
        const topicsCount = document.getElementById('topicsCount');
        if (topicsCount) {
            topicsCount.textContent = data.topics_count || 0;
        }
        
        const positiveSentiments = document.getElementById('positiveSentiments');
        if (positiveSentiments) {
            positiveSentiments.textContent = data.sentiments?.إيجابي || 0;
        }
        
        const relationshipLevel = document.getElementById('relationshipLevel');
        if (relationshipLevel) {
            relationshipLevel.textContent = data.relationship_level || 'جديد';
        }
        
        // Update topics list
        const topicsList = document.getElementById('topicsList');
        if (topicsList) {
            if (data.topics && data.topics.length > 0) {
                topicsList.innerHTML = data.topics.map(topic => 
                    `<span class="topic-tag">${topic}</span>`
                ).join('');
            } else {
                topicsList.innerHTML = '<p>لا توجد مواضيع مطروحة بعد</p>';
            }
        }
    }
    
    async loadPersonality() {
        try {
            const response = await fetch('/personality');
            const data = await response.json();
            
            if (response.ok) {
                this.updatePersonalityDisplay(data);
            }
        } catch (error) {
            console.error('Error loading personality:', error);
        }
    }
    
    updatePersonalityDisplay(data) {
        // Update traits
        const traitsList = document.getElementById('traitsList');
        if (traitsList && data.personality?.traits) {
            traitsList.innerHTML = data.personality.traits.map(trait => 
                `<span class="trait-tag">${trait}</span>`
            ).join('');
        }
        
        // Update emotional state
        const emotionalState = document.getElementById('emotionalState');
        if (emotionalState) {
            emotionalState.textContent = data.emotional_state || 'متحمسة ومتفائلة';
        }
        
        // Update interests
        const interestsList = document.getElementById('interestsList');
        if (interestsList && data.personality?.interests) {
            interestsList.innerHTML = data.personality.interests.map(interest => 
                `<span class="interest-tag">${interest}</span>`
            ).join('');
        }
    }
    
    showMemoryModal() {
        const modal = document.getElementById('memoryModal');
        modal.classList.add('show');
        this.loadMemory();
    }
    
    showStatsModal() {
        const modal = document.getElementById('statsModal');
        modal.classList.add('show');
        this.loadStats();
    }
    
    showPersonalityModal() {
        const modal = document.getElementById('personalityModal');
        modal.classList.add('show');
        this.loadPersonality();
    }
    
    showSettingsModal() {
        const modal = document.getElementById('settingsModal');
        modal.classList.add('show');
        
        // Update form values
        document.getElementById('themeSelect').value = this.settings.theme;
        document.getElementById('fontSizeSelect').value = this.settings.fontSize;
        document.getElementById('soundToggle').checked = this.settings.soundEnabled;
        document.getElementById('gptModeToggle').checked = this.settings.gptModeEnabled;
    }
    
    closeModal(modal) {
        modal.classList.remove('show');
    }
    
    async resetMemory() {
        if (!confirm('هل أنت متأكد من إعادة تعيين الذاكرة؟ سيتم حذف جميع المعلومات المحفوظة.')) {
            return;
        }
        
        try {
            const response = await fetch('/reset', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            
            const data = await response.json();
            
            if (response.ok) {
                // Clear chat messages
                const chatMessages = document.getElementById('chatMessages');
                chatMessages.innerHTML = '';
                
                // Show welcome message
                this.showWelcomeMessage();
                
                // Clear message history
                this.messageHistory = [];
                
                // Show notification
                this.showNotification('تم إعادة تعيين الذاكرة بنجاح', 'success');
                
                // Close all modals
                document.querySelectorAll('.modal.show').forEach(modal => {
                    this.closeModal(modal);
                });
                
            } else {
                throw new Error(data.error || 'خطأ في إعادة تعيين الذاكرة');
            }
            
        } catch (error) {
            console.error('Error resetting memory:', error);
            this.showNotification('خطأ في إعادة تعيين الذاكرة', 'error');
        }
    }
    
    changeTheme(theme) {
        this.settings.theme = theme;
        this.setupTheme();
        this.saveSettings();
    }
    
    setupTheme() {
        const body = document.body;
        body.setAttribute('data-theme', this.settings.theme);
        
        // Update theme select
        const themeSelect = document.getElementById('themeSelect');
        if (themeSelect) {
            themeSelect.value = this.settings.theme;
        }
    }
    
    changeFontSize(size) {
        this.settings.fontSize = size;
        this.setupFontSize();
        this.saveSettings();
    }
    
    setupFontSize() {
        const body = document.body;
        body.className = body.className.replace(/font-\w+/g, '');
        body.classList.add(`font-${this.settings.fontSize}`);
        
        // Update font size select
        const fontSizeSelect = document.getElementById('fontSizeSelect');
        if (fontSizeSelect) {
            fontSizeSelect.value = this.settings.fontSize;
        }
    }
    
    toggleSound(enabled) {
        this.settings.soundEnabled = enabled;
        this.saveSettings();
    }
    
    toggleGPTMode(enabled) {
        this.settings.gptModeEnabled = enabled;
        this.saveSettings();
        
        // Update UI to reflect GPT mode
        const statusText = document.querySelector('.status-text');
        if (statusText) {
            statusText.textContent = enabled ? 'GPT Enhanced' : 'Standard';
        }
    }
    
    playNotificationSound() {
        if (!this.settings.soundEnabled) return;
        
        // Create a simple notification sound
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
        oscillator.frequency.setValueAtTime(600, audioContext.currentTime + 0.1);
        
        gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.2);
    }
    
    showNotification(message, type = 'success') {
        const notification = document.getElementById('notification');
        const notificationText = notification.querySelector('.notification-text');
        const notificationIcon = notification.querySelector('i');
        
        notificationText.textContent = message;
        
        // Update icon and color based on type
        switch (type) {
            case 'success':
                notificationIcon.className = 'fas fa-check-circle';
                notification.style.background = 'var(--success-color)';
                break;
            case 'error':
                notificationIcon.className = 'fas fa-exclamation-circle';
                notification.style.background = 'var(--error-color)';
                break;
            case 'warning':
                notificationIcon.className = 'fas fa-exclamation-triangle';
                notification.style.background = 'var(--warning-color)';
                break;
            default:
                notificationIcon.className = 'fas fa-info-circle';
                notification.style.background = 'var(--gpt-color)';
        }
        
        notification.classList.add('show');
        
        // Auto hide after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    }
    
    loadSettings() {
        const savedSettings = localStorage.getItem('aya-gpt-settings');
        if (savedSettings) {
            this.settings = { ...this.settings, ...JSON.parse(savedSettings) };
        }
    }
    
    saveSettings() {
        localStorage.setItem('aya-gpt-settings', JSON.stringify(this.settings));
    }
    
    // Utility methods
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.gptAIApp = new GPTEnhancedAIAgentApp();
});

// Add CSS for font sizes and additional styles
const style = document.createElement('style');
style.textContent = `
    .font-small { font-size: 0.875rem; }
    .font-medium { font-size: 1rem; }
    .font-large { font-size: 1.125rem; }
    
    .user-info-grid {
        display: grid;
        gap: 0.5rem;
    }
    
    .info-item {
        padding: 0.5rem;
        background: var(--bg-primary);
        border-radius: var(--radius-sm);
        border: 1px solid var(--border-light);
    }
    
    .gpt-enhanced {
        background: var(--gradient-gpt);
        color: var(--text-white);
    }
    
    .gpt-indicator {
        display: inline-block;
        background: var(--gpt-color);
        color: var(--text-white);
        padding: 0.25rem 0.5rem;
        border-radius: var(--radius-full);
        font-size: 0.75rem;
        font-weight: 600;
        margin-left: 0.5rem;
    }
`;
document.head.appendChild(style);
