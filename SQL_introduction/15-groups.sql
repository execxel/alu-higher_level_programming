-- 15. Number by score
-- List number of records with the same score in second_table.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
