from pydantic import BaseModel
from typing import Optional

class TickRequest(BaseModel):
    merchant_id: str
    trigger_id: str
    customer_id: Optional[str] = None