import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:

    def __init__(self):

        try:
            import streamlit as st
            self.GOOGLE_API_KEY = st.secrets.get("GEMINI_API_KEY")
            self.GEMINI_MODEL = st.secrets.get("GEMINI_MODEL")
        except Exception:
            self.GOOGLE_API_KEY = None
            self.GEMINI_MODEL = None

        self.GOOGLE_API_KEY = self.GOOGLE_API_KEY or os.getenv("GEMINI_API_KEY")

        self.GEMINI_MODEL = (
            self.GEMINI_MODEL
            or os.getenv("GEMINI_MODEL")
            or "gemini-2.5-flash"
        )