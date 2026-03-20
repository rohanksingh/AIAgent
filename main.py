# Orchestration (Main Logic)

from app.agent.planner_agent import planner_agent   
from app.agent.data_agent  import data_agent
from app.agent.detection_agent   import detection_agent  
from app.agent.compliance_agent  import compliance_agent  
from app.agent.report_agent import report_agent 

goal = "Investigate suspicious trades"

# Step 1 : Plan 

plan = planner_agent(goal)
print("\nPLAN:\n", plan)

# Step 2: Load Data 

df, data_summary = data_agent()

# step 3: detect anomalies

suspicious, detection_summary = detection_agent(df)

# step 4 : Compliance analysis

compliance_output = compliance_agent(
    data_summary ,
    detection_summary,
    suspicious
)

# Step 5: Final report 

final_report = report_agent(
    goal,   
    plan,
    compliance_output
)

print("\nFINAL REPORT:\n")
print(final_report)