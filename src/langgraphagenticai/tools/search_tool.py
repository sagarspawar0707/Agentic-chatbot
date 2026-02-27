from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    return the list of tools to be used in the chatbot

    """
    tools=[TavilySearchResults(max_results=3)]
    return tools

def create_tool_nodes(tools):
    """
    Create ToolNode instances for each tool in the provided list.
    
    """
    return ToolNode(tools=tools)

