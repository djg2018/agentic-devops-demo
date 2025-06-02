# fix_suggestion_agent.py

def suggest_fix(error_summary):
    suggestions = {
        "Intentional startup failure for triage test": "Remove the test error from app.js or comment it out to allow successful startup.",
        "EADDRINUSE": "Port is already in use. Free the port or use a different one.",
        "MODULE_NOT_FOUND": "A required module is missing. Run `npm install` or check dependencies.",
    }

    for key, fix in suggestions.items():
        if key in error_summary:
            return fix

    return "No known fix found. Please investigate manually."
