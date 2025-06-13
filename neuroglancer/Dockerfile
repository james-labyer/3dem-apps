FROM condaforge/miniforge3:24.11.3-2
LABEL maintainer="James Labyer <james.labyer@gmail.com>"

# Configure ENV
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update && apt-get install -y \
    ssh \
    vim \
    curl \
    libgtk-3-dev \
    libasound2-dev \
    xz-utils \
    && rm -rf /var/lib/apt/lists/*

# COPY in the conda environment yaml file
COPY ./ng.yaml /tmp/ng.yaml

# install the custom conda environment
ARG ENV_NAME=/app/ng

RUN conda update conda && conda update --all

RUN conda env create -f /tmp/ng.yaml -p ${ENV_NAME} \
    && echo "conda activate ${ENV_NAME}" >> /etc/skel/.bashrc \
    && echo "conda activate ${ENV_NAME}" >> ~/.bashrc

ENV PATH=${ENV_NAME}/bin:$PATH

COPY ./start.ipynb ./install_firefox_linux-x86_64.sh ./setup.sh /app/

RUN chmod +x /app/start.ipynb /app/install_firefox_linux-x86_64.sh /app/setup.sh

RUN chmod +rw /app/start.ipynb

RUN mkdir -p /ff/bin

WORKDIR /app

RUN /app/install_firefox_linux-x86_64.sh

ENTRYPOINT ["/app/setup.sh"]
