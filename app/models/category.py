from pydantic import ConfigDict
from typing import List, Optional
from pydantic import BaseModel


from pydantic import BaseModel, Field

class VoiceProfile(BaseModel):
    tone: str
    register_style: str = Field(alias="register")
    code_mix: str

    vocab_allowed: list[str]
    vocab_taboo: list[str]

    salutation_examples: list[str]
    tone_examples: list[str]

    model_config = {
        "populate_by_name": True
    }


class OfferTemplate(BaseModel):
    id: str
    title: str
    value: str
    audience: str
    type: str


class PeerStats(BaseModel):
    scope: str

    avg_rating: float
    avg_review_count: int

    avg_views_30d: int
    avg_calls_30d: int
    avg_directions_30d: int

    avg_ctr: float

    avg_photos: int
    avg_post_freq_days: int

    retention_6mo_pct: Optional[float] = None
    retention_3mo_pct: Optional[float] = None

    monthly_churn_pct: Optional[float] = None
    delivery_share_pct: Optional[float] = None
    repeat_customer_pct: Optional[float] = None
    trial_to_paid_pct: Optional[float] = None


class DigestItem(BaseModel):
    id: str
    kind: str
    title: str
    source: str

    summary: str
    actionable: str

    trial_n: Optional[int] = None
    patient_segment: Optional[str] = None


class SeasonalBeat(BaseModel):
    month: str
    note: str


class TrendSignal(BaseModel):
    title: str
    summary: str


class CategoryContext(BaseModel):

    slug: str
    display_name: str

    voice: VoiceProfile

    offer_catalog: list[OfferTemplate]

    peer_stats: PeerStats

    digest: list[DigestItem]

    seasonal_beats: list = []

    trend_signals: list = []

    patient_content_library: list = []

    model_config = ConfigDict(extra="allow")