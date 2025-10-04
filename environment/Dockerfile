# hash:sha256:6e7882874050c554a7faa8de43d3386a9ad454667d23b70f5b2fabba98afe880
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/cuda-miniconda-jupyterlab:latest

ARG DEBIAN_FRONTEND=noninteractive
ARG GIT_ASKPASS
COPY git-askpass /

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential=12.9ubuntu3 \
        curl=7.81.0-1ubuntu1.21 \
        emacs=1:27.1+1-3ubuntu5.2 \
        gcc=4:11.2.0-1ubuntu1 \
        libcurl4-gnutls-dev=7.81.0-1ubuntu1.21 \
        libhdf5-dev=1.10.7+repack-4ubuntu2 \
        libssl-dev=3.0.2-0ubuntu1.20 \
        libxml2-dev=2.9.13+dfsg-1ubuntu0.9 \
        libzmq3-dev=4.3.4-2 \
        openssh-client=1:8.9p1-3ubuntu0.13 \
        wget=1.21.2-2ubuntu1.1 \
    && rm -rf /var/lib/apt/lists/*

COPY postInstall /
RUN --mount=type=secret,id=secrets . /run/secrets/secrets \
    && /postInstall
