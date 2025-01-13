from typing import Any

from sqlmodel import Session

from app.models import Item


class ItemRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, items_: list[dict[str, Any]]) -> list[Item]:
        items = []
        for item_data in items_:
            items.append(
                Item(  # type: ignore
                    description=item_data["short_description"], price=item_data["price"]
                )
            )
        return items
