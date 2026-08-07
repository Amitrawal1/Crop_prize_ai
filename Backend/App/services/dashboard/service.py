from sqlalchemy.orm import Session

from app.repositories.market_repository import MarketRepository
from app.services.agmarknet.client import AgmarknetClient


class DashboardService:

    def __init__(self, db: Session):

        self.db = db

        self.market_repository = MarketRepository(db)

        self.client = AgmarknetClient()

    def get_dashboard(
        self,
        state_id: int,
        district_id: int,
        commodity_id: int,
        variety_id: int,
        grade_id: int,
        date: str,
    ):

        markets = self.market_repository.get_markets_by_district(
            district_id,
        )

        market_ids = [market.id for market in markets]

        payload = self.client.build_dashboard_payload(
            date=date,
            group=[100000],
            commodity=[commodity_id],
            variety=variety_id,
            state=state_id,
            district=[district_id],
            market=market_ids,
            grades=[grade_id],
        )

        return self.client.get_dashboard_data(payload)