import json

from app.models.request import ComposeRequest
from app.models.response import ComposeResponse
from app.services.llm_service import LLMService
from app.services.prompt_builder import PromptBuilder


class Composer:

    def __init__(self):
        self.llm = LLMService()

    def compose(self, request: ComposeRequest) -> ComposeResponse:

        prompt = PromptBuilder.build(request)

        result = self.llm.generate(prompt)

        response = json.loads(result)

        return ComposeResponse(**response)