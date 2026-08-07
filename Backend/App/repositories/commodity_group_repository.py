from sqlalchemy.orm import Session

from app.models.commodity_group import CommodityGroup


class CommodityGroupRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_group(
        self,
        group_id: int,
        group_name: str,
    ):

        existing = self.db.get(
            CommodityGroup,
            group_id,
        )

        if existing:
            return existing

        group = CommodityGroup(
            id=group_id,
            group_name=group_name,
        )

        self.db.add(group)
        self.db.commit()
        self.db.refresh(group)

        return group