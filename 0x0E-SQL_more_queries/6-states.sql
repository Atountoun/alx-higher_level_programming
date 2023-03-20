-- script that create the db 'hbtn_0d_usa' and table 'states' in that db

-- create db 'hbtn_0d_usa'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- select that database
USE hbtn_0d_usa;
-- create table 'states'
CREATE TABLE IF NOT EXISTS states (
	PRIMARY KEY (id),
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	name VARCHAR(256) NOT NULL
	);
