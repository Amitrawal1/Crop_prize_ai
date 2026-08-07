from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class District(Base):

    __tablename__ = "districts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    district_name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    state_id: Mapped[int] = mapped_column(
        ForeignKey("states.id"),
        nullable=False,
    )