import json

from google import genai

from app.config import settings


client = genai.Client(api_key=settings.GEMINI_API_KEY)


class LLMService:

    def generate(self, prompt: str) -> dict:
        """
        Sends the prompt to Gemini and returns parsed JSON.
        """

        response = client.models.generate_content(
            model=settings.MODEL_NAME,
            contents=prompt,
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = (
                text.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return json.loads(text)