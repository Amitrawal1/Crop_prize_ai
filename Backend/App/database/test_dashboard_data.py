from app.database.connection import SessionLocal
from app.models.dashboard_data import DashboardData


def main():

    db = SessionLocal()

    rows = db.query(DashboardData).all()

    print(f"Total Rows: {len(rows)}")
    print()

    for row in rows:
        print(
            row.commodity_name,
            row.current_price,
            row.current_arrival,
            row.reported_date,
        )

    db.close()


if __name__ == "__main__":
    main()