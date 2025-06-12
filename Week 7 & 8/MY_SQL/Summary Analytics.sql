-- SELECT MAX(imdb_rating)
-- FROM movies
-- WHERE industry = "Bollywood"; -- Returns the highest imdb_rating in all Bollywood movies.

-- SELECT MIN(imdb_rating)
-- FROM movies
-- WHERE industry = "Bollywood"; -- Returns the lowest imdb_rating in all Bollywood movies.

-- SELECT ROUND(AVG(imdb_rating), 2) AS avg_rating
-- FROM movies
-- WHERE studio = "Marvel Studios"; -- Returns the average rating of all movies produced by Marvel to 2 d.p

-- SELECT industry, COUNT(*)
-- FROM movies
-- GROUP BY industry; -- Returns count of movies produced by each industry

-- SELECT studio, COUNT(*) as num_movies
-- FROM movies 
-- GROUP BY studio
-- ORDER BY num_movies ASC; -- Returns count of movies produced by each studio in ascending order of count.

SELECT industry, COUNT(*) as num_movies,
	   ROUND(AVG(imdb_rating), 2) as avg_rating
FROM movies
GROUP BY industry; -- Returns count and average rating of movies produced by each industry.