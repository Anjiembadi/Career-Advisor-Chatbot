import google.generativeai as genai
from prompts import CareerAdvisorPrompts


class GeminiClient:

    def __init__(self, config):
        genai.configure(api_key=config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(config.GEMINI_MODEL)

    def get_response(self, user_input, history=None):
        try:
            prompt = CareerAdvisorPrompts.SYSTEM_PROMPT + "\n\nUser: " + user_input

            response = self.model.generate_content(prompt)

            return response.text

        except Exception as e:
            return f"Sorry, something went wrong: {str(e)}"