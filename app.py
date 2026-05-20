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
st.write(
    "Ask me about careers, resumes, interviews, skills, and learning roadmaps."
)

# Small UI improvement
st.markdown("""
<style>
.stChatInput input {
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

client = GeminiClient(config)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chats
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input(
    "Ask your career question..."
)

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.get_response(
                user_input,
                st.session_state.messages
            )

            st.write(response)

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    logger.info(f"User: {user_input}")
    logger.info(f"Bot: {response}")