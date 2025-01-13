import uuid
from typing import Any

from fastapi import APIRouter

from app.db import SessionDep
from app.schemas.receipt import ReceiptRequest, ReceiptResponse
from app.services.receipt import ReceiptService

router = APIRouter(prefix="/receipts", tags=["receipts"])


@router.get("/{id_}/points", response_model=dict[str, int])
def read_item(session: SessionDep, id_: uuid.UUID) -> Any:
    _service = ReceiptService(session)
    points = _service.get_points(id_)

    return {"points": points}


@router.post("/process", response_model=ReceiptResponse)
def process_receipt(
    *,
    session: SessionDep,
    receipt_in: ReceiptRequest,
) -> Any:
    _service = ReceiptService(session)
    instance = _service.create(receipt_in)

    return ReceiptResponse(**{"id": instance.id})
