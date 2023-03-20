-- script that lists all records of the table 'second_table'

-- don't list rows without a 'name' value
-- display the score and the name
-- list records by descending score
SELECT score, name
	FROM second_table
	WHERE name IS NOT NULL;
