from typing import Any

from app.models import Item


class ItemRepository:
    model = Item

    def create(self, items_: list[dict[str, Any]]) -> list[Item]:
        items = []
        for item_data in items_:
            items.append(
                self.model(
                    description=item_data["short_description"], price=item_data["price"]
                )
            )
        return items
