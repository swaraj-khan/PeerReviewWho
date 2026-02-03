import google.generativeai as genai
from config.settings import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

class LLMService:
    def __init__(self):
        self.model = genai.GenerativeModel(settings.MODEL_NAME)

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
