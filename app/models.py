from app import db

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    prep_time_minutes = db.Column(db.Integer)
    cook_time_minutes = db.Column(db.Integer)

class Ingredient(db.Model):
    __tablename__: 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    quantity = db.Column(db.Float)
    size = db.Column(db.Float)
    unit = db.Column(db.String(25))
    style = db.Column(db.String(25))
