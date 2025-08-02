-- Create Database
CREATE DATABASE IF NOT EXISTS disaster;

-- Use the database
USE disaster;


DROP TABLE IF EXISTS users;

-- Create users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);


-- Drop table if it already exists
DROP TABLE IF EXISTS disasters;

-- Create Disasters Table
CREATE TABLE disasters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    disaster_name VARCHAR(255),
    disaster_type VARCHAR(100),
    location VARCHAR(255),
    country VARCHAR(100),
    region VARCHAR(100),
    start_date DATE,
    end_date DATE,
    population_affected INT,
    economic_loss DECIMAL(15,2),
    relief_measures_taken TEXT,
    severity_level VARCHAR(50),
    deaths INT
);