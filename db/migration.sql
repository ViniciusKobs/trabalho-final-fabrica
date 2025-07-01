DROP DATABASE IF EXISTS market;
CREATE DATABASE market;
USE market;

CREATE TABLE users (
    id       CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email    VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id          INT PRIMARY KEY AUTO INCREMENT,
    name        VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    category    VARCHAR(255) NOT NULL,
    weight      FLOAT NOT NULL
)

CREATE TABLE markets (
    id      INT PRIMARY KEY AUTO INCREMENT,
    name    VARCHAR(255) NOT NULL UNIQUE,
)

CREATE TABLE pricing (
    product_id INT,
    market_id INT,
    price FLOAT
)