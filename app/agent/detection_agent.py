from app.tools.anomaly_detector import detect_anomalies
from app.services.llm_client import ask_llm

def detection_agent(df):
    suspicious = detect_anomalies(df)

    if suspicious.empty:
        detection_summary = "No suspicious trades detected."
    else:
        detection_summary = ask_llm(
            f"Explain why these trades may be suspicious:\n{suspicious.to_string(index=False)}"
        )

    return suspicious, detection_summary