-- SELECT release_year, count(*) AS num_movies
-- FROM movies
-- GROUP BY release_year
-- HAVING num_movies > 2 -- Unlike Where, Column used in Having has to be present in select clause
-- ORDER BY num_movies DESC; -- Returns the years in which more than 2 movies were released

-- Order of Execution
-- FROM --> WHERE --> GROUP BY --> HAVING --> ORDER BY

-- SELECT *, YEAR(CURDATE()) - birth_year as age  -- Returns the current year
-- FROM actors; -- Returns the age of all actors

-- SELECT *, revenue - budget AS profit
-- FROM financials; -- Returns the profit each movie made

-- SELECT *,
-- IF (currency = "USD", revenue * 77, revenue) AS revenue_INR
-- FROM financials; -- Returns the revenue of each movie in Indian ruppees

-- IF (condition, true, false)

-- SELECT *, 
-- IF( unit = "Billions", revenue * 1000, 
-- IF (unit = "Thousands", revenue / 1000, revenue)) AS revenue_millions
-- FROM financials;

SELECT *,
CASE
	WHEN unit = "Billions" THEN revenue * 1000
	WHEN unit = "Thousands" THEN revenue / 1000
    ELSE revenue
END AS revenue_millions
FROM financials; -- Returns the revenue of each movie in millions.