from dotenv import load_dotenv
import os


from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
load_dotenv()


@tool("triple")
def triple(x: float) -> float:
    """
    param num: The number to triple.
    return: The tripled value of the input number.
    """
    return float(x) * 3

tools = [TavilySearch(max_results=1), triple]

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0).bind_tools(tools)