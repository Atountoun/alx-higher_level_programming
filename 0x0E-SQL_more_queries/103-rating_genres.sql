-- script that lists all genres in the db 'hbtn_0d_tvshows_rate' by their rating

-- each record should display: tv_genres.name, rating sum
-- sort the result in descending order by their rating
SELECT tv_genre.name,
	SUM(show_rating.rate) AS rating
	FROM tv_genres AS tv_genre
		JOIN tv_show_genres AS tv_show_genre
		ON tv_show_genre.genre_id = tv_genre.id

		JOIN tv_shows AS tv_show
		ON tv_show_genre.show_id = tv_show.id

		JOIN tv_show_ratings AS show_rating
		ON show_rating.show_id = tv_show.id
	GROUP BY tv_genre.name
	ORDER BY rating DESC;
