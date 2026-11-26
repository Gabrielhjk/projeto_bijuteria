from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import DateTime, ForeignKey
from datetime import datetime
from zoneinfo import ZoneInfo
from ..db import Base

zone_info = ZoneInfo("America/Sao_Paulo")

class ProductionHistoric(Base):
    __tablename__ = "production_historic"

    id: Mapped[int] = mapped_column(primary_key=True)
    production_id: Mapped[int] = mapped_column(ForeignKey("production.id"))
    stage_id: Mapped[int] = mapped_column(ForeignKey("stages.id"))
    entry_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), datetime.now(zone_info))
    exit_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), datetime.now(zone_info))