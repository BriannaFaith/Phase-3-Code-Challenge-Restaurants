from __init__ import CURSOR, CONN
from restaurant import Restaurant
from customer import Customer


class Review:
    all_reviews = {}

    def __init__(self,restaurant_id, customer_id, star_rating):
        self.id = None
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.star_rating= star_rating  # Renamed to avoid conflict with method name
        Review.all_reviews[self.id] = self

    def __str__(self):
        customer = Customer.find_by_id(self.customer_id)
        return f"Review: {self.customer.full_name()} rated {self.star_rating} stars"

    def customer(self):
        return Customer.find_by_id(self.customer_id)

    def restaurant(self):
        return Restaurant.find_by_id(self.restaurant_id)

    @classmethod
    def all(cls):
        return cls.all_reviews.values()

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            review_id INTEGER PRIMARY KEY,
            restaurant_id INTEGER,
            customer_id INTEGER,
            star_rating INTEGER,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO reviews (review_id, restaurant_id, customer_id, star_rating)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.id, self.restaurant.id, self.customer.id, self.star_rating))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def instance_from_db(cls, row):
        review_id = row[0]
        restaurant_id = row[1]
        customer_id = row[2]
        star_rating = row[3]

        restaurant = Restaurant.find_by_id(restaurant_id)
        customer = Customer.find_by_id(customer_id)

        if review_id in cls.all_reviews:
            review = cls.all_reviews[review_id]
            review.star_rating = star_rating
        else:
            review = cls(restaurant_id, customer_id, star_rating)
            review.id = review_id
            Review.all_reviews[review_id] = review

        return review

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."