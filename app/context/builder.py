"""
Context Builder

This module constructs a CFO-ready Context Snapshot for a given client.

This is a meaning-making layer:
- Interprets financial state
- Highlights what changed
- Surfaces risks and open questions
- Produces a calm, call-ready briefing
"""

from datetime import datetime
from typing import List, Dict
from pydantic import BaseModel


# ---------------- Pydantic Models ----------------

class Alert(BaseModel):
    type: str
    severity: str
    message: str


class OpenDecision(BaseModel):
    id: str
    question: str
    severity: str


class LastInteraction(BaseModel):
    type: str
    date: str
    summary: str


class ContextSnapshot(BaseModel):
    client_id: str
    generated_at: str
    headline: str
    alerts: List[Alert]
    key_metrics: Dict
    recent_changes: List[str]
    open_decisions: List[OpenDecision]
    last_interaction: LastInteraction


# ---------------- Builder Function ----------------

def build_context_snapshot(client_id: str) -> ContextSnapshot:
    # Demo historical metrics (previous month)
    previous_metrics = {
        "cash_balance": 4000000.0,
        "monthly_burn": 750000.0,
        "runway_months": 5.3,
        "revenue_mom_growth": 0.05,
        "aws_spend": 42000.0,
        "payroll": 480000.0,
        "marketing": 70000.0
    }

    # Demo current metrics
    current_metrics = {
        "cash_balance": 4200000.0,
        "monthly_burn": 810000.0,
        "runway_months": 5.2,
        "revenue_mom_growth": 0.06,
        "days_since_last_contact": 7.0,
        "aws_spend": 50000.0,
        "payroll": 500000.0,
        "marketing": 75000.0
    }

    # Detect recent changes
    recent_changes = []
    for k, v in current_metrics.items():
        prev = previous_metrics.get(k)
        if prev is not None and v != prev:
            if isinstance(v, float):
                pct_change = (v - prev) / prev * 100
                recent_changes.append(f"{k.replace('_',' ').title()} changed from {prev} to {v} ({pct_change:.1f}% MoM)")
            else:
                recent_changes.append(f"{k.replace('_',' ').title()} changed from {prev} to {v}")

    # Generate alerts
    alerts = []
    if current_metrics["runway_months"] < 6:
        alerts.append(Alert(
            type="runway",
            severity="high",
            message=f"Cash runway at {current_metrics['runway_months']} months"
        ))
    if current_metrics["revenue_mom_growth"] < 0.01:
        alerts.append(Alert(
            type="revenue",
            severity="medium",
            message=f"Revenue growth is low: {current_metrics['revenue_mom_growth']*100:.1f}% MoM"
        ))

    # Headline picks the most urgent alert
    headline = alerts[0].message + " — focus on burn control before growth" if alerts else "All metrics healthy"

    # Static demo open decisions
    open_decisions = [
        OpenDecision(id="dec_001", question="Approve Q2 hiring plan?", severity="high")
    ]

    # Static last interaction
    last_interaction = LastInteraction(
        type="client_call",
        date="2026-01-05",
        summary="Discussed burn rate and Q1 hiring plan"
    )

    # Build snapshot
    snapshot = ContextSnapshot(
        client_id=client_id,
        generated_at=datetime.utcnow().isoformat(),  # ISO string for Pydantic V2
        headline=headline,
        alerts=alerts,
        key_metrics=current_metrics,
        recent_changes=recent_changes,
        open_decisions=open_decisions,
        last_interaction=last_interaction
    )

    return snapshot


# ---------------- Demo Run ----------------
if __name__ == "__main__":
    snapshot = build_context_snapshot("client_acme")
    print(snapshot.model_dump_json(indent=2))  # Pydantic V2 safe