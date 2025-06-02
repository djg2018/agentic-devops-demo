import os
from AIAgents.log_triage_agent import triage
from AIAgents.fix_suggestion_agent import suggest_fix
from AIAgents.notification_agent import notify
from AIAgents.auto_fix_agent import apply_fix

def run_agentic_ai():
    if os.getenv("AGENTIC_AI_ENABLED", "false").lower() != "true":
        print("🔕 Agentic AI is disabled by toggle.")
        return

    print("🤖 Agentic AI is enabled. Starting triage...")

    try:
        with open("app.log") as f:
            log = f.read()
    except FileNotFoundError:
        print("❌ Log file 'app.log' not found.")
        return

    result = triage(log)
    summary = result.get("summary")
    suggestion = result.get("suggestion")

    print(f"🔎 Summary: {summary}")
    print(f"💡 Suggestion: {suggestion}")

    # Send notification
    notify(summary, suggestion)

    # Auto-fix if enabled
    if os.getenv("AUTO_FIX_ENABLED", "false").lower() == "true":
        print("🛠️ Auto-fix is enabled.")
        apply_fix()
    else:
        print("🛑 Auto-fix is disabled. Manual intervention required.")

if __name__ == "__main__":
    run_agentic_ai()
