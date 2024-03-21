-- A script that creates table users with attribute id, email, name
-- With attributes ID, integer, never null, auto increment
-- email, varchar, never null, and unique
-- script to execute if table exists
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
