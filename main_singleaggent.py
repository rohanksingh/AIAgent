from app.agent.agent_loop import run_agent

if __name__== "__main__":
    goal = "Investigate suspicious trades"
    state = run_agent(goal)
    
    print("\nFinal Output:\n")
    print(state.final_answer)