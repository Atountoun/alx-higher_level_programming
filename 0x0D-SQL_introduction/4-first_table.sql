-- script that creates a table called 'first_table' in the current db

-- db name will be passed as argument of the mysql command
-- the script should not fail if the table already exists
CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256)
	);
