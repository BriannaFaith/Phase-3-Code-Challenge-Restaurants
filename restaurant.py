from __init__ import CURSOR, CONN

class Restaurant:
    all_restaurants = []

    def __init__(self,name,price):
        self.name = name
        self.price = price
        self._id = None
        self._reviews = []
        Restaurant.all_restaurants.append(self)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def __repr__(self):
        return f"<Restaurant {self.id}: {self.name}, {self.price}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql= """
            INSERT INTO restaurants(name,price)
            VALUES(?,?)
        """
        CURSOR.execute(sql,(self.name, self.price))
        CONN.commit()

    def restaurant_reviews(self):
        sql = """
            SELECT * FROM reviews
            WHERE restaurant_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        return [row for row in CURSOR.fetchall()]

    def customers(self):
        from customer import Customer
        sql = """
            SELECT customer_id FROM reviews
            WHERE restaurant_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        return [row[0] for row in CURSOR.fetchall()]
    @classmethod
    def fanciest(cls):
        sql = """
            SELECT * FROM restaurants
            WHERE id = (
            SELECT restaurant_id FROM reviews
            JOIN customers ON reviews.customer_id = customers.id
            GROUP BY restaurant_id
            ORDER BY AVG(star_rating) DESC
            LIMIT 1
        )
    """
        row = CURSOR.execute(sql).fetchone()
        if row and len(row) >= 4:
            return cls(*row[1:])
        return None

    @classmethod
    def find_by_id(cls, restaurant_id):
        sql = "SELECT * FROM restaurants WHERE id = ?"
        CURSOR.execute(sql, (restaurant_id,))
        row = CURSOR.fetchone()
        if row:
            restaurant = cls(row[1],row[2])
            restaurant.id = row[0]
            return restaurant
        else:
            return None
        