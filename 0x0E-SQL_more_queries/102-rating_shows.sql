-- script that lists all shows from 'hbtn_0d_tvshows_rate' by their rating

-- each record should display: tv_shows.title, rating sum
-- sort the result in descending order by the rating
SELECT tv_show.title,
	SUM(show_rating.rate) AS rating
	FROM tv_shows AS tv_show
		JOIN tv_show_ratings AS show_rating
		ON tv_show.id = show_rating.show_id
	GROUP BY tv_show.title
	ORDER BY rating DESC;
