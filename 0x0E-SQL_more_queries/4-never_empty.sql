-- script that creates the table on MYSQL server
-- if the table already exists, script should not fail

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)NOT NULL);
