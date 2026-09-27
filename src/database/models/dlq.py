"""
model de dlq
"""

from src.database.base import Base 
from sqlalchemy import String, DateTime, BOOLEAN, Text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
class Dlq(Base):

    __tablename__ = "dlq"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    session_id: Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    status: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    


