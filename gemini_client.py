import google.generativeai as genai
from prompts import CareerAdvisorPrompts


class GeminiClient:

    def __init__(self, config):
        genai.configure(api_key=config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(config.GEMINI_MODEL)

    def trim_history(self, messages, max_messages=6):
        """
        Keeps only the latest messages to avoid long context.
        """
        return messages[-max_messages:]

    def format_history(self, messages):
        history_text = ""

        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            history_text += f"{role}: {content}\n"

        return history_text

    def get_response_stream(self, user_input, messages):
        try:
            trimmed_messages = self.trim_history(messages)
            history_text = self.format_history(trimmed_messages)

            prompt = CareerAdvisorPrompts.build_prompt(
                user_input,
                history_text
            )

            response = self.model.generate_content(
                prompt,
                stream=True
            )

            for chunk in response:
                if chunk.text:
                    yield chunk.text

        except Exception as e:
            if "429" in str(e):
                yield "⚠️ Daily Gemini API limit reached. Please try again later."
            else:
                yield f"Sorry, something went wrong: {str(e)}"