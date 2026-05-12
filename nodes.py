from dotenv import load_dotenv
import os
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode

from react import llm, tools

load_dotenv()

SYSTEM_PROMPT = """You are a helpful assistant that can use 
tools to answer questions. You have access to the following tools:"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    """
    Run the agent reasoning process, which involves generating a
    response using the language model and tools, and then updating the state with the new messages.
    This function will be called repeatedly until the agent decides to stop.
    """
    
    response = llm.invoke([{"role": "system", "content": SYSTEM_PROMPT}], *state["messages"])
    return {"messages": [response]}


tool_node = ToolNode(tools)
