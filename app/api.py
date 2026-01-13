"""
API Endpoints

This file defines all /api routes for the CFO context demo.
"""

from fastapi import APIRouter
from app.context.builder import build_context_snapshot

router = APIRouter()


@router.get("/clients/{client_id}/context")
def get_client_context(client_id: str):
    """
    Return a CFO-ready context snapshot for the given client.
    """
    snapshot = build_context_snapshot(client_id)
    return snapshot.model_dump()  # Pydantic V2 safe dictionary