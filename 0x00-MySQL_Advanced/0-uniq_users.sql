-- A script that creates table users with attribute id, email, name

CREATE TABLE IF NOT EXIST user(
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
