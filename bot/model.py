from sqlalchemy import BigInteger, ForeignKey, Integer, UniqueConstraint, Text
from bot.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
    
class User(Base):
    __tablename__ = "users"
    
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str | None] = mapped_column(Text)
    first_name: Mapped[str | None] = mapped_column(Text)
    last_name: Mapped[str | None] = mapped_column(Text)
    points: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    
    # Relationships
    # humming_samples = relationship("HummingSample", back_populates="user")
    # game_sessions = relationship("GameSession", back_populates="user")
    # guesses = relationship("Guess", back_populates="user")
    
    def __repr__(self):
        return f"<User(telegram_id={self.telegram_id}, username={self.username})>"
