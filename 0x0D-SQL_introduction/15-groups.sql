-- script that lists the number of records with the same score
-- in the table 'second_table'

-- the result should display the score
-- and the number of records for this score with the label number
-- sort the list by the number of records (descending)
SELECT score,
	COUNT(score) AS number
	FROM second_table
	GROUP BY score
	ORDER BY number DESC;
