from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class CommodityGroup(Base):

    __tablename__ = "commodity_groups"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    group_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )