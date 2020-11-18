-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT DISTINCT tv_shows.title title, tv_genres.name name
FROM tv_show_genres
RIGHT OUTER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
RIGHT OUTER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_genres.name;
