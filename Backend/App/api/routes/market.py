from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.market import Market

router = APIRouter()


@router.get("/markets")
def get_markets(
    district_id: int | None = None,
    db: Session = Depends(get_db),
):

    query = db.query(Market)

    if district_id is not None:
        query = query.filter(Market.district_id == district_id)

    return query.all()