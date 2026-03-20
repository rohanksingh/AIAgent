from app.tools.data_loader import load_data
from app.services.llm_client import ask_llm

def data_agent():
    df = load_data()
    summary = ask_llm(f"Summarize this dataset:\n{df.head().to_string()}")
    return df, summary