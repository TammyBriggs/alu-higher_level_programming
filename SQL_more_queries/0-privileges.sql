-- Script that lists all privileges of the MySQL users

-- Query to list all privileges (GRANT) of the MySQL users
SELECT * 
FROM information_schema.user_privileges
WHERE grantee IN ('user_0d_1@localhost', 'user_0d_2@localhost');

