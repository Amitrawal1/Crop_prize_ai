from app.database.connection import SessionLocal
from app.models.district import District


def main() -> None:

    db = SessionLocal()

    districts = db.query(District).all()

    print(f"Total Districts: {len(districts)}")
    print()

    for district in districts[:20]:
        print(
            district.id,
            "-",
            district.district_name,
            "- State ID:",
            district.state_id,
        )

    db.close()


if __name__ == "__main__":
    main()