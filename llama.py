import os
import streamlit as st
from streamlit_chat import message
import cohere

cohere_api_key = "sx25yULmw6YEvfNlXlRp0bTiQlR7eOZc7Vsn9YOT"

if not cohere_api_key:
    raise ValueError("COHERE_API_KEY environment variable not found")

co = cohere.Client(cohere_api_key)

def get_response(prompt):
    response = co.generate(
        model='command',  
        prompt=prompt,
        max_tokens=50
    )
    return response.generations[0].text.strip()


def clear_chat():
    st.session_state.messages = [{"role": "assistant", "content": "Say something to get started!"}]

