# Merovingian

He was an exiled program within the Matrix who figuratively appeared as one of the kingpin figures.

> Choice is an illusion created between those with power and those without.
>
> -- <cite>The Merovingian</cite>

The project demonstrates using various containers for SQL and NoSQL databases from within and outside `Docker`.

All are configured to be accessible via the windows command line and store their data in a `data` subfolder.

Although not tested, the project should also work ``as-is`` on a UNIX platform with `docker` installed or 
using the `docker-compose` module for `Podman`.

* [Install Docker Desktop on Linux](https://docs.docker.com/desktop/setup/install/linux/)
* [How to use docker-compose with Podman on Linux](https://linuxconfig.org/how-to-use-docker-compose-with-podman-on-linux)
* [`podman kube generate` Generate Kubernetes YAML based on containers, pods or volumes](https://docs.podman.io/en/latest/markdown/podman-kube-generate.1.html)

## Docker and Docker Compose

* [Docker CLI](https://docs.docker.com/reference/cli/docker/)
* [Compose file reference](https://docs.docker.com/reference/compose-file/)
* [Sharing local files with containers](https://docs.docker.com/get-started/docker-concepts/running-containers/sharing-local-files/)
* [Volumes](https://docs.docker.com/engine/storage/volumes/)

## SQL and NoSQL Databases

### Valkey

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
* `valkey-vanilla`, which is commented-out, deploys the one from DockerHub, with a default configuration

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
### MariaDB

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
MariaDB [(none)]> CREATE DATABASE test;
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

### PostgreSQL
 
The Python versions of `psycopg2` and `psycopg2-binary` *DO NOT* install on Windows.

The pure python driver `pg8000` works with Python on Windows.

* [Python drivers for PostgreSQL](https://wiki.postgresql.org/wiki/Python)
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
# psql -U admin -W postgres
Password:
psql (17.2 (Debian 17.2-1.pgdg120+1))
Type "help" for help.

postgres=# select version();
                                                       version
---------------------------------------------------------------------------------------------------------------------
 PostgreSQL 17.2 (Debian 17.2-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
(1 row)

postgres=# \l
                                                 List of databases
   Name    | Owner | Encoding | Locale Provider |  Collate   |   Ctype    | Locale | ICU Rules | Access privileges
-----------+-------+----------+-----------------+------------+------------+--------+-----------+-------------------
 postgres  | admin | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           |
 template0 | admin | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/admin         +
           |       |          |                 |            |            |        |           | admin=CTc/admin
 template1 | admin | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/admin         +
           |       |          |                 |            |            |        |           | admin=CTc/admin
(3 rows)

postgres=# CREATE DATABASE test;
CREATE DATABASE
postgres=# \l
                                                 List of databases
   Name    | Owner | Encoding | Locale Provider |  Collate   |   Ctype    | Locale | ICU Rules | Access privileges
-----------+-------+----------+-----------------+------------+------------+--------+-----------+-------------------
 postgres  | admin | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           |
 template0 | admin | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/admin         +
           |       |          |                 |            |            |        |           | admin=CTc/admin
 template1 | admin | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           | =c/admin         +
           |       |          |                 |            |            |        |           | admin=CTc/admin
 test      | admin | UTF8     | libc            | en_US.utf8 | en_US.utf8 |        |           |
(4 rows)
```

Create `example` database using either the `localhost` or from the `alpine` container.

```console
PS1> cd src
PS1> .\venv\Scripts\activate
PS1> python .\postgres-test.py
```

```console
PS1> docker exec it posgres sh
#  psql -U admin -W test

test=# \dt
        List of relations
 Schema |  Name   | Type  | Owner
--------+---------+-------+-------
 public | example | table | admin
(1 row)

test=# \d example
                                   Table "public.example"
 Column |         Type          | Collation | Nullable |               Default
--------+-----------------------+-----------+----------+-------------------------------------
 id     | integer               |           | not null | nextval('example_id_seq'::regclass)
 name   | character varying(20) |           | not null |
Indexes:
    "example_pkey" PRIMARY KEY, btree (id)

test=# select * from example;
 id |   name
----+-----------
  1 | Ashley
  2 | Barry
  3 | Christina
(3 rows)
    
test=# exit
# exit
PS1> docker compose down postgres
```

There is a test script in the `src` folder called [postgres-test.py](./src/postgres-test.py)


### MongoDB

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
PS1> docker compose up -d mongodb
PS1> docker exec -it mongodb sh      # Interactive Shell
PS1> docker exec -it mongodb bash    # Interactive Bash Shell
PS1> docker exec -it mongodb mongosh # Mongosh
docker exec -it mongodb mongosh
Current Mongosh Log ID: 67585e6ed11efa7bb4e94969
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.4
Using MongoDB:          8.0.3
Using Mongosh:          2.3.4

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/

test> db
test
test> exit
PS1> docker compose down mongodb
```

> **Warning**
> 
> For `MongoDB` to search the `data` folder, it will create an automatic `docker volume` into which it mounts 
> Windows `mongodb\data` folder. 
> 
> The `docker volume` is not removed when the `service` is stopped, so periodically run `docker volume prune` 
> to remove any unused `docker volumes`.

There is a test script in the `src` folder called [mongodb-test.py](./src/mongodb-test.py)

## Database Administration tools

### AdminerEvo

`AdminerEvo` is a fork of Adminer, but it's better maintained and has more features.

It's a full-featured database management tool written in PHP, which supports

* `MySQL`, `MariaDB`, `PostgreSQL`, `SQLite`, `MS SQL`, `Oracle`, `Elasticsearch` and `MongoDB`.

Useful references

* [DockerHub: Adminerevo](https://hub.docker.com/r/shyim/adminerevo)
* [GitHub: shyim/adminerevo-docker](https://github.com/shyim/adminerevo-docker)

`Adminerevo` is normally installed alongside the database in the same container but here it uses a standalone container. 

**Note:** `MongoDB` was not working when this documentation as written.

```console
PS1> docker compose up -d adminrevo
PS1> start "http://127.0.1.1:8080"
PS1> docker compose down adminrevo
```

The *WebUI Login* details are as follows:

| System     | Server   | Username | Password | Database |
|------------|----------|----------|----------|----------|
| MySQL      | mariadb  | user     | password |          |
| PostgreSQL | postgres | admin    | admin    |          |

### DbGate

A sophisticated WebUI for managing the databases, see the `compose.yaml` for the configuration details.

Like the other databases, User `admin`, with Password `admin`

* [DbGate is cross-platform SQL+noSQL database client](https://dbgate.org/docs/index.html)
* [Use storage database and administration for settings (Premium)](https://dbgate.org/docs/web-app-config.html)
* [DbGate - Environment Variables](https://dbgate.org/docs/env-variables.html)

Unlike other containers `DbGate` is not configured to store its data on the local system but in a `docker volume`, 
so this must be created before trying to start the `dbgate` service.

```console
PS1> docker volume create dbgate-data 
PS1> docker volume ls
DRIVER    VOLUME NAME
local     64ade407fdcd1a212cdc45be88912b3b7bd568cf37b4ffc97ef556043461a818
local     295a1fe10ebb426f70b1f00eac472897c7482bed9bce4df2842ef2956cf07ba3
local     756c8b618be37350b915d98fe9e14b83e26df32b34d99eee2b189b17747ddd1c
local     dbgate-data
```
To start and stop the service.

```console
PS1> docker compose up -d dbgate

# Open from Docker-Desktop or
PS1> start "http://localhost:3000"

PS1> docker compose down dbgate
```

When the `dbgate` service is no longer required do not forget to delete the `docker volume`

```console
PS1> docker volume rm dbgate-data
```

### Mongo-Express

`mongo-express` is a web-based MongoDB admin interface written in `Node.js`, `Express.js`, and `Bootstrap3`.

Useful references

* [DockerHub: Mongo Express](https://hub.docker.com/_/mongo-express/)
* [GitHub: Mongo Express](https://github.com/mongo-express/mongo-express)

> Security Notice
>
> JSON documents are parsed through a javascript virtual machine, so the web interface can be used for executing malicious javascript on a server.
>
> `mongo-express` should only be used privately for development purposes.

```console
PS1> docker compose up -d mongo-express
PS1> start "http://127.0.1.1:8081"
PS1> docker compose down mongo-express
```

## Interaction and Testing

### SRC

Some simple example programs that work from your local system. 
The docker containers need to be running and are accessed via `localhost`

A virtual environment should be created.

```console
PS1> docker compose up -d
PS1> python -m venv venv
PS1> venv\Scripts\activate
(venv)> python -m pip install --upgrade pip
(venv)> pip install -r requirements.txt --upgrade
(venv)> python <test-program>.py
(venv)> deactivate
PS1> docker compose down
PS1>
```

| Program           | Description                 |
|-------------------|-----------------------------|
| format-dates.py   | Date formatting example     |
| odd-numbers.py    | Print odd number in range   | 
| valkey-test.py    | Simple Valkey example       |
| valkey-example.py | Valkey Interactive examples |
| mariadb-test.py   | Simple MariaDB example      |
| postgres-test.py  | Simple PostgreSQL example   |
| mongodb-test.py   | Simple MongoDB example      |

### Alpine

Is an example development container, based on the official `python-alpine` container.

> Please see `README.md` in the `alpine` folder for specifics.

It communicates with the other containers over the Docker `dev_net` network.

The local `alpine\repo` folder is mounted in a `devel` account and provides access to run the source code. 

```console
PS1> docker compose up -d dbgate
PS1> docker exec -it alpine ash
PS1> docker compose down alpine
```

The same examples as the `src` folder but using the docker `service` names, rather than `localhost` to 
create the connection.

| Program           | Description                 |
|-------------------|-----------------------------|
| format-dates.py   | Date formatting example     |
| odd-numbers.py    | Print odd number in range   | 
| valkey-test.py    | Simple Valkey example       |
| valkey-example.py | Valkey Interactive examples |
| mariadb-test.py   | Simple MariaDB example      |
| postgres-test.py  | Simple PostgreSQL example   |
| mongodb-test.py   | Simple MongoDB example      |

The source code is best edited on your local system.

Your local system is probably not Linux, so be aware of 
*"Windows/MacOS Unix line ending madness when using GIT on Windows"*

* [Configuring Git to handle line endings](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)
* [gitattributes - Best Practices](https://rehansaeed.com/gitattributes-best-practices/)