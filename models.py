
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    type = Column(String(25))
    prep_time_minutes = Column(Integer)
    cook_time_minutes = Column(Integer)
    recipe_source = Column(String())
    vegetable_required = Column(Boolean)
    starch_required = Column(Boolean)


class Ingredient(Base):
    __tablename = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    quantity = Column(Float)
    size = Column(Float)
    unit = Column(String(25))
    style = Column(String(25))
