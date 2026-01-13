from pydantic import BaseModel
from typing import List, Dict, Optional


class Alert(BaseModel):
    type: str  # e.g., "runway"
    severity: str  # "low", "medium", "high"
    message: str


class OpenDecision(BaseModel):
    id: str
    question: str
    severity: str  # "low", "medium", "high"


class LastInteraction(BaseModel):
    type: str  # e.g., "client_call"
    date: str  # YYYY-MM-DD
    summary: str


class ContextSnapshot(BaseModel):
    client_id: str
    generated_at: str  # ISO timestamp
    headline: str
    alerts: List[Alert]
    key_metrics: Dict[str, float]  # cash_balance, monthly_burn, runway_months, revenue_mom_growth, days_since_last_contact
    recent_changes: List[str]
    open_decisions: List[OpenDecision]
    last_interaction: LastInteraction