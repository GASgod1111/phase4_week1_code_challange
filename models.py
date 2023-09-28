from flask_sqlalchemy import SQLAlchemy
from app import db


class Restaurant(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False, unique=True)
  address = db.Column(db.String(200))
  type = db.Column(db.String(200))

  def serialize(self):
      return {
          'id': self.id,
          'name': self.name,
          'address': self.address,
          'type': self.type
      }

class Pizza(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  ingredients = db.Column(db.String(200))

  def serialize(self):
      return {
          'id': self.id,
          'name': self.name,
          'ingredients': self.ingredients
      }

class RestaurantPizza(db.Model):   
  id = db.Column(db.Integer, primary_key=True)
  price = db.Column(db.Integer, nullable=False)
  pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
  restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)