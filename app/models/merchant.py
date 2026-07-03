from typing import List, Optional
from pydantic import BaseModel


class MerchantIdentity(BaseModel):
    name: str
    city: str
    locality: str
    place_id: str
    verified: bool
    languages: List[str]
    owner_first_name: Optional[str] = None
    established_year: Optional[int] = None


class Subscription(BaseModel):
    status: str
    plan: str
    days_remaining: int
    days_since_expiry: Optional[int] = None


class PerformanceDelta(BaseModel):
    views_pct: float
    calls_pct: float
    ctr_pct: float


class PerformanceSnapshot(BaseModel):
    window_days: int
    views: int
    calls: int
    directions: int
    ctr: float
    leads: int
    delta_7d: PerformanceDelta


class MerchantOffer(BaseModel):
    id: str
    title: str
    status: str
    started: Optional[str] = None
    ended: Optional[str] = None


class CustomerAggregate(BaseModel):
    total_unique_ytd: int
    lapsed_180d_plus: int
    retention_6mo_pct: float
    high_risk_adult_count: int

class ReviewTheme(BaseModel):
    theme: str
    sentiment: str
    occurrences_30d: int
    common_quote: str


class MerchantContext(BaseModel):
    merchant_id: str
    category_slug: str

    identity: MerchantIdentity
    subscription: Subscription
    performance: PerformanceSnapshot

    offers: List[MerchantOffer]

    conversation_history: List[dict]

    customer_aggregate: CustomerAggregate

    signals: List[str]

    review_themes: List[ReviewTheme]