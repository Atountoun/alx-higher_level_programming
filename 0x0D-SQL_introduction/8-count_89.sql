-- script that displays the number of records with id = 89
-- first_table is the name of the table to be used

-- the db name will be passed as an argument of the mysql command
SELECT COUNT(*)
	FROM first_table
	WHERE id = 89;
