import datetime
import uuid
from typing import List

from sqlmodel import Field, SQLModel, Relationship

from app.models import Item
from app.models.item import ReceiptItems


class Receipt(SQLModel, table=True):
    __tablename__ = "receipt"

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    retailer: str
    purchase_at: datetime.datetime
    total: float = Field(nullable=False)

    # items: list[Item] = Relationship(back_populates="receipts", link_model=receipt_item)
    items: List[Item] = Relationship(back_populates="receipts", link_model=ReceiptItems)