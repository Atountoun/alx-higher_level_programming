-- script that creates the table 'id_not_null', dbname passed as argument

-- create table 'id_not_null' with id, name
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
	);
