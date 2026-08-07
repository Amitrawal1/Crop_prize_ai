from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class PriceHistory(Base):

    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    commodity_name: Mapped[str] = mapped_column(String)

    market_name: Mapped[str] = mapped_column(String)

    district_name: Mapped[str] = mapped_column(String)

    state_name: Mapped[str] = mapped_column(String)

    reported_date: Mapped[str] = mapped_column(String)

    modal_price: Mapped[float] = mapped_column(Float)

    min_price: Mapped[float] = mapped_column(Float)

    max_price: Mapped[float] = mapped_column(Float)

    arrival: Mapped[float] = mapped_column(Float)