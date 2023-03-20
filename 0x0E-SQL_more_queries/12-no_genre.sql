-- script that lists all shows contained in 'hbtn_0d_tvshows'
-- only shows that do not have a genre linked

-- each record should display: tv_shows.title, tv_show_genres.genre_id
-- sort result in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_show.title, show_genre.genre_id
	FROM tv_shows AS tv_show
		LEFT JOIN tv_show_genres AS show_genre
		ON tv_show.id = show_genre.show_id
		WHERE show_genre.show_id IS NULL
	ORDER BY tv_show.title, show_genre.genre_id ASC;
