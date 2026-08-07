from app.database.connection import SessionLocal
from app.models.market import Market


def main():

    db = SessionLocal()

    markets = (
        db.query(Market)
        .filter(Market.id.in_([297, 2194]))
        .all()
    )

    for market in markets:
        print(
            market.id,
            market.market_name,
            market.district_id,
        )

    db.close()


if __name__ == "__main__":
    main()