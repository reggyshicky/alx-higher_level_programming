-- lists the number of records with the sam score in the table
SELECT score, count(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC
