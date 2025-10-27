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

## Module 2 – State Management in LangGraph

### Lesson: State Schema

In this lesson, I learned how to define the shape of the graph state using TypedDict. I explored how state is passed between nodes and how schema validation helps ensure data consistency throughout the graph execution.

### Lesson: State Reducers

In this lesson, I explored how to use reducers to manage state updates. I learned that by default, state keys are overwritten, but reducers like `add_messages` allow appending new information to lists, which is crucial for chat history.

### Lesson: Multiple Schemas

In this lesson, I learned how to deal with different input and output schemas. This is useful when different parts of the graph need to work with slightly different data structures, allowing for more flexible graph designs.

### Lesson: Trim and Filter Messages

In this lesson, I implemented strategies to manage the context window. I learned how to simply filter messages (e.g. keep only recent ones) or trim them to ensure the LLM receives the most relevant context without exceeding token limits.

### Lesson: Chatbot with Summarization

In this lesson, I learned how to integrate a summarization step into the graph. When the conversation gets too long, the graph can automatically generate a summary of older messages and store it, keeping the 'active' memory small.

### Lesson: Chatbot with External Memory

In this lesson, I connected the graph to an external database (simulated) to perist message history. This taught me how to save state outside the graph so that conversations can resume even after the process restarts.

## Module 3 – UX & Human-in-the-Loop

### Lesson: Breakpoints

In this lesson, I learned how to pause graph execution using `interrupt_before`. This allows for inspection of the state or simply stopping the process to wait for external triggers before proceeding.

### Lesson: Dynamic Breakpoints

In this lesson, I explored conditional breakpoints. Instead of always stopping, I learned to trigger interruptions only when certain criteria are met (suspicious output, low confidence, or specific tool usage).

### Lesson: Edit State & Human Feedback

In this lesson, I learned how a human can intervene during a breakpoint to edit the state. This enables "human-in-the-loop" workflows where a user can approve, reject, or modify an agent's proposed action before it executes.

### Lesson: Time Travel

In this lesson, I learned about LangGraph's checkpointing capabilities that allow "time travel". I can replay the graph from a previous state, which is incredibly useful for debugging or allowing users to retry specific steps.

### Lesson: Streaming Interruption

In this lesson, I learned how to handle interruptions even during streaming responses. This makes the user experience smoother, as users can stop an ongoing generation if they see it going off track.

## Module 4 – Tools & Agents

### Lesson: Parallelization

In this lesson, I learned how to run multiple nodes in parallel. This is helpful for tasks that don't depend on each other, significantly speeding up the overall workflow by processing independent steps concurrently.

### Lesson: Sub-graphs

In this lesson, I learned to compose graphs within graphs. This "sub-graph" pattern allows me to encapsulate complex logic into a single node in the parent graph, making the overall architecture modular and easier to read.

### Lesson: Map-Reduce

In this lesson, I applied the map-reduce pattern to LangGraph. I learned how to "map" a task across a list of inputs (processing them in parallel) and then "reduce" the results into a single summary or output.

### Lesson: Research Assistant

In this lesson, I combined the previous concepts to build a research assistant. It uses parallel browsing steps to gather information from multiple sources and then synthesizes the answer, demonstrating the power of concurrent agent execution.
