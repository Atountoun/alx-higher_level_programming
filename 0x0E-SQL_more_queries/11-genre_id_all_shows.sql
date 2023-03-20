-- script that lists all shows contained in the database 'hbtn_0d_tvshows'

-- each record should display: tv_shows.title, tv_show_genre.genre_id
-- sort result in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_show.title, show_genre.genre_id
	FROM tv_shows AS tv_show
		LEFT JOIN tv_show_genres AS show_genre
		ON tv_show.id = show_genre.show_id
	ORDER BY tv_show.title, show_genre.genre_id ASC;
