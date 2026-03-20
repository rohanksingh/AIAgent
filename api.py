from fastapi import FastAPI, Response
from pydantic import BaseModel, Field
from app.orchestrator import run_surveillance_workflow

app = FastAPI()

class GoalRequest(BaseModel):
    goal: str = Field(
        ...,
        example="Investigate suspicious trades and produce a surveillance report",
        description="Describe the analytical goal for the AI agent"
    )

@app.get("/")
def home():
    return {"message": "Agentic AI API is running"}

@app.head("/")
def home_head():
    return Response(status_code=200)

@app.post("/run-agent")
def run_agent(req: GoalRequest):
    print("INPUT RECEIVED:", req.goal)
    return run_surveillance_workflow(req.goal)