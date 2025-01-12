import datetime
from typing import Any

from app.models import Receipt, Item


class ReceiptRepository:
    model = Receipt

    def create(self, data: dict[str, Any], items: list[Item]) -> Receipt:
        purchase_at = datetime.datetime.combine(
            data["purchase_date"], data["purchase_time"]
        )
        receipt = self.model(
            retailer=data["retailer"],
            purchase_at=purchase_at,
            total=data["total"],
            items=items,
        )
        return receipt
