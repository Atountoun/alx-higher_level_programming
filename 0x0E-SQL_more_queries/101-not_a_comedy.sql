-- script that lists all shows without the genre 'Comedy' in the db 'hbtn_0d_tvshows'

-- tv_genres table contains only one record where name = Comedy
-- each record should display: tv_shows.title
-- sort the result in ascending order by the show title
SELECT tv_show.title
	FROM tv_shows AS tv_show
	WHERE tv_show.id NOT IN (
		SELECT tv_show_genre.show_id
			FROM tv_show_genres AS tv_show_genre
				JOIN tv_genres AS tv_genre
				ON tv_show_genre.genre_id = tv_genre.id
				WHERE tv_genre.name = "Comedy"
			)
	ORDER BY tv_show.title ASC;
