import datetime
import uuid

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

from app.schemas.item import ItemRequest


class ReceiptRequest(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    retailer: str
    purchase_date: datetime.date
    purchase_time: datetime.time
    total: float
    items: list[ItemRequest] = Field(min_length=1)


class ReceiptResponse(BaseModel):
    id: uuid.UUID
