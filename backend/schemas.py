from typing import List, Union

from pydantic import BaseModel


class ScoreBase(BaseModel):
    score: int
    time: int


class ScoreCreate(ScoreBase):
    pass


class Score(ScoreBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    scores: List[Score] = []

    class Config:
        orm_mode = True
