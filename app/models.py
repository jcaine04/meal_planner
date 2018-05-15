
from sqlalchemy import Column, Integer, String, Boolean

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(25))
    prep_time_minutes = db.Column(db.Integer)
    cook_time_minutes = db.Column(db.Integer)
    recipe_source = db.Column(db.String())
    vegetable_required = db.Column(db.Boolean)
    starch_required = db.Column(db.Boolean)

class Ingredient(db.Model):
    __tablename__: 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    quantity = db.Column(db.Float)
    size = db.Column(db.Float)
    unit = db.Column(db.String(25))
    style = db.Column(db.String(25))
