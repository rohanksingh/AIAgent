# AIAgent

## Project Architecture

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

## Project folder structure
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


