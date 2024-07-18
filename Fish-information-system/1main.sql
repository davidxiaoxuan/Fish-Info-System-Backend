drop database if exists fish_db;
create database if not exists fish_db;
use fish_db;
CREATE table if not exists fishes_table(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255),
  age INT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  is_active BOOLEAN
);