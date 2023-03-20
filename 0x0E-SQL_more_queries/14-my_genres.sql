-- script that uses 'hbtn_0d_tvshows' db to list all genres of the show 'Dexter'
-- the tv_shows table contains only one record where title = 'Dexter'

-- each record should display 'tv_genres.name'
-- sort result in ascending order by the genre name
SELECT tv_genre.name
	FROM tv_genres AS tv_genre
		JOIN tv_show_genres AS tv_show_genre
		ON tv_genre.id = tv_show_genre.genre_id

		JOIN tv_shows AS tv_show
		ON tv_show_genre.show_id = tv_show.id
		WHERE tv_show.title = 'Dexter'
	ORDER BY tv_genre.name ASC;	
