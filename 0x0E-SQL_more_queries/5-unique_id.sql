-- script that creates the table unique_id on my sql server
-- if the table exists, script should not fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
