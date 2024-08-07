-- This script creates the table id_not_null on the MySQL server.
-- The table has columns:
--   - id: INT with the default value 1
--   - name: VARCHAR(256)
-- The database name will be passed as an argument of the mysql command.
-- If the table id_not_null already exists, the script will not fail.

USE <database_name>;

-- Create the table id_not_null if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
