import datetime
import math
from enum import IntEnum

from app.models import Item, Receipt


class RewardPoints(IntEnum):
    RETAILER_NAME = 1
    ROUND_TOTAL = 50
    TOTAL_MULTIPLY_BY_25 = 25
    EVERY_TWO_ITEMS = 5
    ODD_DATE = 6
    PURCHASE_TIME = 10


TOTAL_MULTIPLIER = 0.25
ITEM_DESCRIPTION_LENGTH_MULTIPLIER = 3
ITEM_PRICE_MULTIPLIER = 0.2
PURCHASE_TIME_START, PURCHASE_TIME_END = 14, 16  # 24-hrs format


class RewardsCalculator:
    def __init__(self, receipt: Receipt):
        self.receipt = receipt

    def _process_retailer_name(self, name: str) -> int:
        counter = 0
        for char in name:
            if char.isalnum():
                counter += RewardPoints.RETAILER_NAME
        return counter

    def _process_total(self, total: float) -> int:
        res = 0
        if total.is_integer():
            res += RewardPoints.ROUND_TOTAL
        if (total / TOTAL_MULTIPLIER).is_integer():
            res += RewardPoints.TOTAL_MULTIPLY_BY_25
        return res

    def _process_items(self, items: list[Item]) -> int:
        res = (len(items) // 2) * RewardPoints.EVERY_TWO_ITEMS
        for item in items:
            if (
                len(item.description) / ITEM_DESCRIPTION_LENGTH_MULTIPLIER
            ).is_integer():
                res += math.floor(item.price * ITEM_PRICE_MULTIPLIER)
        return res

    def _process_datetime(self, datetime_: datetime.datetime) -> int:
        res = 0
        if datetime_.day % 2 != 0:
            res += RewardPoints.ODD_DATE
        if datetime_.hour in range(PURCHASE_TIME_START, PURCHASE_TIME_END + 1):
            res += RewardPoints.PURCHASE_TIME
        return res

    def calculate_rewards(self) -> int:
        return (
            +self._process_retailer_name(self.receipt.retailer)
            + self._process_total(self.receipt.total)
            + self._process_items(self.receipt.items)
            + self._process_datetime(self.receipt.purchase_at)
        )
