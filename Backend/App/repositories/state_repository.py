from sqlalchemy.orm import Session

from app.models.state import State


class StateRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_state(
        self,
        state_id: int,
        state_name: str,
    ) -> State:

        existing = self.db.get(State, state_id)

        if existing:
            return existing

        state = State(
            id=state_id,
            state_name=state_name,
        )

        self.db.add(state)
        self.db.commit()
        self.db.refresh(state)

        return state
    