from app.database.connection import SessionLocal
from app.models.state import State


def main() -> None:

    db = SessionLocal()

    states = db.query(State).all()

    print(f"Total States: {len(states)}")
    print()

    for state in states:
        print(state.id, "-", state.state_name)

    db.close()


if __name__ == "__main__":
    main()