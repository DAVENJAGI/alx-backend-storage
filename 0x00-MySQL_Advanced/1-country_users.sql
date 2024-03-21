-- Script that creates Table that users with below requirement
CREATE TABLE IF NOT EXIST users (
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY
	email VARCHAR(255) NOT NULL UNIQUE
	name VARCHAR(255)
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
