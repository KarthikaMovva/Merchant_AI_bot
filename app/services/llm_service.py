import os
import json
import re
import logging

import google.generativeai as genai

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LLMService:

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")

        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("gemini-2.5-flash")

    def generate(self, prompt: str):


        if not self.api_key:
            logger.warning("Gemini API key not configured. Running in demo mode.")

            return {
                "message": "Demo message: We miss you at our clinic!",
                "cta": "Book appointment",
                "send_as": "whatsapp",
                "rationale": "mock response (no api key)"
            }

        try:

            logger.info("Sending request to Gemini...")

            response = self.model.generate_content(prompt)

            text = response.text.strip()

            logger.info("Raw Gemini Response:\n%s", text)


            text = re.sub(r"^```json\s*", "", text)
            text = re.sub(r"\s*```$", "", text)
            text = text.strip()

            logger.info("Cleaned JSON:\n%s", text)

   
            data = json.loads(text)


            required_fields = [
                "message",
                "cta",
                "send_as",
                "rationale"
            ]
            required_fields = [
                "message",
                "cta",
                "send_as",
                "rationale"
            ]

            missing = [
                field
                for field in required_fields
                if field not in data
            ]

            if missing:
                raise ValueError(
                    f"Missing required fields: {', '.join(missing)}"
                )

            logger.info("LLM response validated successfully.")

            return {
                "message": data["message"],
                "cta": data["cta"],
                "send_as": data["send_as"],
                "rationale": data["rationale"]
            }

        except json.JSONDecodeError:

            logger.exception("Gemini returned invalid JSON.")

            return {
                "message": "Unable to generate message.",
                "cta": "Visit us",
                "send_as": "whatsapp",
                "rationale": "Gemini returned invalid JSON."
            }

        except Exception as e:

            logger.exception("LLM generation failed.")

            return {
                "message": "Unable to generate message.",
                "cta": "Visit us",
                "send_as": "whatsapp",
                "rationale": str(e)
            }