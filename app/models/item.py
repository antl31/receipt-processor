import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models import Receipt


class ReceiptItems(SQLModel, table=True):
    __tablename__ = "receipt_items"  # type: ignore

    item_id: int = Field(foreign_key="item.id", primary_key=True)
    receipt_id: uuid.UUID = Field(foreign_key="receipt.id", primary_key=True)


class Item(SQLModel, table=True):
    __tablename__ = "item"  # type: ignore

    id: int = Field(primary_key=True)
    description: str = Field(nullable=False)
    price: float = Field(nullable=False)

    receipts: list["Receipt"] = Relationship(
        back_populates="items", link_model=ReceiptItems
    )
