from sqlalchemy import BigInteger
from app.database import Base
from sqlalchemy.orm import mapped_column, Mapped

class User(Base):
    __tablename__ = 'users'
    
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str | None]
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]