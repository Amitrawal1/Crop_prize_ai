from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class State(Base):

    __tablename__ = "states"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    state_name: Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False,
    )