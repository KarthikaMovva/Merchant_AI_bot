from typing import Any, Dict, Optional
from pydantic import BaseModel


class TriggerContext(BaseModel):
    id: str

    scope: str
    kind: str
    source: str

    merchant_id: str
    customer_id: Optional[str] = None

    payload: Dict[str, Any] = {}

    urgency: int

    suppression_key: str

    expires_at: Optional[str] = None