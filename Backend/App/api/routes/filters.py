from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db

from app.models.state import State
from app.models.district import District
from app.models.market import Market
from app.models.commodity import Commodity
from app.models.commodity_group import CommodityGroup

router = APIRouter()


@router.get("/filters")
def get_filters(
    db: Session = Depends(get_db),
):

    return {
        "states": db.query(State).all(),
        "districts": db.query(District).all(),
        "markets": db.query(Market).all(),
        "commodity_groups": db.query(CommodityGroup).all(),
        "commodities": db.query(Commodity).all(),
    }