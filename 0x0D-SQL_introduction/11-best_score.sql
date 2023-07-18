-- lists all records with a score >= 10 in the second_table of the db
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
