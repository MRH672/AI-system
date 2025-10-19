import sys
from typing import Optional


class SimpleAgent:
    """A minimal, rule-based AI agent with a tiny set of intents.

    This agent is intentionally simple: it matches a handful of patterns
    and falls back to a helpful echo-style response. Designed to run in
    constrained environments with zero third-party dependencies.
    """

    def __init__(self, agent_name: str = "Iman-Agent") -> None:
        self.agent_name = agent_name

    def respond(self, message: str) -> str:
        normalized = message.strip().lower()

        if not normalized:
            return "I didn't catch that. Please type something."

        if any(greet in normalized for greet in ("hi", "hello", "hey", "salam", "سلام")):
            return "Hello! I'm a simple AI agent. How can I help you today?"

        if any(thanks in normalized for thanks in ("thanks", "thank you", "شكرا", "thx")):
            return "You're welcome!"

        if "help" in normalized or "مساعدة" in normalized:
            return (
                "You can ask me simple questions. Examples: '\n'"
                "- say hi\n"
                "- ask for a quick summary about a topic (very short)\n"
                "- or just type anything and I'll try to assist"
            )

        if normalized.startswith("summarize ") or normalized.startswith("summary ") or normalized.startswith("خلاصة "):
            topic = message.split(" ", 1)[1] if " " in message else "the topic"
            return (
                f"Brief summary of {topic}: A concise, high-level overview highlighting key points "
                "with minimal detail. Ask more specific questions for depth."
            )

        if "time" in normalized:
            from datetime import datetime

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return f"Current local time: {now}"

        if "exit" in normalized or "quit" in normalized or "خروج" in normalized:
            return "__EXIT__"

        return (
            "I may be simple, but I'm here to help. You said: '"
            + message.strip()
            + "'. Try 'help' for options."
        )


def run_repl(agent: Optional[SimpleAgent] = None) -> int:
    agent = agent or SimpleAgent()
    print(f"{agent.agent_name} ready. Type 'help' or 'exit' to quit.")

    try:
        while True:
            try:
                user_input = input("> ")
            except EOFError:
                print()  # new line for clean exit
                break

            reply = agent.respond(user_input)
            if reply == "__EXIT__":
                print("Goodbye!")
                break

            print(reply)
    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")
    return 0


if __name__ == "__main__":
    sys.exit(run_repl())


