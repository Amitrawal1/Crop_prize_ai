from sqlalchemy.orm import Session

from app.models.district import District


class DistrictRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_district(
        self,
        district_id: int,
        district_name: str,
        state_id: int,
    ) -> District:

        existing = self.db.get(District, district_id)

        if existing:
            return existing

        district = District(
            id=district_id,
            district_name=district_name,
            state_id=state_id,
        )

        self.db.add(district)
        self.db.commit()
        self.db.refresh(district)

        return district