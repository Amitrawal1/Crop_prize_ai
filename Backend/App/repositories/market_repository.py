from sqlalchemy.orm import Session

from app.models.market import Market


class MarketRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_market(
        self,
        market_id: int,
        market_name: str,
        district_id: int,
    ) -> Market:

        existing = self.db.get(
            Market,
            market_id,
        )

        if existing:
            return existing

        market = Market(
            id=market_id,
            market_name=market_name,
            district_id=district_id,
        )
        
    def get_markets_by_district(
        self,
        district_id: int,
    ):
        return (
            self.db.query(Market)
            .filter(Market.district_id == district_id)
            .all()
        )

        self.db.add(market)

        self.db.commit()

        self.db.refresh(market)

        return market