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
    
    humming_samples = relationship("HummingSample", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(telegram_id={self.telegram_id}, username={self.username})>"

class HummingSample(Base):
    __tablename__ = "humming_samples"

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.telegram_id", ondelete="CASCADE"), nullable=False)
    file_id: Mapped[str] = mapped_column(Text, nullable=False)  
    song_title: Mapped[str] = mapped_column(Text)
    song_artist: Mapped[str] = mapped_column(Text)

    # Связь с User (Обратная связь)
    user = relationship("User", back_populates="humming_samples")

    def __repr__(self):
        return f"<HummingSample(id={self.id}, user_id={self.user_id}, file_id={self.file_id})>"
