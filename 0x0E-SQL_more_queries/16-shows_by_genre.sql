-- script that lists all shows, and all genres linked to that show from bd 'hbtn_0d_tvshows'

-- if a show doesn't have a genre, display NULL in the genre column
-- each record should display: tv_shows.title, tv_genres.name
-- sort result in ascending order by show title and genre name
SELECT tv_show.title, tv_genre.name
	FROM tv_shows AS tv_show
		LEFT JOIN tv_show_genres AS tv_show_genre
		ON tv_show.id = tv_show_genre.show_id

		LEFT JOIN tv_genres AS tv_genre
		ON tv_show_genre.genre_id = tv_genre.id
	ORDER BY tv_show.title, tv_genre.name ASC;
