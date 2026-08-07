from app.database.connection import SessionLocal
from app.models.market import Market


def main():

    db = SessionLocal()

    markets = db.query(Market).all()

    print(f"Total Markets: {len(markets)}")
    print()

    for market in markets[:20]:

        print(
            market.id,
            "-",
            market.market_name,
            "- District:",
            market.district_id,
        )

    db.close()


if __name__ == "__main__":
    main()
    