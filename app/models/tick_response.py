from pydantic import BaseModel


class TickResponse(BaseModel):

    message: str

    cta: str

    send_as: str

    rationale: str