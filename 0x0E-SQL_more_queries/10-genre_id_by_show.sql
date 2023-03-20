-- script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked

-- display for each record: tv_shows.title, tv_shows_genres.genre_id
-- sort result in ascending order by tv_shows.title and tv_shows_genres.genre_id
SELECT tv_show.title, show_genre.genre_id
	FROM tv_shows AS tv_show
		JOIN tv_show_genres AS show_genre
		ON tv_show.id = show_genre.show_id
	ORDER BY tv_show.title, show_genre.genre_id ASC;
