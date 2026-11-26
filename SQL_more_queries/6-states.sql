-- Creates the database hbtn_0d_usa if it does not already exist.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Selects the database hbtn_0d_usa.
USE `hbtn_0d_usa`;
-- Creates the table states with an auto-incrementing primary key.
CREATE TABLE IF NOT EXISTS `states` (
    `id` INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    `name` VARCHAR(256) NOT NULL
);
