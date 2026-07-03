from typing import List
from pydantic import BaseModel


class CustomerIdentity(BaseModel):
    name: str
    phone_redacted: str
    language_pref: str
    age_band: str


class Relationship(BaseModel):
    first_visit: str
    last_visit: str
    visits_total: int
    services_received: List[str]
    lifetime_value: int


class Preferences(BaseModel):
    preferred_slots: str
    channel: str
    reminder_opt_in: bool


class Consent(BaseModel):
    opted_in_at: str
    scope: List[str]


class CustomerContext(BaseModel):
    customer_id: str
    merchant_id: str

    identity: CustomerIdentity
    relationship: Relationship

    state: str

    preferences: Preferences

    consent: Consent