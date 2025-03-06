from sqlalchemy import BigInteger, ForeignKey, Integer, String, UniqueConstraint
from bot.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
    
class User(Base):
    __tablename__ = "users"
    
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username = Mapped[str | None]
    first_name = Mapped[str | None]
    last_name = Mapped[str | None]
    points = Mapped[int]
    
    # Relationships
    # humming_samples = relationship("HummingSample", back_populates="user")
    # game_sessions = relationship("GameSession", back_populates="user")
    # guesses = relationship("Guess", back_populates="user")
    
    def __repr__(self):
        return f"<User(telegram_id={self.telegram_id}, username={self.username})>"
