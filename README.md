## AIAgent

### Project Architecture

```mermaid
graph TD
    A[agentic-trade-surveillance]

    A --> B[api.py]
    A --> C[main.py]
    A --> D[requirements.txt]

    A --> E[app]
    E --> F[orchestrator.py]

    E --> G[agents]
    G --> G1[planner_agent.py]
    G --> G2[data_agent.py]
    G --> G3[detection_agent.py]
    G --> G4[compliance_agent.py]
    G --> G5[report_agent.py]

    E --> H[tools]
    H --> H1[data_loader.py]
    H --> H2[anomaly_detector.py]

    E --> I[services]
    I --> I1[llm_client.py]

    A --> J[data]
    J --> J1[trades.csv]
```

### Project folder structure

```

agentic-trade-surveillance/
│
├── api.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── app/
│   ├── __init__.py
│   ├── orchestrator.py
│   │
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── data_agent.py
│   │   ├── detection_agent.py
│   │   ├── compliance_agent.py
│   │   └── report_agent.py
│   │
│   ├── tools/
│   │   ├── data_loader.py
│   │   └── anomaly_detector.py
│   │
│   └── services/
│       └── llm_client.py
│
└── data/
    └── trades.csv
```
### Demo link 

https://aiagent-ln0x.onrender.com

<img width="372" height="178" alt="image" src="https://github.com/user-attachments/assets/991b7f89-b197-4b2f-b43f-eab9851a6310" />

### Demo deployment on reander.com

<img width="853" height="392" alt="image" src="https://github.com/user-attachments/assets/36454a75-d830-4216-8951-0a2fc1841d25" />

### Demo run on webbrowser

<img width="867" height="442" alt="image" src="https://github.com/user-attachments/assets/e24a6d49-99d9-48c0-bf91-5c31509a2fec" />

### Running locally 

```bash
pip install -r requirements.txt
uvicorn api:app --reload
```

### Output Sample shared in screenshots

```bash
Link for getting output
http://127.0.0.1:8000/docs
```

