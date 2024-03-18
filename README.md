## Phase 3 Code Challenge: Restaurants


For this assignment, we'll be working with a restaurant review domain. We have three models: `Restaurant`, `Review`, and `Customer`.



For our purposes, a `Restaurant` has many `Review`s, a `Customer` has many `Review`s, and a `Review` belongs to a `Restaurant` and to a `Customer`.`Restaurant` - `Customer` is a many-to-many relationship.