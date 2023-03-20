-- script that creates the table 'force_name'
-- database name will be passed as an argument to the mysql command

-- create table 'force_name'
CREATE TABLE IF NOT EXISTS force_name (
	id INT,
	name VARCHAR(256) NOT NULL
	);
