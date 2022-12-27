from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
import passlib.hash as _hash

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(40), unique=True, index=True)
    hashed_password = Column(String)
    scores = relationship("Score", back_populates="owner")

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)


class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer, index=True)
    time = Column(Integer, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="scores")
