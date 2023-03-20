-- script that create the db 'hbtn_0d_usa' and table 'cities' in that db

-- create db 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select that db
USE hbtn_0d_usa;
-- create 'cities' table
CREATE TABLE IF NOT EXISTS cities (
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states (id),
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256)
	);
