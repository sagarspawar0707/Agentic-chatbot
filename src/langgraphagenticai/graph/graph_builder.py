from langgraph.graph import START, StateGraph, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.node.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_nodes
from langgraph.prebuilt import ToolNode,tools_condition
from src.langgraphagenticai.node.chatbot_with_tool_node import ChatbotWithToolNode


class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)


    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph with a single state that processes user messages and generates responses.
        """
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process_input)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds a chatbot graph that integrates external tools for enhanced functionality.
        """
        #define tool and tool nodes
        tools=get_tools()
        tool_node=create_tool_nodes(tools)

        ## Define LLm
        llm=self.llm

        obj_chatbot_with_node=ChatbotWithToolNode(llm,tool_node)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)

        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)

        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot",END)


    def setup_graph(self,usecase):
        """
        Sets up the graph based on the selected use case.
        """
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase=="Chatbot With Web":
            self.chatbot_with_tools_build_graph()    

        return self.graph_builder.compile()
          
                                    