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

PS1> docker compose down valkey
```

## PostgreSQL

Use `docker compose` to start, stop the container.

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

## Python

* [Docker Interactive Mode in Python 3 Programming](https://dnmtechs.com/using-docker-interactive-mode-in-python-3-programming/)
* [Installing Python in Alpine Linux](https://www.askpython.com/python/examples/python-alpine-linux)
