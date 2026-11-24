from sqlalchemy import String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from database import Base
from datetime import datetime, timezone

class User(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String(255))
    email:Mapped[str] = mapped_column(String(255), unique=True)
    hashed_password:Mapped[str] = mapped_column(String(255))
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

class Transaction(Base):
    __tablename__ = "transactions"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    Userid:Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    amount:Mapped[int] = mapped_column(Integer)
    type:Mapped[str] = mapped_column(String(200))
    category:Mapped[str] = mapped_column(String(200))
    description:Mapped[str] = mapped_column(String(255))
    created_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))
    updated_at:Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
