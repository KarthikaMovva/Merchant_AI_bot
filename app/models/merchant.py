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

    days_remaining: Optional[int] = None
    renewed_at: Optional[str] = None
    days_since_expiry: Optional[int] = None


class PerformanceDelta(BaseModel):
    views_pct: Optional[float] = None
    calls_pct: Optional[float] = None
    ctr_pct: Optional[float] = None


class PerformanceSnapshot(BaseModel):
    window_days: Optional[int] = None
    views: Optional[int] = None
    calls: Optional[int] = None
    directions: Optional[int] = None
    ctr: Optional[float] = None
    leads: Optional[int] = None

    delta_7d: Optional[PerformanceDelta] = None


class MerchantOffer(BaseModel):
    id: str
    title: str
    status: str

    started: Optional[str] = None
    ended: Optional[str] = None


class CustomerAggregate(BaseModel):
    total_unique_ytd: Optional[int] = None

    lapsed_180d_plus: Optional[int] = None
    retention_6mo_pct: Optional[float] = None

    retention_3mo_pct: Optional[float] = None
    repeat_customer_pct: Optional[float] = None
    monthly_churn_pct: Optional[float] = None

    high_risk_adult_count: Optional[int] = None


class ReviewTheme(BaseModel):
    theme: Optional[str] = None
    sentiment: Optional[str] = None
    occurrences_30d: Optional[int] = None

    common_quote: Optional[str] = None


class MerchantContext(BaseModel):
    merchant_id: str
    category_slug: str

    identity: MerchantIdentity

    subscription: Optional[Subscription] = None

    performance: Optional[PerformanceSnapshot] = None

    offers: List[MerchantOffer] = []

    conversation_history: List[dict] = []

    customer_aggregate: Optional[CustomerAggregate] = None

    signals: List[str] = []

    review_themes: List[ReviewTheme] = []