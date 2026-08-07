from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.district import District

router = APIRouter()


@router.get("/districts")
def get_districts(
    state_id: int | None = None,
    db: Session = Depends(get_db),
):

    query = db.query(District)

    if state_id is not None:
        query = query.filter(District.state_id == state_id)

    return query.all()