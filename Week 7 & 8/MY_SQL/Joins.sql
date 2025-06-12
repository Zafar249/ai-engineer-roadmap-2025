-- SELECT m.movie_id, title, budget, revenue
-- FROM movies m
-- INNER JOIN financials f
-- ON m.movie_id = f.movie_id;
-- Joins movies table to financials table and returns information about each movie

-- When joining two tables together, the from table is the left table 
-- and the table you join is the right table.

-- SELECT m.movie_id, title, budget, revenue
-- FROM movies m
-- LEFT JOIN financials f
-- ON m.movie_id = f.movie_id; -- Returns all movies even if they have no budget or revenue

-- SELECT movie_id, title, budget, revenue
-- FROM movies m
-- RIGHT OUTER JOIN financials f
-- USING (movie_ID); -- Returns all financials even if they have no movie title

-- USING can also join two tables using two columns

SELECT m.movie_id, title, budget, revenue
FROM movies m
LEFT JOIN financials f
ON m.movie_id = f.movie_id
UNION
SELECT f.movie_id, title, budget, revenue
FROM movies m
RIGHT JOIN financials f
ON m.movie_id = f.movie_id; -- Returns all the information in the selected columns from both tables.