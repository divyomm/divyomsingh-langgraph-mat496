from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END

# Simple State definition
class AgentState(TypedDict):
    messages: list[str]
    summary: str

# Dummy node function
def chatbot(state: AgentState):
    return {"messages": ["Module 2 chatbot processed this."]}

# Dummy node function
def summarizer(state: AgentState):
    return {"summary": "Summary of conversation"}

# Build graph
workflow = StateGraph(AgentState)
workflow.add_node("chatbot", chatbot)
workflow.add_node("summarizer", summarizer)

workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", "summarizer")
workflow.add_edge("summarizer", END)

app = workflow.compile()

print("Module 2: State & Memory executed successfully.")
print("Graph compiled with StateGraph, Nodes, and Edges.")
