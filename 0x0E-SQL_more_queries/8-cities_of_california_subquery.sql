-- script that lists cities of california that can be found in the db
-- lists all the cities of california state
-- that can be found in the db hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
);
