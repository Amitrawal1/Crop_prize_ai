from app.database.connection import SessionLocal
from app.models.commodity import Commodity


def main():

    db = SessionLocal()

    commodities = db.query(Commodity).all()

    print(f"Total Commodities: {len(commodities)}")
    print()

    for commodity in commodities:
        print(
            commodity.id,
            "-",
            commodity.commodity_name,
            "- Group:",
            commodity.commodity_group_id,
            "- Type:",
            commodity.commodity_type,
        )

    db.close()


if __name__ == "__main__":
    main()