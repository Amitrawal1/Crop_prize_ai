from sqlalchemy.orm import Session

from app.models.price_history import PriceHistory


class PriceHistoryRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(
        self,
        row: PriceHistory,
    ):

        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)

        return row