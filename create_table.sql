CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER
    );

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT
    );

CREATE TABLE reviews (
    review_id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    customer_id INTEGER,
    star_rating INTEGER,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    );

