from flask import Flask, request, jsonify
from models import *
from app import app

@app.route('/')
def home():
   print("Home route is being executed.")
   return '<h1>Welcome, We\'re glad you\'re here</h1>'

@app.route('/restaurants')
def get_restaurants():
  restaurants = Restaurant.query.all()
  
  serialized_restaurants = [restaurant.serialize() for restaurant in restaurants]
  return jsonify(serialized_restaurants)

@app.route('/restaurants/<int:id>') 
def get_restaurant(id):
  restaurant = Restaurant.query.get(id)

  if not restaurant:
    return jsonify({'error': 'Restaurant not found'}), 404

  return jsonify(restaurant.serialize()) 

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
  restaurant = Restaurant.query.get(id)

  if not restaurant:
    return jsonify({'error': 'Restaurant not found'}), 404

  db.session.delete(restaurant)
  db.session.commit()

  return '', 204

################################################################

@app.route('/pizzas')
def get_pizzas():
  pizzas = Pizza.query.all()
  serialized_pizzas = [pizza.serialize() for pizza in pizzas]
  return jsonify(serialized_pizzas)

@app.route('/restaurant_pizzas', methods=['POST']) 
def create_restaurant_pizza():

  data = request.get_json()  
  pizza = Pizza.query.get(data['pizza_id'])
  restaurant = Restaurant.query.get(data['restaurant_id'])

  if not pizza or not restaurant:  
    return jsonify({'errors': ['Pizza or restaurant not found']}), 400

  rp = RestaurantPizza(price=data['price'], pizza=pizza, restaurant=restaurant)

  db.session.add(rp)
  db.session.commit()

  return jsonify(pizza.serialize())