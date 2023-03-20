-- script that creates the database 'hbtn_0d_2' and the user 'user_0d_2'

-- create user 'user_0d_2' with password 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- create database 'hbtn_0d_2'
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- grant select access to user 'user_0d_2' on database 'hbtn_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
