from app.database.connection import SessionLocal
from app.models.commodity_group import CommodityGroup


def main():

    db = SessionLocal()

    groups = db.query(CommodityGroup).all()

    print(f"Total Commodity Groups: {len(groups)}")
    print()

    for group in groups:
        print(group.id, "-", group.group_name)

    db.close()


if __name__ == "__main__":
    main()