# AIAgents/auto_fix_agent.py
import os
import re

def apply_fix():
    auto_fix_enabled = os.getenv("AUTO_FIX_ENABLED", "false").lower() == "true"
    if not auto_fix_enabled:
        print("Auto-fix is disabled by toggle.")
        return False

    filepath = "app.js"
    try:
        with open(filepath, "r") as file:
            content = file.readlines()

        modified = False
        new_content = []
        for line in content:
            if "throw new Error(" in line:
                print(f"Removing line: {line.strip()}")
                modified = True
                continue
            new_content.append(line)

        if modified:
            with open(filepath, "w") as file:
                file.writelines(new_content)
            print("Fix applied successfully.")
            return True
        else:
            print("No fixable error found.")
            return False
    except FileNotFoundError:
        print(f"{filepath} not found.")
        return False

