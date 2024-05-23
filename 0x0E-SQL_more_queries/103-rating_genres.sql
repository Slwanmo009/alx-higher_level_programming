-- This script lists all genres in the hbtn_0d_tvshows_rate database by their rating.
-- Each record displays: tv_genres.name - rating sum
-- Results are sorted in descending order by their rating
-- The database name will be passed as an argument of the mysql command.

-- Selects all genres by their rating sum and orders them by rating in descending order
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_show_ratings ON tv_show_genres.tv_show_id = tv_show_ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
