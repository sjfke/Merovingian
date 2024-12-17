FROM python:3-alpine
# Change User to perform privileged actions
USER 0

# ENV BUILDER_VERSION 1.0
ENV UID=1001
ENV WHEEL=10

WORKDIR /home/devel

# https://hub.docker.com/_/python/
# https://wiki.alpinelinux.org/wiki/Setting_up_a_new_user
RUN /sbin/apk update && /sbin/apk add doas

RUN adduser -g "Developer" -D -h /home/devel --uid ${UID} --shell /bin/ash devel -G wheel && echo "devel:devel" | chpasswd

### To avoid Windows/MacOS Unix line ending madness when using GIT on Windows
# https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings
# https://rehansaeed.com/gitattributes-best-practices/
RUN echo "permit persist :wheel" > /etc/doas.conf && chown -c root:root /etc/doas.conf && chmod -c 0400 /etc/doas.conf

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER ${UID}
# USER 0

# DO NOT SET a default port for this image
# EXPOSE ${PORT}

# CMD ["/bin/bash","-c","while true ; do sleep 1; done;"]
CMD ["/bin/ash","-c","tail -f /dev/null"]