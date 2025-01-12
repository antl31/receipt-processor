import uuid
from typing import List

from sqlalchemy import Column, ForeignKey, Table
from sqlmodel import Field, Relationship, SQLModel

# receipt_item = Table(
#     "receipt_item",
#     SQLModel.metadata,
#     Column("receipt_id", ForeignKey("receipt.id", ondelete="CASCADE"), primary_key=True),
#     Column("item_id", ForeignKey("item.id", ondelete="CASCADE"), primary_key=True),
# )


class ReceiptItems(SQLModel, table=True):
    __tablename__ = "receipt_items"

    item_id: int = Field(foreign_key="item.id", primary_key=True)
    receipt_id: uuid.UUID = Field(foreign_key="receipt.id", primary_key=True)


class Item(SQLModel, table=True):
    __tablename__ = "item"

    id: int = Field(primary_key=True)
    description: str = Field(nullable=False)
    price: float = Field(nullable=False)

    # Back reference to the Receipt model
    # receipts: list["Receipt"] = Relationship(back_populates="items", link_model=receipt_item)
    receipts: List["Receipt"] = Relationship(
        back_populates="items", link_model=ReceiptItems
    )
