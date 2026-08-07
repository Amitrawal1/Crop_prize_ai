from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class DashboardData(Base):

    __tablename__ = "dashboard_data"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    commodity_name: Mapped[str] = mapped_column(String)

    commodity_group: Mapped[str] = mapped_column(String)

    trend: Mapped[str] = mapped_column(String)

    reported_date: Mapped[str] = mapped_column(String)

    msp_price: Mapped[float] = mapped_column(Float)

    current_price: Mapped[float] = mapped_column(Float)

    current_arrival: Mapped[float] = mapped_column(Float)

    one_day_price: Mapped[float] = mapped_column(Float)

    two_day_price: Mapped[float] = mapped_column(Float)

    one_day_arrival: Mapped[float] = mapped_column(Float)

    two_day_arrival: Mapped[float] = mapped_column(Float)