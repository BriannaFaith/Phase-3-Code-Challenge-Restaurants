from __init__ import CURSOR, CONN
from restaurant import Restaurant
from customer import Customer
from review import Review

# Create tables if they don't exist
Restaurant.create_table()
Customer.create_table()
Review.create_table()

# Insert test data
# Insert restaurants
CURSOR.execute("INSERT INTO restaurants (name, price) VALUES ('Restaurant A', 1000)")
CURSOR.execute("INSERT INTO restaurants (name, price) VALUES ('Restaurant B', 2000)")

# Insert customers
CURSOR.execute("INSERT INTO customers (first_name, last_name, email) VALUES ('John', 'Doe', 'john.doe@example.com')")
CURSOR.execute("INSERT INTO customers (first_name, last_name, email) VALUES ('Jane', 'Smith', 'jane.smith@example.com')")

# Insert reviews
CURSOR.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (1, 1, 5)")
CURSOR.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (2, 2, 4)")

CONN.commit()

# Check Object Relationship Methods
# Review customer() and restaurant() methods
review = Review.instance_from_db(CURSOR.execute("SELECT * FROM reviews WHERE review_id = 1").fetchone())
print(review.customer())
print(review.restaurant())

# Restaurant reviews() and customers() methods
restaurant = Restaurant("Restaurant A", 1000)
reviews = restaurant.restaurant_reviews()
print(reviews)
print(restaurant.customers())

# Customer reviews() and restaurants() methods
customer = Customer("John", "Doe", "john.doe@example.com")
print(customer.reviews)
print(customer.restaurants())

# Check Aggregate and Relationship Methods
# Customer full_name() method
print(customer.full_name())

# Customer favorite_restaurant() method
print(customer.favorite_restaurant())

# Customer add_review() method
customer.add_review(restaurant, 4)

# Customer delete_reviews() method
customer.delete_reviews(restaurant)

# Review full_review() method
print(review.full_review)

# Restaurant fanciest()
fanciest_restaurant = Restaurant.fanciest()
print(fanciest_restaurant)


