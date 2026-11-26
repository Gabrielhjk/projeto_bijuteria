from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.production_historic import ProductionHistoric
from sqlalchemy import Enum, DateTime, ForeignKey
from datetime import datetime
from zoneinfo import ZoneInfo
from ..db.enums.status import StatusEnum
from ..db import Base
from typing import List

zone_info = ZoneInfo("America/Sao_Paulo")

class Production(Base):
    __tablename__ = "production"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    current_stage_id: Mapped[int] = mapped_column(ForeignKey("stages.id"))
    amount: Mapped[int]
    status: Mapped[Enum] = mapped_column(Enum(StatusEnum))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), datetime.now(zone_info))
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), datetime.now(zone_info))
    completion_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), datetime.now(zone_info))

    productions_historic: Mapped[List["ProductionHistoric"]] = relationship()