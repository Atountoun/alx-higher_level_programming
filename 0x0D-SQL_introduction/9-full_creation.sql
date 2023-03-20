-- script that creates a table 'second_table' in the db 'hbtn_0c_0'
-- add multiples rows

-- cols name: id, name, score
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
	);

-- insert multiples rows in the table
INSERT INTO second_table
VALUES (1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
