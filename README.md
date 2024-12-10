# Project

## Docker and Docker Compose

* [Docker CLI](https://docs.docker.com/reference/cli/docker/)
* [Compose file reference](https://docs.docker.com/reference/compose-file/)
* [Sharing local files with containers](https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/)
* [Volumes](https://docs.docker.com/engine/storage/volumes/)

## Valkey

It is a port of 'redis', so 'redis' tutorials should be usable.

* [Redis Tutorial](https://www.tutorialspoint.com/redis/index.htm)

Reference documentation

* [Valkey: official docker containers](https://valkey.io/download/releases/v8-0-0/)
* [Valkey: Tutorial](https://www.percona.com/blog/hello-valkey-lets-get-started/)
* [Documentation: Valkey configuration](https://valkey.io/topics/valkey.conf/)
* [Valkey: Documentation by topic](https://valkey.io/topics/)
* [Valkey: Command Reference](https://valkey.io/commands/)
* [valkey-py - Core Commands](https://valkey-py.readthedocs.io/en/latest/commands.html#core-commands)
* [How to Use the Redis Docker Official Image](https://www.docker.com/blog/how-to-use-the-redis-docker-official-image/)

Use `docker compose` to start, stop the container.

* `valkey` service builds the container, copying a configuration template, into `/usr/local`
* `valkey-vanilla`, which is commented-out, deploys the one from DockerHub, with any configuration

Both mount `valkey\data` so the files are stored locally on Windows

Like the other containers it is configured on `dev_net` to isolate it from any other containers.

```console
# Start the container
PS1> docker compose up -d valkey

# Login to container
PS1> docker exec -it valkey sh         # interactive UNIX Shell

# Start the valkey-cli
PS1> docker exec -it valkey valkey-cli # valkey-cli
127.0.0.1:6379> SET mynumber 42
OK
127.0.0.1:6379> GET mynumber
"42"
127.0.0.1:6379> TYPE mynumber
string
127.0.0.1:6379> OBJECT ENCODING mynumber
"int"
127.0.0.1:6379> INCR mynumber
(integer) 43
127.0.0.1:6379> DECR mynumber
(integer) 42
127.0.0.1:6379> exit

# Checking for protected mode
PS1> docker exec -it valkey valkey-cli
127.0.0.1:6379> config get *protect*
1) "protected-mode"
2) "no"
3) "enable-protected-configs"
4) "no"
127.0.0.1:6379> config get *bind*
1) "bind"
2) "* -::*"
3) "bind-source-addr"
4) ""
127.0.0.1:6379> exit

PS1> docker compose down valkey
```
## MariaDB

The MariaDB `root` password is `admin`, set in the `compose.yaml` file.

```console
PS1> docker exec -it mariadb bash
# mariadb -u root -p
MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.013 sec)
MariaDB [mysql]> use mysql;
MariaDB [mysql]> select host,user,password_expired from user limit 6;
+-----------+-------------+------------------+
| Host      | User        | password_expired |
+-----------+-------------+------------------+
| localhost | mariadb.sys | Y                |
| localhost | root        | N                |
| %         | root        | N                |
| 127.0.0.1 | healthcheck | N                |
| ::1       | healthcheck | N                |
| localhost | healthcheck | N                |
+-----------+-------------+------------------+
6 rows in set (0.001 sec)
MariaDB [mysql]> exit;
root@3f69733aef31:/# exit
```

**NOTE:** `SQLAlchemy` distinguishes between [MySQL and MariaDB](https://docs.sqlalchemy.org/en/20/dialects/mysql.html).

* [How to Create User With Grant Privileges in MariaDB](https://www.geeksforgeeks.org/how-to-create-user-with-grant-privileges-in-mariadb/)
* [MySQL Cheatsheet](https://nonbleedingedge.com/cheatsheets/mysql.html)
* [MySQL® Notes for Professionals book](https://goalkicker.com/MySQLBook/)

Example of how to create a `user`, set a password and `grant` access to the database `test`.

```console
PS1> docker exec -it mariadb bash
root@3f69733aef31:/# mariadb -u root -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 4
Server version: 11.6.2-MariaDB-ubu2404 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
MariaDB [(none)]>
MariaDB [(none)]> create database test;
Query OK, 1 row affected (0.007 sec)

# Need all IP's hence '%' (Docker Network is 192.168.65.0/24)
MariaDB [(none)]> CREATE USER 'user'@'%' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.004 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON test.* TO 'user'@'%' IDENTIFIED BY 'password';
Query OK, 0 rows affected (0.004 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> SHOW GRANTS FOR 'user'@'%'; 
+-------------------------------------------------------------------------------------------------------------+
| Grants for user@localhost                                                                                   |
+-------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `user`@`localhost` IDENTIFIED BY PASSWORD '*2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19' |
| GRANT ALL PRIVILEGES ON `test`.* TO `user`@`localhost`                                                      |
+-------------------------------------------------------------------------------------------------------------+
2 rows in set (0.000 sec)

MariaDB [(none)]> exit
Bye
root@3f69733aef31:/# mariadb -u user -p
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 5
Server version: 11.6.2-MariaDB-ubu2404 mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use test
Database changed
MariaDB [test]> show tables;
Empty set (0.004 sec)

MariaDB [test]> exit
```

There is a test script in the `src` folder called [mariadb-test.py](./src/mariadb-test.py)

## PostgreSQL
 
The Python versions of `psycopg2` and `psycopg2-binary` *DO NOT* install on Windows.

The pure python driver `pg8000` works with Python on Windows.

* [PyPi pg8000 1.31.2](https://pypi.org/project/pg8000/)
* [GitHub tlocke/pg8000](https://github.com/tlocke/pg8000/)
* [PostgreSQL® Notes for Professionals book](https://goalkicker.com/PostgreSQLBook/)

Use `docker compose (up -d|stop) postgres` to start, stop the container.

Like the other containers it is configured on `dev_net` to isolate it from any other containers.

```console
PS1> docker compose up -d postgres

## Login to container and Test `psql` interface:
PS1> docker exec -it postgres sh
#
# psql -U admin -W test
Password:
psql (17.2 (Debian 17.2-1.pgdg120+1))
Type "help" for help.

test=# select version();
                                                       version
---------------------------------------------------------------------------------------------------------------------
 PostgreSQL 17.2 (Debian 17.2-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
(1 row)

test=# exit
# exit
PS1>
```

There is a test script in the `src` folder called `posgres-test.py`

## MongoDB

Use `docker compose` to start, stop the container.

Like the other containers it is configured on `dev_net` to isolate it from any other containers.

Like the other databases, User `admin`, with Password `admin`

* [MongoDB](https://www.mongodb.com/)
* [TutorialsPoint: MongoDB - Overview](https://www.tutorialspoint.com/mongodb/mongodb_overview.htm)
* [TecAdmin: MongoDB Tutorials](https://tecadmin.net/tutorial/mongodb/mongodb-tutorials/)
* [W3Schools: MongoDB Overview](https://www.w3schools.in/mongodb/overview)
* [Welcome to MongoDB Shell (mongosh)](https://www.mongodb.com/docs/mongodb-shell/)
* [Python MongoDB](https://www.w3schools.com/python/python_mongodb_getstarted.asp)
* [GitHub mongo-express / mongo-express](https://github.com/mongo-express/mongo-express)

```console
PS1> docker exec -it mongodb sh      # Interactive Shell
PS1> docker exec -it mongodb bash    # Interactive Bash Shell
PS1> docker exec -it mongodb mongosh # Mongosh
```

## DbGate

A sophisticated WebUI for managing the databases, see the `compose.yaml` for the configuration details.

Like the other databases, User `admin`, with Password `admin`

* [DbGate is cross-platform SQL+noSQL database client](https://dbgate.org/docs/index.html)
* [Use storage database and administration for settings (Premium)](https://dbgate.org/docs/web-app-config.html)
* [DbGate - Environment Variables](https://dbgate.org/docs/env-variables.html)

```console
PS1> docker compose up -d dbgate

# Open from Docker-Desktop or
PS1> start "http://localhost:3000"

PS1> docker compose down dbgate
```

## SRC

Some simple example programs. A virtual environment should be created.

```console
PS1> python -m venv venv
PS1> venv\Scripts\activate
(venv)> python -m pip install --upgrade pip
(venv)> pip install -r requirements.txt --upgrade
(venv)> python <test-program>.py
(venv)> deactivate
PS1>
```

| Program          | Description               |
|------------------|---------------------------|
| format-dates.py  | Date formatting example   |
| odd-numbers.py   | Print odd number in range | 
| valkey-test.py   | Simple Valkey example     |
| mariadb-test.py  | Simple MariaDB example    |
| postgres-test.py | Simple PostgreSQL example |
| mongodb-test.py  | Simple MongoDB example    |

