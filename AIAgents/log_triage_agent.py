import re

def triage(log_text):
    """
    Simple Log Triage Agent:
    - Extracts key error lines
    - Summarizes the type of failure
    """

    lines = log_text.strip().splitlines()

    # Try to extract lines with common failure signals
    error_lines = [line for line in lines if re.search(r'error|failed|exception', line, re.IGNORECASE)]

    # Limit to a few relevant lines
    short_summary = "\n".join(error_lines[:5]) if error_lines else "No errors found."

    # Basic diagnosis logic (can be replaced with LLM later)
    if "module not found" in log_text.lower():
        suggestion = "Possible missing dependency. Check package.json or npm install."
    elif "test failed" in log_text.lower():
        suggestion = "Some unit tests failed. Review the test cases."
    elif "timeout" in log_text.lower():
        suggestion = "Likely a long-running step or network issue."
    else:
        suggestion = "Manual review recommended. Unclassified error."

    return {
        "summary": short_summary,
        "suggestion": suggestion
    }

