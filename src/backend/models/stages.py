from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.production_historic import ProductionHistoric
from models.production import Production
from sqlalchemy import String
from typing import List
from ..db import Base

class Stages(Base):
    __tablename__ = "stages"

    id: Mapped[int] = mapped_column(primary_key=True)
    stage_name: Mapped[str] = mapped_column(String(50))

    productions_historic: Mapped[List["ProductionHistoric"]] = relationship()
    productions: Mapped[List["Production"]] = relationship()