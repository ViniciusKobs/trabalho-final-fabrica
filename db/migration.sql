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

CREATE TABLE brands (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    image       TEXT
);

CREATE TABLE products (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    brand_id    INT,
    name        VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    image       TEXT,
    weight      INT,
    volume      INT,
    units       INT,
    length      INT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE products_categories (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    product_id  INT,
    category_id INT
);

CREATE TABLE brands_categories (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    brand_id    INT,
    category_id INT
);

CREATE TABLE categories (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    name        VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE markets (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    name       VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE pricing (
    id         INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    market_id  INT,
    price      FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);