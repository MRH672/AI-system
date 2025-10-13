# حل المشاكل - Learning AI Agent 🔧

## المشاكل الشائعة والحلول

### 1. خطأ في حفظ الملفات
```
Error saving conversation: [Errno 2] No such file or directory: 'aya_conversations.json'
Error saving memory: [Errno 9] Bad file descriptor
```

**السبب**: الملفات تحاول الإنشاء في المجلد الخطأ

**الحل**: 
- تأكد من تشغيل الـ Agent من داخل مجلد `aya`
- استخدم ملف `start_learning_agent.bat` للتشغيل السهل
- أو استخدم الأمر: `cd aya` ثم `python learning_ai_agent.py`

### 2. خطأ في الترميز (Unicode)
```
UnicodeEncodeError: 'charmap' codec can't encode character
```

**السبب**: مشكلة في عرض النص العربي أو الإيموجي

**الحل**: 
- استخدم `learning_ai_agent.py` بدلاً من `ai_agent.py`
- تأكد من أن الـ CMD يدعم UTF-8
- استخدم Windows Terminal بدلاً من Command Prompt

### 3. الملفات لا تُحفظ
```
File not found errors
```

**الحل**:
1. تأكد من صلاحيات الكتابة في المجلد
2. تأكد من أن Python مثبت بشكل صحيح
3. استخدم المسار الكامل للملفات

### 4. الذاكرة لا تُحفظ
```
Memory not loading on restart
```

**الحل**:
1. تأكد من وجود ملف `aya_memory.json`
2. تأكد من صلاحيات القراءة والكتابة
3. امسح الملف وأعد المحاولة

## كيفية إعادة تعيين الذاكرة

### حذف جميع البيانات المحفوظة:
```bash
# في مجلد aya
del aya_memory.json
del aya_conversations.json
```

### أو استخدم هذا الأمر:
```bash
python -c "import os; os.remove('aya_memory.json') if os.path.exists('aya_memory.json') else None; os.remove('aya_conversations.json') if os.path.exists('aya_conversations.json') else None; print('Memory reset successfully')"
```

## التحقق من صحة الملفات

### فحص محتوى ملف الذاكرة:
```bash
python -c "import json; data = json.load(open('aya_memory.json', 'r', encoding='utf-8')); print(json.dumps(data, indent=2, ensure_ascii=False))"
```

### فحص محتوى ملف المحادثات:
```bash
python -c "import json; data = json.load(open('aya_conversations.json', 'r', encoding='utf-8')); print(f'Total conversations: {len(data)}')"
```

## نصائح للاستخدام الأمثل

1. **استخدم ملف Batch**: `start_learning_agent.bat`
2. **لا تغلق الـ CMD بقوة**: استخدم `exit` أو `quit`
3. **انتظر الحفظ**: دع الـ Agent يحفظ البيانات قبل الإغلاق
4. **تأكد من المجلد**: شغل الـ Agent من مجلد `aya`

## رسائل الخطأ والحلول

| الخطأ | السبب | الحل |
|-------|-------|------|
| `No such file or directory` | المجلد الخطأ | استخدم `cd aya` |
| `Bad file descriptor` | مشكلة في الكتابة | تأكد من الصلاحيات |
| `UnicodeEncodeError` | مشكلة ترميز | استخدم `learning_ai_agent.py` |
| `Permission denied` | صلاحيات | شغل كـ Administrator |

## اختبار سريع

```bash
# اختبار الـ Agent
python -c "from learning_ai_agent import LearningAIAgent; agent = LearningAIAgent(); print('Agent loaded successfully')"

# اختبار الحفظ
python -c "from learning_ai_agent import LearningAIAgent; agent = LearningAIAgent(); agent.save_memory(); print('Memory saved successfully')"
```

## الدعم

إذا استمرت المشاكل:
1. تأكد من إصدار Python (3.7+)
2. تأكد من صلاحيات المجلد
3. جرب تشغيل الـ Agent كـ Administrator
4. تحقق من مساحة القرص المتاحة

---

**نصيحة**: استخدم دائماً `start_learning_agent.bat` للحصول على أفضل تجربة! 🚀
