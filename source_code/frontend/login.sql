CREATE DATABASE login;
USE login;

CREATE TABLE login_info (
	id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);


INSERT INTO login_info
(name, username, password)
VALUES
('Emma', 'en.moseley@gmail.com', 'Maple'),
('Dan', 'lala@gmail.com', 'Green'),
('Beth', 'sunday@gmail.com', 'Blue');


SELECT * FROM login_info;
