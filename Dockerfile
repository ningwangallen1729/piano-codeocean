# PIANO: Probabilistic Inference Autoencoder Networks for multi-Omics
# Copyright (C) 2025 Ning Wang

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# hash:sha256:efe04cd2567bb9241fc6b72a3fb36d96271710494fb18df0bd31e189420457d0
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/cuda-miniconda-jupyterlab:latest

COPY requirements.txt /tmp/

# Install standard Linux server packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    openssh-client \
    curl \
    wget \
    libcurl4-gnutls-dev \
    libxml2-dev \
    libssl-dev \
    libzmq3-dev \
    libhdf5-dev \
    emacs \
    vim && \
    rm -rf /var/lib/apt/lists/*

# Install uv (static binary)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Install pip for Python 3.10
RUN /root/.local/bin/uv pip install --system -r /tmp/requirements.txt

# Final environment verification
RUN python3 --version
