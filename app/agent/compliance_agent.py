from app.services.llm_client import ask_llm

def compliance_agent(data_summary, detection_summary, suspicious):
    suspicious_text = suspicious.to_string(index=False) if not suspicious.empty else "No suspicious trades."
    prompt = f"""
Data Summary:
{data_summary}

Detection Summary:
{detection_summary}

Trades:
{suspicious_text}

Provide compliance interpretation and next review steps.
"""
    return ask_llm(prompt)