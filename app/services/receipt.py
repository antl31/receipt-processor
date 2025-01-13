import uuid
from http import HTTPStatus

from fastapi import HTTPException
from sqlmodel import Session

from app.models import Receipt
from app.repository import ItemRepository, ReceiptRepository
from app.schemas import ReceiptRequest
from app.utils.caluclate_rewards import RewardsCalculator


class ReceiptService:
    """
    Service class for handling cities.
    """

    def __init__(self, session: Session):
        self.repository = ReceiptRepository(session)
        self.item_repository = ItemRepository(session)
        self.session = session

    def get_points(self, id_: uuid.UUID) -> int:
        receipt = self.repository.get_by_id(id_)
        if not receipt:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail="Receipt not found"
            )
        calculator = RewardsCalculator(receipt)

        return calculator.calculate_rewards()

    def create(self, receipt_in: ReceiptRequest) -> Receipt:
        items = self.item_repository.create(receipt_in.model_dump()["items"])
        self.session.add_all(items)
        instance = self.repository.create(receipt_in.model_dump(), items)
        self.session.add(instance)
        self.session.commit()
        return instance
