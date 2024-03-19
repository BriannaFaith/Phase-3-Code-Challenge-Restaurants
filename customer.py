from __init__ import CURSOR, CONN
from restaurant import Restaurant

class Customer:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self._id = None
        self._reviews = []

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def reviews(self):
        if not self._reviews:
            self._reviews = self.get_reviews()
        return self._reviews


    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO customers(first_name, last_name, email)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name, self.email))
        CONN.commit()

    def get_reviews(self):
        sql = """
            SELECT * FROM reviews
            WHERE customer_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        return [row for row in CURSOR.fetchall()]

    def restaurants(self):
        sql = """
            SELECT restaurant_id FROM reviews
            WHERE customer_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        restaurant_ids= [row[0] for row in CURSOR.fetchall()]
        return restaurant_ids

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        if not self.reviews:
            return None
        favorite_review = max(self.reviews, key=lambda review: review.star_rating)
        return favorite_review.restaurant

    def add_review(self, restaurant, rating):
        from review import Review
        new_review = Review(self, restaurant, rating)
        self.reviews.append(new_review)
        restaurant_obj = Restaurant.find_by_id(restaurant.id)
        if restaurant_obj:
            restaurant.id = restaurant_obj.id
            new_review.restaurant = restaurant_obj
            new_review.save()  
        else:
            print(f"Restaurant with ID {restaurant.id} not found.")

    def delete_reviews(self, restaurant):
        sql = """
            DELETE FROM reviews

            WHERE customer_id = ? AND restaurant_id = ?
        """
        for review in self.reviews:
            if review.restaurant == restaurant:
                CURSOR.execute(sql, (self.id, restaurant.id))
                CONN.commit()
                self.reviews.remove(review)

    @classmethod
    def find_by_id(cls, customer_id):
        sql = "SELECT * FROM customers WHERE id = ?"
        CURSOR.execute(sql, (customer_id,))
        row = CURSOR.fetchone()
        if row:
            customer = cls(row[1], row[2],row[3])
            customer.id = row[0]
            return customer
        else:
            return None
