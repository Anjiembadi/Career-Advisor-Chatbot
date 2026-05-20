import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:

    def __init__(self):

        self.GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

        self.GEMINI_MODEL = "gemini-2.5-flash"