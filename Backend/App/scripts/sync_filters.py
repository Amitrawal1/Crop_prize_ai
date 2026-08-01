from app.database.connection import SessionLocal

from app.repositories.state_repository import StateRepository
from app.repositories.district_repository import DistrictRepository
from app.repositories.market_repository import MarketRepository
from app.repositories.commodity_group_repository import CommodityGroupRepository
from app.repositories.commodity_repository import CommodityRepository


from app.services.agmarknet.client import AgmarknetClient


def main() -> None:

    client = AgmarknetClient()

    db = SessionLocal()

    state_repository = StateRepository(db)
    district_repository = DistrictRepository(db)
    market_repository = MarketRepository(db)
    commodity_group_repository = CommodityGroupRepository(db)
    commodity_repository = CommodityRepository(db)

    filters = client.get_filters()
    
    grades = filters["data"]["grade_data"]

    print(grades[0])
    print(grades[1])

    return
    
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

    # --------------------
    # Sync Markets
    # --------------------

    markets = filters["data"]["market_data"]

    print(f"Found {len(markets)} markets")

    for market in markets:

        # Skip "All Markets"
        if market["district_id"] is None:
            continue

        market_repository.create_market(
            market_id=market["id"],
            market_name=market["mkt_name"],
            district_id=market["district_id"],
        )
    
    # --------------------
    # Sync Commodity Groups
    # --------------------

    groups = filters["data"]["cmdt_group_data"]

    print(f"Found {len(groups)} commodity groups")

    for group in groups:

        # Skip "All Commodity Groups"
        if group["id"] == 100000:
            continue

        commodity_group_repository.create_group(
            group_id=group["id"],
            group_name=group["cmdt_grp_name"],
        )
    
    # --------------------
    # Sync Commodities
    # --------------------

    commodities = filters["data"]["cmdt_data"]

    print(f"Found {len(commodities)} commodities")

    for commodity in commodities:

        # Skip "All Commodities"
        if commodity["cmdt_group_id"] is None:
            continue

        commodity_repository.create_commodity(
            commodity_id=commodity["cmdt_id"],
            commodity_name=commodity["cmdt_name"],
            commodity_group_id=commodity["cmdt_group_id"],
            commodity_type=commodity["cmdt_type_flag"],
        )
        
    db.close()

    print("Synchronization completed.")


if __name__ == "__main__":
    main()