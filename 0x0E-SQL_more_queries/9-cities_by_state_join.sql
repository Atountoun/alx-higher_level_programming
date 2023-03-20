-- script that lists all cities contained in db 'hbtn_0d_usa'

-- display 'cities.id', 'cities.name', 'states.name'
SELECT c.id, c.name, s.name
	FROM cities AS c
		LEFT JOIN states AS s
		ON c.state_id = s.id
	ORDER BY c.id ASC;
