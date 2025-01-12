import uuid
from typing import Any, Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.db import SessionDep
from app.models import Receipt
from app.repository.item import ItemRepository
from app.repository.receipt import ReceiptRepository
from app.serializers.receipt import ReceiptRequest, ReceiptResponse

router = APIRouter(prefix="/receipts", tags=["receipts"])


# @router.get("/{id}", response_model=ItemPublic)
# def read_item(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
#     """
#     Get item by ID.
#     """
#     item = session.get(Item, id)
#         if not item:
#             raise HTTPException(status_code=404, detail="Item not found")

#     return item


@router.post("/process", response_model=ReceiptResponse)
def process_receipt(
    *,
    session: SessionDep,
    rec_repository:  Annotated[ReceiptRepository, Depends(ReceiptRepository)],
    item_repository:  Annotated[ItemRepository, Depends(ItemRepository)],
    receipt_in: ReceiptRequest,
) -> Any:
    items = item_repository.create(receipt_in.model_dump()["items"])
    session.add_all(items)
    instance = rec_repository.create(receipt_in.model_dump(),items)
    session.add(instance)

    session.commit()
    return {"id": instance.id}
