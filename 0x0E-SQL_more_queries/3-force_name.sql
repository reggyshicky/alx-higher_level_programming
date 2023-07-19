-- script that creates the table force_name on MYSQL server
-- if the table force_name already exists, your script shoud not fail

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL);
