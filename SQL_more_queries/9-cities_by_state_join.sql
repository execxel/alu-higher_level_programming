-- 9. Cities by States
-- List all cities with their state names ordered by city id.
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
