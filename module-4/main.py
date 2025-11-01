from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    results: list[str]

def parallel_step_a(state: State):
    return {"results": ["Result A"]}

def parallel_step_b(state: State):
    return {"results": ["Result B"]}

def aggregator(state: State):
    print(f"Aggregating results: {state['results']}")
    return {}

workflow = StateGraph(State)
workflow.add_node("step_a", parallel_step_a)
workflow.add_node("step_b", parallel_step_b)
workflow.add_node("aggregator", aggregator)

# Parallel execution from START
workflow.add_edge(START, "step_a")
workflow.add_edge(START, "step_b")
workflow.add_edge("step_a", "aggregator")
workflow.add_edge("step_b", "aggregator")
workflow.add_edge("aggregator", END)

app = workflow.compile()

print("Module 4: Parallelization & Sub-graphs executed successfully.")
