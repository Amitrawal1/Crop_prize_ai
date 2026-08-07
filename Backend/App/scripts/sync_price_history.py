from app.database.connection import SessionLocal

from app.services.dashboard.service import DashboardService


def main():

    db = SessionLocal()

    service = DashboardService(db)

    data = service.get_dashboard(
        state_id=34,
        district_id=586,
        commodity_id=1,
        variety_id=100021,
        grade_id=4,
        request_date="2026-08-01",
    )

    print(data["status"])
    print(data["message"])

    db.close()


if __name__ == "__main__":
    main()