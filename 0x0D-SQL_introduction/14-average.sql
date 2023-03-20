-- script that computes the score average of all records in the table 'second_table'

-- the result column should be average
-- the db name will be passed as an argument of the mysql command
SELECT
	AVG(score) AS average
	FROM second_table;
