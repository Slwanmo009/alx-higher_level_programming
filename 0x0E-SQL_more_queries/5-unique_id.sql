-- This script creates the table unique_id on the MySQL server.
-- The table has columns:
--   - id: INT with the default value 1 and must be unique
--   - name: VARCHAR(256)
-- The database name will be passed as an argument of the mysql command.
-- If the table unique_id already exists, the script will not fail.

USE <database_name>;

-- Create the table unique_id if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
