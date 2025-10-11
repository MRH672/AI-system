#!/bin/bash

# ألوان للـ Terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

clear

echo -e "${CYAN}"
echo " █████╗ ██╗    ███████╗██╗ ██████╗ ███████╗███╗   ██╗████████╗"
echo "██╔══██╗██║    ██╔════╝██║██╔════╝ ██╔════╝████╗  ██║╚══██╔══╝"
echo "███████║██║    █████╗  ██║██║  ███╗█████╗  ██╔██╗ ██║   ██║   "
echo "██╔══██║██║    ██╔══╝  ██║██║   ██║██╔══╝  ██║╚██╗██║   ██║   "
echo "██║  ██║██║    ██║     ██║╚██████╔╝███████╗██║ ╚████║   ██║   "
echo "╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   "
echo -e "${NC}"
echo -e "${YELLOW}                    الذكي الذي يتعلم من كل تفاعل${NC}"
echo
echo "================================================================"
echo

# التحقق من وجود Python3
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ خطأ: Python3 غير مثبت${NC}"
    echo
    echo "يرجى تثبيت Python3 أولاً:"
    echo "• Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "• CentOS/RHEL: sudo yum install python3 python3-pip"
    echo "• macOS: brew install python3"
    echo
    exit 1
fi

echo -e "${GREEN}✅ Python3 مثبت بنجاح${NC}"
echo

# التحقق من وجود الملفات المطلوبة
if [ ! -f "src/ai_agent.py" ]; then
    echo -e "${RED}❌ خطأ: ملف src/ai_agent.py غير موجود${NC}"
    exit 1
fi

if [ ! -f "src/app.py" ]; then
    echo -e "${RED}❌ خطأ: ملف src/app.py غير موجود${NC}"
    exit 1
fi

echo -e "${GREEN}✅ الملفات المطلوبة موجودة${NC}"
echo

echo -e "${BLUE}🚀 بدء تشغيل AI Agent...${NC}"
echo
echo -e "${PURPLE}📱 سيتم فتح المتصفح تلقائياً${NC}"
echo -e "${PURPLE}🌐 أو انتقل يدوياً إلى: http://localhost:5000${NC}"
echo
echo -e "${YELLOW}⏹️ اضغط Ctrl+C لإيقاف الخادم${NC}"
echo

# تشغيل AI Agent
python3 scripts/launch.py

echo
echo -e "${GREEN}👋 شكراً لك لاستخدام AI Agent!${NC}"
