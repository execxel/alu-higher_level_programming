-- 16. Say my name
-- List records in second_table with a non-empty name ordered by score descending.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
