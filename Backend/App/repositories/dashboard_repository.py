from sqlalchemy.orm import Session

from app.models.dashboard_data import DashboardData


class DashboardRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_dashboard_record(
        self,
        commodity_name: str,
        reported_date: str,
    ):

        return (
            self.db.query(DashboardData)
            .filter(
                DashboardData.commodity_name == commodity_name,
                DashboardData.reported_date == reported_date,
            )
            .first()
        )

    def create_dashboard_data(
        self,
        record: dict,
    ):

        existing = self.get_dashboard_record(
            commodity_name=record["cmdt_name"],
            reported_date=record["reported_date"],
        )

        if existing:
            return existing

        row = DashboardData(
            commodity_name=record["cmdt_name"],
            commodity_group=record["cmdt_grp_name"],
            trend=record["trend"],
            reported_date=record["reported_date"],
            msp_price=float(record["msp_price"]),
            current_price=float(record["as_on_price"]),
            current_arrival=float(record["as_on_arrival"]),
            one_day_price=float(record["one_day_ago_price"]),
            two_day_price=float(record["two_day_ago_price"]),
            one_day_arrival=float(record["one_day_ago_arrival"]),
            two_day_arrival=float(record["two_day_ago_arrival"]),
        )

        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)

        return row