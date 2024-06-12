CREATE DATABASE liquor_store;
USE liquor_store;

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

GRANT ALL PRIVILEGES ON *.* TO 'samwel'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
