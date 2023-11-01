from typing import List, Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from .database import Base

class Item(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), index=True)
    count: Mapped[int]
    price: Mapped[float]
    
    def __repr__(self) -> str:
        return f"Item(id={self.id!r}, name={self.name!r}, count={self.count!r}, price={self.price!r})"