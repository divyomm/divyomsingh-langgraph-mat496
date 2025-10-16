Lesson 1: Motivation

A single LLM can do a lot, but it’s limited — it can’t use tools, remember context, or handle multi-step tasks on its own.
LangGraph fixes this by letting us connect different steps (like retrieving data, reasoning, summarizing) into one flow.
It basically turns isolated LLM calls into structured, stateful workflows that can reason and act more intelligently.

Lesson 2: Simple Graph

In this lesson, I learned how to create a simple graph using LangGraph. The main idea is to connect different nodes (agents or tasks) and define how data flows between them. I got hands-on experience setting up inputs and outputs, running the graph, and seeing how everything interacts.

It also touched on debugging and monitoring the graph, which helps make sure everything works as expected. Overall, this lesson gave me a solid foundation to build more complex agent workflows in the future.

Lesson 3: LangSmith Studio

In this lesson, I learned how to use LangSmith Studio to build and test LangGraph workflows. I explored Graph Mode to visualize nodes and data flow, Chat Mode to test conversational agents, and tools for debugging and refining prompts. It helped me understand how to design, monitor, and improve agent workflows efficiently.

Lesson 4: Chain

In this lesson, I learned how to use Chains in LangGraph to connect multiple nodes into a sequence. Each node performs a specific task, and Chains manage the flow of data between them. I explored how to define inputs and outputs, handle errors, and ensure smooth execution across the sequence. This lesson helped me understand how to build more complex workflows by chaining together simpler tasks.

Lesson 5: Router

In this lesson, I learned how to use Routers in LangGraph to direct data to different paths based on conditions. Routers act like decision points in a workflow, allowing for dynamic branching. I explored how to set up conditions, manage multiple outputs, and ensure that data flows correctly through the chosen paths. This lesson helped me understand how to build more flexible and responsive workflows by incorporating conditional logic.

Lesson 6: Agents

In this module, I explored the concept of agents within the LangGraph framework. I learned that agents are components that can make decisions, manage state, and interact with tools or other agents to accomplish tasks. The module covered how to define agents, set up their logic, and integrate them into a larger workflow. By the end, I gained hands-on experience in building intelligent agents capable of performing complex, multi-step tasks autonomously.

Lesson 7: Agent with Memory

In this module, I learned how to enhance LangGraph agents with memory capabilities, enabling them to remember and utilize past interactions. I explored two types of memory:

Short-term memory: Persisted during a session, allowing agents to maintain context within a conversation.

Long-term memory: Stored across sessions, enabling agents to recall information from previous interactions.

I also practiced integrating memory into agents using LangGraph's checkpointer, allowing for state retention across multiple turns. This enhancement enables the creation of more intelligent and context-aware agents.