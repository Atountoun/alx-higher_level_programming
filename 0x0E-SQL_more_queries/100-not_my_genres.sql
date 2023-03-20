-- script that uses the 'hbtn_0d_tvshows' db to list all genres not linked to the show 'Dexter'

-- tv_shows table contains only one record where title = 'Dexter'
-- each record should display: tv_genres.name
-- sort result in ascending order by the genre name
SELECT tv_genre.name
	FROM tv_genres AS tv_genre
	WHERE tv_genre.id NOT IN (
		SELECT tv_show_genre.genre_id
			FROM tv_show_genres AS tv_show_genre
				JOIN tv_shows AS tv_show
				ON tv_show_genre.show_id = tv_show.id
				WHERE tv_show.title = "Dexter"
			)
	ORDER BY tv_genre.name ASC;
