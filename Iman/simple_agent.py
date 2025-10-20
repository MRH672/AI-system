import json
import sys
import os
from datetime import datetime
from typing import Optional, Dict, List, Any


if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


class InteractiveAgent:

    def __init__(self, agent_name: str = "Iman-Agent") -> None:
        self.agent_name = agent_name
        self.memory_file = "memory.json"
        self.conversation_file = "conversations.json"
        self.memory = self.load_memory()
        self.conversation_history = self.load_conversations()
        self.learning_patterns = {
            "personal_info": ["اسمي", "أنا", "انا", "عمري", "سني", "انا عندي", "أعيش", "أعمل", "أدرس"],
            "preferences": ["أحب", "احب", "أفضل", "افضل", "لا أحب", "لا احب", "أكره", "اكره", "مفضل"],
            "facts": ["تعلم", "اعرف", "أعرف", "معلومات", "حقيقة"]
        }

    # ---------------- Memory Management ----------------
    def load_memory(self):
        try:
            with open(self.memory_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                
                if "user_info" not in data:
                    data["user_info"] = {}
                if "learned_facts" not in data:
                    data["learned_facts"] = []
                if "preferences" not in data:
                    data["preferences"] = {}
                if "conversation_count" not in data:
                    data["conversation_count"] = 0
                if "last_seen" not in data:
                    data["last_seen"] = ""
                return data
        except FileNotFoundError:
            return {
                "user_info": {},
                "learned_facts": [],
                "preferences": {},
                "conversation_count": 0,
                "last_seen": ""
            }

    def load_conversations(self):
        try:
            with open(self.conversation_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except (FileNotFoundError, json.JSONDecodeError, ValueError):
            return []

    def save_memory(self):
        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=4, ensure_ascii=False)

    def save_conversations(self):
        with open(self.conversation_file, "w", encoding="utf-8") as f:
            json.dump(self.conversation_history, f, indent=4, ensure_ascii=False)

    def update_memory(self, key, value):
        self.memory[key] = value
        self.save_memory()

    def add_learned_fact(self, fact: str, category: str = "general"):
        """إضافة حقيقة جديدة تعلمها الـ Agent"""
        fact_entry = {
            "fact": fact,
            "category": category,
            "learned_at": datetime.now().isoformat()
        }
        self.memory["learned_facts"].append(fact_entry)
        self.save_memory()

    

    def learn_from_message(self, message: str) -> Dict[str, Any]:
        """تحليل الرسالة وتعلم معلومات جديدة"""
        message_lower = message.lower()
        learned_info = {}
        
        
        if any(pattern in message_lower for pattern in self.learning_patterns["personal_info"]):
           
            if "اسمي" in message_lower:
                name_part = message_lower.split("اسمي")[-1].strip()
                if name_part and len(name_part) < 50:
                    learned_info["name"] = name_part.title()
            elif message_lower.startswith("انا ") or message_lower.startswith("أنا "):
                possible_name = message_lower.split(" ", 1)[-1].strip()
                if possible_name and len(possible_name) < 50 and not any(token in possible_name for token in ["عندي", "عمري", "سنة", "سن"]):
                    learned_info["name"] = possible_name.title()
            
            
            if any(token in message_lower for token in ["عمري", "عندي", "سنة", "سن", "سنى", "سني"]):
                import re
                age_match = re.search(r'(\d+)', message)
                if age_match:
                    learned_info["age"] = age_match.group(1)
        
       
        if any(pattern in message_lower for pattern in self.learning_patterns["preferences"]):
            if "أحب" in message_lower:
                liked_item = message_lower.split("أحب")[-1].strip()
                if liked_item and len(liked_item) < 100:
                    learned_info["likes"] = liked_item
            elif "أفضل" in message_lower:
                preferred_item = message_lower.split("أفضل")[-1].strip()
                if preferred_item and len(preferred_item) < 100:
                    learned_info["preferences"] = preferred_item
        
        return learned_info

    def respond(self, message: str) -> str:
        
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user_message": message,
            "agent_response": ""
        })
        
       
        learned_info = self.learn_from_message(message)
        if learned_info:
            for key, value in learned_info.items():
                if key == "name":
                    self.memory["user_info"]["name"] = value
                elif key == "age":
                    self.memory["user_info"]["age"] = value
                elif key == "likes":
                    self.memory["preferences"]["likes"] = value
                elif key == "preferences":
                    self.memory["preferences"]["general"] = value
            self.save_memory()
        
        normalized = message.lower().strip()
        if not normalized:
            return "لم أفهم ما تقول. من فضلك اكتب شيئاً واضحاً."

        
        if any(greet in normalized for greet in ("hi", "hello", "hey", "salam", "سلام", "مرحبا", "أهلا", "اهلا", "اهلاً", "السلام عليكم", "ازيك", "هلا", "هاي")):
            user_name = self.memory["user_info"].get("name", "")
            if user_name:
                self.memory["conversation_count"] += 1
                self.memory["last_seen"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_memory()
                return f"مرحباً مرة أخرى {user_name}! كيف حالك اليوم؟"
            return f"مرحباً! أنا {self.agent_name}. ما اسمك؟"

       
        if "اسمي" in normalized or normalized.startswith("انا ") or normalized.startswith("أنا "):
            if "اسمي" in normalized:
                name = normalized.split("اسمي")[-1].strip().title()
            else:
                name = normalized.split(" ", 1)[-1].strip().title()
            
            if name and len(name) < 50:
                self.memory["user_info"]["name"] = name
                self.save_memory()
                return f"سعيد بلقائك {name}! كم عمرك؟"

       
        if any(token in normalized for token in ["عمري", "انا عندي", "عندي", "سنة", "سن", "سني", "سنى"]):
            import re
            age_match = re.search(r'(\d+)', message)
            if age_match:
                age = age_match.group(1)
                self.memory["user_info"]["age"] = age
                self.save_memory()
                return f"ممتاز! إذن أنت {age} سنة. أخبرني المزيد عنك!"

        
        if any(token in normalized for token in ["صممتك", "انشأتك", "أنشأتك", "خلقتك", "عملتك", "سوّيتك", "سويتك"]):
            designer_name = self.memory["user_info"].get("name", "شخص")
            designer_age = self.memory["user_info"].get("age", "")
            self.memory["user_info"]["is_designer"] = True
            self.save_memory()
            return "رائع! سأتذكر دائماً أنك من صممني. شكراً لك!"

        if any(token in normalized for token in ["من صممك", "مين صممك", "من أنشأك", "مين أنشأك", "مين عملك", "من عملك", "من صانعك", "مين صانعك", "من خلقك", "مين خلقك", "مين مصممك", "من مصممك"]):
            if self.memory["user_info"].get("is_designer"):
                designer_name = self.memory["user_info"].get("name", "شخص")
                designer_age = self.memory["user_info"].get("age", "")
                if designer_age:
                    return f"صممتني {designer_name}، وهي {designer_age} سنة"
                else:
                    return f"صممتني {designer_name}"
            return "لا أعرف بعد من صممني"

        
        if any(token in normalized for token in ["وقت", "الساعة", "كم الساعة", "الوقت كام", "الساعة كام", "time"]):
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return f"الوقت الحالي: {now}"

        
        if "مساعدة" in normalized or "help" in normalized:
            return (
                "يمكنك أن تخبرني أشياء عنك، مثل:\n"
                "- اسمي إيمان\n"
                "- عمري 23 سنة\n"
                "- أحب البرمجة\n"
                "- صممتك\n"
                "وسأتذكر كل شيء حتى لو أغلقتني!"
            )

        
        if "ماذا تعرف" in normalized or "معلومات" in normalized:
            user_name = self.memory["user_info"].get("name", "غير معروف")
            user_age = self.memory["user_info"].get("age", "غير معروف")
            likes = self.memory["preferences"].get("likes", "لم تخبرني بعد")
            
            response = f"أعرف عنك:\n"
            response += f"- اسمك: {user_name}\n"
            response += f"- عمرك: {user_age} سنة\n"
            response += f"- تحب: {likes}\n"
            response += f"- عدد محادثاتنا: {self.memory['conversation_count']}\n"
            response += f"- آخر مرة تحدثنا: {self.memory['last_seen']}\n"
            return response

        
        if normalized in ("exit", "quit", "خروج", "وداع", "باي"):
            self.memory["last_seen"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_memory()
            return "_EXIT_"

        
        if learned_info:
            return "شكراً لك على هذه المعلومة! سأتذكرها. هل تريد إخباري بشيء آخر؟"
        
        return f"أفهم أنك تقول: '{message.strip()}' هل يمكنك توضيح أكثر؟"

# ---------------- REPL Loop ----------------
def run_repl(agent: Optional[InteractiveAgent] = None) -> int:
    agent = agent or InteractiveAgent()
    
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except Exception:
        pass

    print("=" * 60)
    print("AI Agent Interactive - عربي بالكامل")
    print("يتعلم ويتذكر معلوماتك حتى بعد إغلاق التطبيق")
    print("=" * 60)

    
    user_name = agent.memory["user_info"].get("name", "")
    if user_name:
        print(f"مرحباً مرة أخرى {user_name}!")
        print(f"أنا {agent.agent_name} - AI Agent متفاعل يتذكر كل شيء!")
        print(f"عدد محادثاتنا السابقة: {agent.memory['conversation_count']}")
        if agent.memory['last_seen']:
            print(f"آخر مرة تحدثنا: {agent.memory['last_seen']}")
    else:
        print(f"مرحباً! أنا {agent.agent_name}")
        print("AI Agent متفاعل يتعلم ويتذكر كل شيء!")
    
    print("اكتب 'مساعدة' للمساعدة أو 'خروج' للخروج")
    print("-" * 50)

    try:
        while True:
            try:
                user_input = input("أنت: ")
            except (EOFError, KeyboardInterrupt):
                print("\nتم إيقاف البرنامج.")
                break
            reply = agent.respond(user_input)
            
            
            if agent.conversation_history:
                agent.conversation_history[-1]["agent_response"] = reply
                agent.save_conversations()
            
            if reply == "_EXIT_":
                print("وداعاً! سأتذكر كل شيء حتى نلتقي مرة أخرى!")
                break
            print(f"الـ Agent: {reply}")
            print("-" * 30)
            
    except KeyboardInterrupt:
        print("\nتم إيقاف البرنامج. وداعاً!")
        agent.memory["last_seen"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        agent.save_memory()
    return 0


if __name__ == "__main__":
    sys.exit(run_repl())


