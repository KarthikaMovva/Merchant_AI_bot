from app.services.data_loader import dataset
from app.services.llm_service import LLMService
from app.services.prompt_builder import PromptBuilder


class MessageService:

    def __init__(self):

        self.loader = dataset

        self.prompt_builder = PromptBuilder()

        self.llm = LLMService()

    def compose(
        self,
        merchant_id: str,
        trigger_id: str,
        customer_id: str | None = None,
    ) -> dict:

        merchant = self.loader.get_merchant(merchant_id)

        if merchant is None:
            raise ValueError("Merchant not found.")

        category = self.loader.get_category(
            merchant.category_slug
        )

        if category is None:
            raise ValueError("Category not found.")

        trigger = self.loader.get_trigger(trigger_id)

        if trigger is None:
            raise ValueError("Trigger not found.")

        customer = None

        if customer_id:
            customer = self.loader.get_customer(customer_id)

        prompt = self.prompt_builder.build(
            category=category,
            merchant=merchant,
            trigger=trigger,
            customer=customer,
        )

        response = self.llm.generate(prompt)

        return response