"""
ملف إعدادات AI Agent
"""

# إعدادات قاعدة البيانات
DATABASE_CONFIG = {
    'default_path': 'agent_memory.db',
    'backup_enabled': True,
    'backup_interval': 100,  # عدد المحادثات قبل النسخ الاحتياطي
}

# إعدادات التعلم
LEARNING_CONFIG = {
    'similarity_threshold': 0.3,  # عتبة التشابه للبحث عن محادثات مشابهة
    'min_pattern_frequency': 2,   # الحد الأدنى لعدد مرات تكرار النمط
    'confidence_increment': 0.1,  # زيادة الثقة عند التعلم
    'max_patterns': 1000,         # الحد الأقصى لعدد الأنماط المحفوظة
}

# إعدادات معالجة النصوص
TEXT_PROCESSING_CONFIG = {
    'max_input_length': 500,      # الحد الأقصى لطول المدخلات
    'min_input_length': 1,        # الحد الأدنى لطول المدخلات
    'remove_stopwords': True,     # إزالة الكلمات الشائعة
    'language': 'english',        # اللغة الافتراضية
}

# إعدادات تحليل المشاعر
SENTIMENT_CONFIG = {
    'positive_words': [
        'good', 'great', 'excellent', 'amazing', 'wonderful', 'love', 'like', 
        'happy', 'pleased', 'fantastic', 'awesome', 'brilliant', 'perfect',
        'beautiful', 'nice', 'wonderful', 'outstanding', 'superb', 'marvelous'
    ],
    'negative_words': [
        'bad', 'terrible', 'awful', 'hate', 'dislike', 'angry', 'sad', 
        'disappointed', 'horrible', 'worst', 'hateful', 'annoying', 'frustrated',
        'upset', 'mad', 'furious', 'disgusting', 'pathetic', 'useless'
    ]
}

# إعدادات المواضيع
TOPIC_CONFIG = {
    'keywords': {
        'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
        'weather': ['weather', 'rain', 'sunny', 'cloudy', 'temperature', 'hot', 'cold', 'windy'],
        'food': ['food', 'eat', 'restaurant', 'cooking', 'recipe', 'meal', 'hungry', 'dinner'],
        'work': ['work', 'job', 'office', 'meeting', 'project', 'boss', 'colleague', 'career'],
        'technology': ['computer', 'software', 'programming', 'AI', 'technology', 'code', 'app', 'website'],
        'personal': ['family', 'friend', 'relationship', 'personal', 'life', 'home', 'health'],
        'entertainment': ['movie', 'music', 'game', 'book', 'sport', 'fun', 'party', 'vacation'],
        'education': ['school', 'university', 'study', 'learn', 'course', 'teacher', 'student'],
        'shopping': ['buy', 'shop', 'store', 'price', 'money', 'purchase', 'sale', 'discount']
    }
}

# إعدادات الردود الافتراضية
DEFAULT_RESPONSES = {
    'greeting': [
        "مرحباً! كيف يمكنني مساعدتك اليوم؟",
        "أهلاً وسهلاً! أنا هنا لمساعدتك.",
        "مرحباً بك! كيف حالك اليوم؟"
    ],
    'weather': [
        "الطقس موضوع مثير للاهتمام. كيف هو الطقس في منطقتك؟",
        "أحب التحدث عن الطقس! هل تستمتع بالطقس اليوم؟",
        "الطقس يؤثر على مزاجنا كثيراً. كيف تشعر تجاه الطقس؟"
    ],
    'food': [
        "الطعام رائع! هل تريد التحدث عن وصفة معينة أو مطعم؟",
        "أحب الطعام! ما هو طعامك المفضل؟",
        "الطبخ فن جميل. هل تحب الطبخ؟"
    ],
    'work': [
        "العمل جزء مهم من حياتنا. كيف تسير الأمور في عملك؟",
        "العمل يمكن أن يكون ممتعاً ومليئاً بالتحديات. كيف تشعر تجاه عملك؟",
        "أتمنى أن يكون يومك في العمل جيداً!"
    ],
    'technology': [
        "التكنولوجيا تتطور بسرعة! ما الذي يثير اهتمامك في هذا المجال؟",
        "أحب التكنولوجيا! هل تعمل في مجال التقنية؟",
        "التكنولوجيا تجعل حياتنا أسهل. ما رأيك في ذلك؟"
    ],
    'positive': [
        "أشعر أنك في مزاج جيد اليوم! هذا رائع.",
        "يبدو أنك سعيد! هذا يجعلني سعيداً أيضاً.",
        "مزاجك الإيجابي مُعدي! شكراً لك."
    ],
    'negative': [
        "يبدو أنك تمر بيوم صعب. هل تريد التحدث عن ما يزعجك؟",
        "أفهم أنك تشعر بالإحباط. أنا هنا للاستماع.",
        "أتمنى أن تتحسن حالتك قريباً. هل يمكنني مساعدتك؟"
    ],
    'default': [
        "هذا مثير للاهتمام. هل يمكنك إعطائي المزيد من التفاصيل؟",
        "أفهم. هل تريد التحدث أكثر عن هذا الموضوع؟",
        "شكراً لك على مشاركة هذا معي. ماذا تريد أن نفعل؟"
    ]
}

# إعدادات واجهة الويب
WEB_CONFIG = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': True,
    'max_message_length': 500,
    'auto_save_interval': 30,  # ثواني
}

# إعدادات النسخ الاحتياطي
BACKUP_CONFIG = {
    'enabled': True,
    'directory': 'backups',
    'max_backups': 10,
    'compression': True,
}
