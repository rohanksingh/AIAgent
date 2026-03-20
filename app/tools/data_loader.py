import pandas as pd        

def load_data():
    df = pd.read_csv("C:/Users/rohan/agentic-trade-surveillance/data/trades.csv")
    return df       #.to_string(index=False)