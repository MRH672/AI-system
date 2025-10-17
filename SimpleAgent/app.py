import json
import os
import uuid
from datetime import datetime, timedelta

from flask import Flask, request, jsonify, render_template, make_response


APP_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(APP_DIR, "data", "memories")
os.makedirs(DATA_DIR, exist_ok=True)


def get_or_create_user_id():
    user_id = request.cookies.get("user_id")
    if not user_id:
        user_id = str(uuid.uuid4())
    return user_id


def memory_path_for(user_id: str) -> str:
    safe_id = "".join(ch for ch in user_id if ch.isalnum() or ch in ("-", "_"))
    return os.path.join(DATA_DIR, f"{safe_id}.json")


def load_memory(user_id: str) -> dict:
    path = memory_path_for(user_id)
    if not os.path.exists(path):
        return {"messages": [], "created_at": datetime.utcnow().isoformat()}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"messages": [], "created_at": datetime.utcnow().isoformat()}


def save_memory(user_id: str, memory: dict) -> None:
    path = memory_path_for(user_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)


def build_response(user_text: str, memory: dict) -> str:
    if not memory.get("messages"):
        return (
            "Hello! I'm your simple English AI agent. I will remember what you say, "
            "even if you close and come back later. How can I help you today?"
        )

    lowered = (user_text or "").strip().lower()
    if not lowered:
        return "I'm here. Please type something and I'll respond."

    if any(greet in lowered for greet in ["hello", "hi", "hey"]):
        return "Hi again! I’m still here and I remember our chat."

    if "remember" in lowered or "do you remember" in lowered:
        return "Yes, I store all your messages so I can recall them later."

    if "what did i say" in lowered or "what i said" in lowered:
        # Return last 3 user messages
        user_msgs = [m["text"] for m in memory["messages"] if m["role"] == "user"]
        if not user_msgs:
            return "You haven't told me anything yet."
        recent = user_msgs[-3:]
        joined = " | ".join(recent)
        return f"Recently you said: {joined}"

    return (
        "Got it. I've saved that. If you ask later, I can remind you what you said."
    )


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates")

    @app.route("/", methods=["GET"])
    def index():
        user_id = get_or_create_user_id()
        memory = load_memory(user_id)
        resp = make_response(render_template("index.html", messages=memory.get("messages", [])))
        if not request.cookies.get("user_id"):
            # Persist cookie for 180 days
            expires = datetime.utcnow() + timedelta(days=180)
            resp.set_cookie("user_id", user_id, expires=expires, httponly=False, samesite="Lax")
        return resp

    @app.post("/api/message")
    def api_message():
        user_id = get_or_create_user_id()
        memory = load_memory(user_id)

        data = request.get_json(silent=True) or {}
        user_text = (data.get("message") or "").strip()

        # Append user message to memory
        memory.setdefault("messages", []).append({
            "role": "user",
            "text": user_text,
            "ts": datetime.utcnow().isoformat()
        })

        # Build assistant reply (English only)
        assistant_text = build_response(user_text, memory)

        # Append assistant message
        memory["messages"].append({
            "role": "assistant",
            "text": assistant_text,
            "ts": datetime.utcnow().isoformat()
        })

        save_memory(user_id, memory)

        resp = make_response(jsonify({
            "reply": assistant_text,
            "messages": memory["messages"]
        }))
        if not request.cookies.get("user_id"):
            expires = datetime.utcnow() + timedelta(days=180)
            resp.set_cookie("user_id", user_id, expires=expires, httponly=False, samesite="Lax")
        return resp

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


