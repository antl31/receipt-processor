from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class ItemRequest(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel)

    short_description: str
    price: float
