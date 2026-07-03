from app.services.data_loader import dataset
from app.services.llm_service import LLMService


class MessageService:

    def __init__(self):
        self.llm = LLMService()

    def compose(
        self,
        merchant_id: str,
        trigger_id: str,
        customer_id: str | None = None,
    ):

        merchant = dataset.get_merchant(merchant_id)

        if merchant is None:
            raise ValueError(f"Merchant {merchant_id} not found")

        trigger = dataset.get_trigger(trigger_id)

        if trigger is None:
            raise ValueError(f"Trigger {trigger_id} not found")

        customer = dataset.get_customer(customer_id)

        category = dataset.get_category(
            merchant["category_slug"]
        )

        merchant_name = merchant["identity"]["name"]
        merchant_city = merchant["identity"]["city"]
        category_name = category.get("name", "")
        trigger_name = trigger.get("name", "")
        trigger_description = trigger.get("description", "")

        prompt = f"""
You are an AI marketing assistant used by local businesses.

Your task:

Generate one highly personalized outreach message.

Requirements:

• Below 70 words
• Friendly
• Professional
• Include one CTA
• Mention merchant naturally
• Do not exaggerate
• Do not use markdown
• Return ONLY JSON

Schema:

{{
    "message":"...",
    "cta":"...",
    "send_as":"whatsapp",
    "rationale":"..."
}}

Merchant

Merchant:
{merchant_name}

Category:
{category_name}

City:
{merchant_city}

Trigger:
{trigger_name}

Description:
{trigger_description}

Customer:
{customer if customer else "General Customer"}


Keep message below 70 words.

Professional.

Actionable.

Engaging.
"""

        return self.llm.generate(prompt)