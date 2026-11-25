from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, DateTime
from models.production import production
from datetime import datetime
from zoneinfo import ZoneInfo
from nanoid import generate
from ..db import Base
from typing import List

zone_info = ZoneInfo("America/Sao_Paulo")

class products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(100))
    product_code: Mapped[str] = mapped_column(String(8), unique=True, default=lambda: generate('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', 8))
    description: Mapped[str] = mapped_column(String(250))
    active: Mapped[Boolean] = mapped_column(default=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), datetime.now(zone_info))
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), datetime.now(zone_info))

    productions: Mapped[List["production"]] = relationship()