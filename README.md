# mysql-selfmanaged

Assignment 5 HHA 504

# GCP Set-Up

1 Connect to VM using terminal 

2 Update VM $ sudo apt-get update

3 Install mysql-server & mysql client using $ sudo apt install mysql-client mysql-server

4 $ sudo mysql 

5 Show databases mysql> show databases; 

6 Create user mysql> create user 'xxx'@'%' identified by 'pwd'

7 Confirm user mysql> select 'user' from mysql.user

# Allowing mysql connections 

$ sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

change bind address from 127.0.0.1 to 0.0.0.0

save change of bind address: control o, exit: control x

restart to apply bind address change $ sudo /etc/init.d/mysql restart

add port 3306 on VM
