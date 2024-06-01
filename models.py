from sqlalchemy import Column, Integer, String
from database import Base


class Scores(Base):
    __tablename__ = "Scores"

    id = Column(Integer, primary_key=True, identity=True)
    name = Column(String)
    score = Column(Integer)
