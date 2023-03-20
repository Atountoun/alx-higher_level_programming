-- script that lists all the cities of California in db 'hbtn_0d_usa'

-- select id of record of states where name is California
-- select id and name of cities where state_id match with the one from states
-- state table contains only record where name is California
SELECT c.id, c.name
	FROM cities AS c
	WHERE c.state_id =
		(SELECT s.id
			FROM states AS s
			WHERE s.name = 'California')
	ORDER BY c.id ASC;
