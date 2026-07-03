from typing import Literal

from pydantic import BaseModel


class ComposeResponse(BaseModel):

    body: str

    cta: str

    send_as: Literal[
        "vera",
        "merchant_on_behalf",
    ]

    suppression_key: str

    rationale: str


class HealthResponse(BaseModel):

    status: str