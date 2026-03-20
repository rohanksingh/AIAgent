from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    work = df.copy()
    model = IsolationForest(contamination=0.2, random_state=42)
    work["flag"] = model.fit_predict(work[["price", "quantity"]])
    return work[work["flag"] == -1]
    print(type(df))

