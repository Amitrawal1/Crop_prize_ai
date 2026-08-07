from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Commodity(Base):

    __tablename__ = "commodities"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    commodity_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    commodity_type: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    commodity_group_id: Mapped[int] = mapped_column(
        ForeignKey("commodity_groups.id"),
        nullable=False,
    )