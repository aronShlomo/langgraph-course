from dotenv import load_dotenv
import os

from langchain_core.messages import HumanMessage
from langgraph.graph import MessagesState, StateGraph,END
from nodes import run_agent_reasoning, tool_node

load_dotenv()

AGENT_REASON = "agent_reason"
ACT = "act"
LAST = -1

def should_continue(state: MessagesState) -> str:
    """
    Determine whether the agent should continue reasoning or if it has finished.
    This is a simple heuristic that checks if the last message from the agent contains a certain keyword.
    In a real implementation, this could be more complex and involve checking for specific conditions in the messages.
    """
    if not state["messages"][LAST].tool_calls:
        return END
    return ACT
    

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)
flow.add_conditional_edges(AGENT_REASON, should_continue, {
    END: END,
    ACT: ACT})

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path="flow.png")



if __name__ == "__main__":
    print("Hello from main langGraph!")
    
    
    # res = app.invoke({"messages": [HumanMessage(content="What is the capital of France?")]})
    # print(res["messages"][LAST].content)