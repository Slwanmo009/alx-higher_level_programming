-- This script lists all shows without the genre Comedy in the hbtn_0d_tvshows database.
-- Each record displays: tv_shows.title
-- Results are sorted in ascending order by the show title
-- The database name will be passed as an argument of the mysql command.

-- Selects all shows that do not have the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT tv_shows.id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
    JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
