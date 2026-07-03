from typing import Optional

from pydantic import BaseModel


class ComposeRequest(BaseModel):

    merchant_id: str

    trigger_id: str

    customer_id: Optional[str] = None