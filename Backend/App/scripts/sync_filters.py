from app.database.connection import SessionLocal
from app.repositories.state_repository import StateRepository
from app.repositories.district_repository import DistrictRepository
from app.services.agmarknet.client import AgmarknetClient


def main() -> None:

    client = AgmarknetClient()

    db = SessionLocal()

    state_repository = StateRepository(db)
    district_repository = DistrictRepository(db)

    filters = client.get_filters()

    # --------------------
    # Sync States
    # --------------------

    states = filters["data"]["state_data"]

    print(f"Found {len(states)} states")

    for state in states:

        state_repository.create_state(
            state_id=state["state_id"],
            state_name=state["state_name"],
        )

    # --------------------
    # Sync Districts
    # --------------------

    districts = filters["data"]["district_data"]

    print(f"Found {len(districts)} districts")

    for district in districts:

        # Skip "All Districts"
        if district["state_id"] is None:
            continue

        district_repository.create_district(
            district_id=district["id"],
            district_name=district["district_name"],
            state_id=district["state_id"],
        )

    db.close()

    print("Synchronization completed.")


if __name__ == "__main__":
    main()