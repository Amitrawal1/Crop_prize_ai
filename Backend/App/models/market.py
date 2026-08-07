from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Market(Base):

    __tablename__ = "markets"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    market_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    district_id: Mapped[int] = mapped_column(
        ForeignKey("districts.id"),
        nullable=False,
    )