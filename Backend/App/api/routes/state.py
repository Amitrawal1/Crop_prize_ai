from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.models.state import State

router = APIRouter()


@router.get("/states")
def get_states(
    db: Session = Depends(get_db),
):

    states = db.query(State).all()

    return states