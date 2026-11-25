from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.production_historic import production_historic
from models.production import production
from sqlalchemy import String
from typing import List
from ..db import Base

class stages(Base):
    __tablename__ = "stages"

    id: Mapped[int] = mapped_column(primary_key=True)
    stage_name: Mapped[str] = mapped_column(String(50))

    productions_historic: Mapped[List["production_historic"]] = relationship()
    productions: Mapped[List["production"]] = relationship()