DROP TABLE IF EXISTS departments;
CREATE TABLE departments (
   id SERIAL PRIMARY KEY,
   name VARCHAR(100) UNIQUE NOT NULL,
   description TEXT 
);
DROP TABLE IF EXISTS admins;
CREATE TABLE admins(
   id SERIAL PRIMARY KEY,
   username  VARCHAR(50) UNIQUE NOT NULL,
   password_hash  VARCHAR(255)
);
DROP TABLE IF EXISTS announcements;
CREATE TABLE announcements(
   id SERIAL PRIMARY KEY,
   title VARCHAR(200) NOT NULL,
   the_content TEXT NOT NULL,
   publication_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);