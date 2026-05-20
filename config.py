import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

class AppConfig:

    def __init__(self):

        self.GOOGLE_API_KEY = (
            st.secrets.get("GEMINI_API_KEY")
            or os.getenv("GEMINI_API_KEY")
        )

        self.GEMINI_MODEL = (
            st.secrets.get("GEMINI_MODEL")
            or os.getenv("GEMINI_MODEL")
            or "gemini-1.5-flash"
        )