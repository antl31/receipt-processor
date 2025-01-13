import datetime
import uuid

from sqlmodel import Field, Relationship, SQLModel

from app.models import Item
from app.models.item import ReceiptItems


class Receipt(SQLModel, table=True):
    __tablename__ = "receipt"  # type: ignore

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    retailer: str
    purchase_at: datetime.datetime
    total: float = Field(nullable=False)

    items: list[Item] = Relationship(back_populates="receipts", link_model=ReceiptItems)
