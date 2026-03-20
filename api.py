from fastapi import FastAPI, Response
from pydantic import BaseModel, Field
from app.orchestrator import run_surveillance_workflow

app = FastAPI(
    title="Agentic AI Trade Surveillance API",
    description="Multi-agent AI system for detecting suspicious trades and generating compliance reports",
    version="1.0"
)

# -----------------------------
# Request Model
# -----------------------------
class GoalRequest(BaseModel):
    goal: str = Field(
        ...,
        example="Investigate suspicious trades and produce a surveillance report",
        description="Describe the analytical goal for the AI agent"
    )

# -----------------------------
# Root Endpoint (GET)
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Agentic AI API is running",
        "docs": "/docs",
        "endpoint": "/run-agent"
    }

# -----------------------------
# Health Check (HEAD) - Render friendly
# -----------------------------
@app.head("/")
def health_check():
    return Response(status_code=200)

# -----------------------------
# Helper GET route (browser-friendly)
# -----------------------------
@app.get("/run-agent")
def run_agent_info():
    return {
        "message": "Use POST /run-agent with JSON body",
        "example": {
            "goal": "Investigate suspicious trades and produce a surveillance report"
        }
    }

# -----------------------------
# Main Agent Endpoint (POST)
# -----------------------------
@app.post("/run-agent")
def run_agent(req: GoalRequest):

    # fallback for Swagger default
    goal = req.goal
    if not goal or goal.strip().lower() == "string":
        goal = "Investigate suspicious trades and produce a surveillance report"

    result = run_surveillance_workflow(goal)

    return {
        "status": "success",
        "data": result
    }