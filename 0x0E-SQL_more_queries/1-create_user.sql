-- This script creates the MySQL server user user_0d_1 with all privileges on the server.
-- The user_0d_1 password is set to user_0d_1_pwd.
-- If the user user_0d_1 already exists, the script will not fail.

-- Create the user user_0d_1 with password user_0d_1_pwd if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes
FLUSH PRIVILEGES;
