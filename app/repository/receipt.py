import datetime
import uuid
from typing import Any

from sqlmodel import Session, select

from app.models import Item, Receipt


class ReceiptRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, data: dict[str, Any], items: list[Item]) -> Receipt:
        purchase_at = datetime.datetime.combine(
            data["purchase_date"], data["purchase_time"]
        )
        receipt = Receipt(
            retailer=data["retailer"],
            purchase_at=purchase_at,
            total=data["total"],
            items=items,
        )
        return receipt

    def get_by_id(self, id_: uuid.UUID) -> Receipt | None:
        statement = select(Receipt).where(Receipt.id == id_)
        return self.session.exec(statement).first()
