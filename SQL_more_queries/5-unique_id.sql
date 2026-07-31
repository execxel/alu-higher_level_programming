-- 5. Unique ID
-- Create the table unique_id with a unique id and default value 1.
CREATE TABLE IF NOT EXISTS unique_id (
  id INT NOT NULL UNIQUE DEFAULT 1,
  name VARCHAR(256)
);
