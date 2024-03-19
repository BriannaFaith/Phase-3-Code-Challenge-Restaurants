## Author
Faith Ogendi

## Phase 3 Code Challenge: Restaurants

For this assignment, we'll be working with a restaurant review domain. We have three models: `Restaurant`, `Review`, and `Customer`.



For our purposes, a `Restaurant` has many `Review`s, a `Customer` has many `Review`s, and a `Review` belongs to a `Restaurant` and to a `Customer`.`Restaurant` - `Customer` is a many-to-many relationship.
## Deliverables
Write the following methods in the classes. Feel free to build out any helper methods if needed.

# Database.
Before working on the rest of the deliverables, you will need to create all tables.

- A `Review` belongs to a `Restaurant`, and a `Review` also belongs to a  `Customer`.  In your script, create any columns your `reviews` table will

 need to establish these relationships.

The `reviews` table should also have:  - A `star_rating` column that stores an integer.


After creating the `reviews` table , use the `main.py` file to create instances of all your classes so you can test your code.



**Once you've set up your tables**, work on building out the following deliverables.

# Object Relationship Methods

Review
- `Review customer()`

 - should return the `Customer` instance for this review

- `Review restaurant()`

 - should return the `Restaurant` instance for this review

Restaurant
- `Restaurant reviews()`

 - returns a collection of all the reviews for the `Restaurant`

- `Restaurant customers()`

 - returns a collection of all the customers who reviewed the `Restaurant`

Customer
- `Customer reviews()`

 - should return a collection of all the reviews that the `Customer` has left

- `Customer restaurants()`

 - should return a collection of all the restaurants that the `Customer` has

   reviewed

# Aggregate and Relationship Methods
Customer
- `Customer full_name()`

 - returns the full name of the customer, with the first name and the last name  concatenated, Western style.

- `Customer favorite_restaurant()`

 - returns the restaurant instance that has the highest star rating from this customer

- `Customer add_review(restaurant, rating)`

 - takes a `restaurant` (an instance of the `Restaurant` class) and a rating

 - creates a new review for the restaurant with the given `restaurant_id`

- `Customer delete_reviews(restaurant)`

 - takes a `restaurant` (an instance of the `Restaurant` class) and

 - removes **all** their reviews for this restaurant

 - you will have to delete rows from the `reviews` table to get this to work!
Review
- `Review full_review()`

 - should return a string formatted as follows:
Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

Restaurant
- `Restaurant fanciest(), this method should be a class method`

- returns _one_ restaurant instance for the restaurant that has the highest   price

- `Restaurant all_reviews()`

- should return a list of strings with all the reviews for this restaurant

  formatted as follows:

[

"Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",

"Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",

]

## Set up Instructions
Clone the repo


## Technologies
Python