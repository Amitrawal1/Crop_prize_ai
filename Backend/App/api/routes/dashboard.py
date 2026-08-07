from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.repositories.market_repository import MarketRepository
from app.schemas.dashboard import DashboardRequest
from app.services.agmarknet.client import AgmarknetClient

router = APIRouter()


@router.post("/dashboard")
def get_dashboard(
    request: DashboardRequest,
    db: Session = Depends(get_db),
):

    market_repository = MarketRepository(db)

    markets = market_repository.get_markets_by_district(
        request.district_id,
    )

    market_ids = [market.id for market in markets]

    client = AgmarknetClient()

    payload = client.build_dashboard_payload(
        date=request.date,
        group=[100000],
        commodity=[request.commodity_id],
        variety=request.variety_id,
        state=request.state_id,
        district=[request.district_id],
        market=market_ids,
        grades=[request.grade_id],
    )

    data = client.get_dashboard_data(payload)

    if data["status"] != "success":
        return {
            "status": False,
            "message": data["message"],
            "records": [],
        }

    return {
        "status": True,
        "message": data["message"],
        "records": data["data"]["records"],
    }