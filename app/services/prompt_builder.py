from typing import Optional

from app.models.category import CategoryContext
from app.models.customer import CustomerContext
from app.models.merchant import MerchantContext
from app.models.trigger import TriggerContext


class PromptBuilder:
    """
    Builds the complete prompt that will be sent to Gemini.
    """

    def build(
        self,
        category: CategoryContext,
        merchant: MerchantContext,
        trigger: TriggerContext,
        customer: Optional[CustomerContext] = None,
    ) -> str:

        system_prompt = """
You are Vera, an expert AI assistant helping Indian merchants over WhatsApp.

Your task is to generate ONE WhatsApp message.

Strict Rules:

1. Use ONLY the provided context.
2. Never hallucinate any facts.
3. Never invent offers, statistics, competitors or research.
4. Mention the trigger naturally.
5. Match the merchant category voice.
6. Personalize using merchant information.
7. Use concrete numbers whenever available.
8. Keep the message concise (less than 120 words).
9. Use only ONE primary CTA.
10. Keep the tone conversational and professional.
11. Match the merchant language preference whenever possible.
12. Return ONLY valid JSON.

Required JSON format:

{
    "body": "...",
    "cta": "...",
    "send_as": "...",
    "suppression_key": "...",
    "rationale": "..."
}
"""

        category_prompt = f"""
========================
CATEGORY CONTEXT
========================

Category:
{category.display_name}

Voice Profile:
{category.voice.model_dump_json(indent=2)}

Peer Statistics:
{category.peer_stats.model_dump_json(indent=2)}

Offer Catalog:
{category.offer_catalog}

Research Digest:
{category.digest}
"""

        merchant_prompt = f"""
========================
MERCHANT CONTEXT
========================

Merchant Identity:
{merchant.identity.model_dump_json(indent=2)}

Subscription:
{merchant.subscription.model_dump_json(indent=2)}

Performance:
{merchant.performance.model_dump_json(indent=2)}

Offers:
{merchant.offers}

Conversation History:
{merchant.conversation_history}

Customer Aggregate:
{merchant.customer_aggregate.model_dump_json(indent=2)}

Signals:
{merchant.signals}

Review Themes:
{merchant.review_themes}
"""

        trigger_prompt = f"""
========================
TRIGGER CONTEXT
========================

Trigger ID:
{trigger.id}

Kind:
{trigger.kind}

Scope:
{trigger.scope}

Source:
{trigger.source}

Payload:
{trigger.payload}

Urgency:
{trigger.urgency}

Suppression Key:
{trigger.suppression_key}
"""

        customer_prompt = ""

        if customer is not None:
            customer_prompt = f"""
========================
CUSTOMER CONTEXT
========================

Identity:
{customer.identity.model_dump_json(indent=2)}

Relationship:
{customer.relationship.model_dump_json(indent=2)}

State:
{customer.state}

Preferences:
{customer.preferences.model_dump_json(indent=2)}

Consent:
{customer.consent.model_dump_json(indent=2)}
"""

        evaluation_prompt = """
========================
EVALUATION CRITERIA
========================

The generated message should maximize:

1. Specificity
2. Category Fit
3. Merchant Fit
4. Trigger Relevance
5. Merchant Engagement

Use:

• Specific numbers
• Merchant-specific personalization
• Category-specific terminology
• Appropriate offers
• Natural Hindi-English mix when appropriate
• Single CTA
"""

        output_prompt = """
========================
OUTPUT
========================

Return ONLY JSON.

No markdown.

No explanation.

No extra text.

JSON ONLY.
"""

        prompt = "\n".join(
            [
                system_prompt,
                category_prompt,
                merchant_prompt,
                trigger_prompt,
                customer_prompt,
                evaluation_prompt,
                output_prompt,
            ]
        )

        return prompt