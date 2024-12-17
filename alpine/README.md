# Alpine

An interactive development container within Docker.

It communicates with the other containers over the Docker `dev_net` network.

The Python source needs to be in the `repo` folder. The folder name can be changed to match your git repo but 
the `compose.yaml` file needs updating. 

It is based on the official `python-alpine` container. A local development account, `devel` was added, and it can run 
superuser (root) commands via `doas` which requires a password, which is the same as the account name.

Creating a local `Virualenv` environment does not work, cause unknown, so the python packages are installed from the 
`requirement.txt` file during the container build. Any changes require that the container is rebuilt.

```console
PS1> docker compose down alpine
# Update the requirements.txt file
PS1> docker compose build alpine
PS1> docker compose up -d alpine
```

An alternative, untested approach, is to modify with `requiremnts.txt` file in the running `alpine` container

```console
# Update the requirements.txt file
$ doas pip install -r requirements.txt --upgrade
```

## Source code

The `repo` folder should contain the source from the `git` repository.

This folder is mounted into the `alpine` container as, `/home/devel/repo`

Editing should be done locally and not on the container itself, (although this is possible).

> Note read the *Windows/MacOS Unix line ending madness* section.

The name of the various hosts correspond to the `service` name in the `compose.yaml` file.

## Useful references

* [OpenBSD - Privileges](https://www.openbsdhandbook.com/system_management/privileges/)
* [OpenBSD - doas.conf](https://man.openbsd.org/OpenBSD-6.0/doas.conf.5)
* [Working with the Alpine Package Keeper (apk)](https://docs.alpinelinux.org/user-handbook/0.1a/Working/apk.html)
* [Apline Linux - Setting up a new user](https://wiki.alpinelinux.org/wiki/Setting_up_a_new_user)

## Windows/MacOS Unix line ending madness when using GIT on Windows

* [Configuring Git to handle line endings](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings)
* [gitattributes - Best Practices](https://rehansaeed.com/gitattributes-best-practices/)