from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from datetime import datetime
from zoneinfo import ZoneInfo
from ..db import Base

zone_info = ZoneInfo("America/Sao_Paulo")

class users(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(120), unique=True)
    senha: Mapped[str]
    created_at = Mapped[DateTime] = mapped_column(DateTime(timezone=True), datetime.now(zone_info))
