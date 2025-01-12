import datetime
import uuid

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from app.serializers.item import ItemRequest


class ReceiptRequest(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    retailer: str
    purchase_date: datetime.date
    purchase_time: datetime.time
    total: float
    items: list[ItemRequest]


class ReceiptResponse(BaseModel):
    id: uuid.UUID
