from faker import Faker
from app import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

def generate_custom_pizza():
    return {
        'name': fake.word(),
        'ingredients': ', '.join(fake.words(nb=5)),
    }

def generate_custom_restaurant():
    return {
        'name': fake.company(),
        'address': fake.address(),
    }

def seed_custom_database():
    custom_pizzas = []
    custom_restaurants = []

    for _ in range(50): 
        pizza_data = generate_custom_pizza()
        custom_pizza = Pizza(**pizza_data)
        custom_pizzas.append(custom_pizza)
        db.session.add(custom_pizza)

    for _ in range(20): 
        restaurant_data = generate_custom_restaurant()
        custom_restaurant = Restaurant(**restaurant_data)
        custom_restaurants.append(custom_restaurant)
        db.session.add(custom_restaurant)

    for custom_pizza in custom_pizzas:
        for custom_restaurant in custom_restaurants:
            price = fake.random_int(min=1, max=30)
            custom_restaurant_pizza = RestaurantPizza(restaurant=custom_restaurant, pizza=custom_pizza, price=price)
            db.session.add(custom_restaurant_pizza)

    db.session.commit()

if __name__ == '__main__':
    seed_custom_database()
