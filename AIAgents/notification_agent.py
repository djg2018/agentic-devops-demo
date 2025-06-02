# notification_agent.py
import smtplib  # Included as placeholder; not used in this demo
from email.message import EmailMessage  # Also placeholder

def notify(error_summary, fix_suggestion):
    print("\n" + "=" * 60)
    print("📢 Deployment Notification")
    print("-" * 60)
    print("🔍 Issue Summary:")
    print(error_summary)
    print("\n🛠️ Suggested Fix:")
    print(fix_suggestion)
    print("=" * 60 + "\n")
    return True

