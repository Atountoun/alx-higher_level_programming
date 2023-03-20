-- script that list all genres from 'hbtn_0d_tvshows'
-- and displays the number of shows linked to each

-- each record should display: 'TV Show genre', 'Number of shows linked to this genre'
-- first column must be called 'genre'
-- second column must be called 'number_of_shows'
-- only display genre that have a show linked
-- sort in descending order by the number of shows linked
SELECT tv_genre.name AS genre,
	COUNT(show_genre.show_id) AS number_of_shows
	FROM tv_genres AS tv_genre
		JOIN tv_show_genres AS show_genre
		ON tv_genre.id = show_genre.genre_id
	GROUP BY tv_genre.name
	ORDER BY number_of_shows DESC;
