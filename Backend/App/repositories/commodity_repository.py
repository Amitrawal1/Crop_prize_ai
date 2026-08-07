from sqlalchemy.orm import Session

from app.models.commodity import Commodity


class CommodityRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_commodity(
        self,
        commodity_id: int,
        commodity_name: str,
        commodity_group_id: int,
        commodity_type: str | None,
    ) -> Commodity:

        existing = self.db.get(
            Commodity,
            commodity_id,
        )

        if existing:
            return existing

        commodity = Commodity(
            id=commodity_id,
            commodity_name=commodity_name,
            commodity_group_id=commodity_group_id,
            commodity_type=commodity_type,
        )

        self.db.add(commodity)
        self.db.commit()
        self.db.refresh(commodity)

        return commodity
    