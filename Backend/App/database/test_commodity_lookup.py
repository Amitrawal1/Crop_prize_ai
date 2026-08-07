from app.database.connection import SessionLocal
from app.models.commodity import Commodity


def main():

    db = SessionLocal()

    commodities = db.query(Commodity).all()

    for commodity in commodities:
        print(
            commodity.id,
            "-",
            commodity.commodity_name,
        )

    db.close()


if __name__ == "__main__":
    main()