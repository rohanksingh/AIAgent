from app.agent.planner_agent import planner_agent
from app.agent.data_agent import data_agent
from app.agent.detection_agent import detection_agent
from app.agent.compliance_agent import compliance_agent
from app.agent.report_agent import report_agent

def run_surveillance_workflow(goal: str):
    print("Running workflow for goal:", goal)

    plan = planner_agent(goal)
    print("PLAN:", plan)

    df, data_summary = data_agent()
    print("DATA SUMMARY:", data_summary)

    suspicious, detection_summary = detection_agent(df)
    print("DETECTION SUMMARY:", detection_summary)

    compliance_summary = compliance_agent(data_summary, detection_summary, suspicious)
    print("COMPLIANCE SUMMARY:", compliance_summary)

    final_report = report_agent(goal, plan, compliance_summary)
    print("FINAL REPORT:", final_report)

    suspicious_rows = suspicious.to_dict(orient="records") if not suspicious.empty else []

    result = {
        "goal": goal,
        "plan": plan,
        "data_summary": data_summary,
        "detection_summary": detection_summary,
        "compliance_summary": compliance_summary,
        "suspicious_trades": suspicious_rows,
        "final_report": final_report,
    }

    print("WORKFLOW RESULT:", result)
    return result