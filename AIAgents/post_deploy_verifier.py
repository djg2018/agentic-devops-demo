import subprocess
import requests
from AIAgents.log_triage_agent import triage

def verify_app(port=8080):
    try:
        response = requests.get(f"http://35.224.117.74:8080/", timeout=5)
        if response.status_code == 200:
            return {"status": "healthy", "details": "App responded with 200 OK"}
        else:
            return {"status": "error", "details": f"Unexpected status code: {response.status_code}"}
    except Exception as e:
        # App is not responding, run triage
        try:
            logs = subprocess.check_output(["tail", "-n", "50", "output.log"], text=True)
        except Exception:
            logs = "No output.log found or unreadable"

        analysis = triage(logs)
        return {"status": "unreachable", "details": str(e), "triage": analysis}
