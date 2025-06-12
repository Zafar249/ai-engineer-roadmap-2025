-- USE moviesdb;

-- SELECT *
-- FROM movies;

-- SELECT COUNT(*)
-- FROM movies
-- WHERE industry = "Bollywood"; -- Returns number of bollywood movies

-- SELECT *
-- FROM movies
-- WHERE industry = "hollywood"; -- Case insensitive

-- SELECT DISTINCT Industry
-- FROM movies; --  Returns Unique Industries

-- SELECT *
-- FROM movies
-- WHERE title LIKE "%THOR%"; -- Wild Card Search, returns movies with thor in the title

-- SELECT *
-- FROM movies
-- WHERE studio = ""; -- Returns all movies with no(NULL) studios

-- SELECT *
-- FROM movies
-- WHERE imdb_rating >= 9.0; -- Returns all movies with a rating greater than  or equal to 9

-- SELECT *
-- FROM movies
-- WHERE imdb_rating BETWEEN 6 AND 8; -- Returns all movies with a rating between 6 and 8

-- SELECT *
-- FROM movies
-- WHERE release_year = 2019 
-- OR release_year = 2022; -- Returns all movies that were released in 2019 or 2022

-- SELECT *
-- FROM movies
-- WHERE release_year IN (2018, 2019, 2022); -- Returns all movies that were released in 2018,2019 and 2022.

-- SELECT *
-- FROM movies
-- WHERE studio IN ("Marvel Studios", "Zee Studios"); -- Returns all movies made by the following studios

-- SELECT *
-- FROM movies
-- WHERE imdb_rating IS NULL; -- Returns all movies with NULL ratings

-- SELECT *
-- FROM movies
-- WHERE imdb_rating IS NULL; -- Returns all movies with No NULL ratings

-- SELECT *
-- FROM movies
-- WHERE industry =  "Bollywood"
-- ORDER BY imdb_rating DESC; -- Returns all bollywood movies ordered by descending imdb_rating

-- SELECT *
-- FROM movies
-- WHERE industry =  "Bollywood"
-- ORDER BY imdb_rating DESC
-- LIMIT 5; -- Returns 5 bollywood movies with the highest imdb_rating in descending order

SELECT *
FROM movies
WHERE industry =  "Hollywood"
ORDER BY imdb_rating DESC
LIMIT 5 OFFSET 1; 
-- Returns 5 hollywood movies with the highest imdb_rating in descending order starting from the 2nd movie