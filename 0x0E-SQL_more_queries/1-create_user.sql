-- create user 'user_0d_1' with password 'user_0d_1_pwd'
-- grant all privileges to the user

-- create user_0d_1 with password usre_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- reload privilege table and apply the change
FLUSH PRIVILEGES;
