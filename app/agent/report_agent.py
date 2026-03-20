from app.services.llm_client import ask_llm

def report_agent(goal, plan, compliance_summary):
    prompt = f"""
Goal: {goal}

Plan:
{plan}

Compliance Summary:
{compliance_summary}

Write a final report with summary, findings, risk interpretation, and recommended action.
"""
    return ask_llm(prompt)