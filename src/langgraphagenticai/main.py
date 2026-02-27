import streamlit as st

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.displayresult import DisplayResultsStreamlit


def load_langgraph_agenticai_app():
    """Main function to load the LangGraph Agentic AI Streamlit app."""

    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()


    if not user_input:
        st.error("Please complete all required fields.")
        return 
    
    user_message=st.chat_input("Type your message here...")


    if user_message:
        try:
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to initialize the LLM model. Please check your API key and model selection.")
                return
            
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("Please select a use case.")
                return
            
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                display=DisplayResultsStreamlit(usecase,graph,user_message)
                display.display_result_on_ui()
            except ValueError as ve:
                st.error(f"Error setting up graph: {ve}")
                return

        except Exception as e:
            st.error(f"An error occurred: {e}")
            return