from app.database.connection import SessionLocal
from app.repositories.market_repository import MarketRepository
from app.repositories.dashboard_repository import DashboardRepository

from app.services.agmarknet.client import AgmarknetClient


def main():

    client = AgmarknetClient()

    db = SessionLocal()

    market_repository = MarketRepository(db)
    dashboard_repository = DashboardRepository(db)

    markets = market_repository.get_markets_by_district(586)

    market_ids = [market.id for market in markets]

    payload = client.build_dashboard_payload(
        date="2026-08-01",
        group=[100000],
        commodity=[1],
        variety=100021,
        state=34,
        district=[586],
        market=market_ids,
        grades=[4],
    )

    print(payload)
    print()

    data = client.get_dashboard_data(payload)

    print(data["status"])
    print(data["message"])

    if data["status"] != "success":
        db.close()
        return

    records = data["data"]["records"]

    print(f"Total Records: {len(records)}")
    print()

    for record in records:

        dashboard_repository.create_dashboard_data(record)

        print(record)

    print()
    print("Dashboard data saved successfully.")


if __name__ == "__main__":
    main()