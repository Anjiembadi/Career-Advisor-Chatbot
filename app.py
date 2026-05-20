import streamlit as st
from config import AppConfig
from gemini_client import GeminiClient
from logger import setup_logger

logger = setup_logger()
config = AppConfig()

st.set_page_config(
    page_title="Career Advisor Chatbot",
    page_icon="💼",
    layout="centered"
)

st.title("💼 Career Advisor Chatbot")
st.write("Ask me about careers, resumes, interviews, skills, and learning roadmaps.")

client = GeminiClient(config)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask your career question...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):

        response_placeholder = st.empty()
    full_response = ""

    try:

        with st.spinner("Thinking..."):

            for chunk in client.get_response_stream(
                user_input,
                st.session_state.messages
            ):

                full_response += chunk
                response_placeholder.markdown(full_response)

    except Exception as e:

        full_response = f"Error: {str(e)}"
        response_placeholder.error(full_response)