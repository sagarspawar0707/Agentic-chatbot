import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
            selected_groq_model = self.user_controls_input.get("selected_model")

            # Validate API key
            if not groq_api_key:
                groq_api_key = os.getenv("GROQ_API_KEY")

            if not groq_api_key:
                st.error("Please enter GROQ API KEY")
                return None

            # Create LLM OUTSIDE condition
            llm = ChatGroq(
                model=selected_groq_model,
                groq_api_key=groq_api_key
            )

            return llm

        except Exception as e:
            raise ValueError(f"Error initializing GROQ LLM: {e}")

        
