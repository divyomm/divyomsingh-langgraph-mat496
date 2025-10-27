from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    approval_status: str

def step_1(state: AgentState):
    print("Step 1 executed.")
    return {"approval_status": "pending"}

def human_approval(state: AgentState):
    print("Human approval step (simulated breakpoint).")
    # In a real scenario, we would interrupt here using interrupt_before
    return {"approval_status": "approved"}

def step_2(state: AgentState):
    print(f"Step 2 executed with status: {state['approval_status']}")
    return {}

workflow = StateGraph(AgentState)
workflow.add_node("step_1", step_1)
workflow.add_node("human_approval", human_approval)
workflow.add_node("step_2", step_2)

workflow.add_edge(START, "step_1")
workflow.add_edge("step_1", "human_approval")
workflow.add_edge("human_approval", "step_2")
workflow.add_edge("step_2", END)

# Compile with interrupt_before logic (commented out for simple run)
app = workflow.compile()

print("Module 3: UX & Human-in-the-Loop executed successfully.")
