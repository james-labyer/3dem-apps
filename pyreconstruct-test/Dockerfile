FROM condaforge/miniforge3:24.11.3-2

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# System dependencies
# qt6 deps from https://doc.qt.io/qt-6/linux-requirements.html
RUN apt-get update && \
    apt-get upgrade -y  && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y bison \
    build-essential \
    bzip2 \
    ca-certificates \
    git \
    libfontconfig1-dev \
    libfreetype-dev \
    libgtk-3-dev \
    libx11-dev \
    libx11-xcb-dev \
    libxcb-cursor-dev \
    libxcb-glx0-dev \
    libxcb-icccm4-dev \
    libxcb-image0-dev \
    libxcb-keysyms1-dev \
    libxcb-randr0-dev \
    libxcb-render-util0-dev \
    libxcb-shape0-dev \
    libxcb-shm0-dev \
    libxcb-sync-dev \
    libxcb-util-dev \
    libxcb-xfixes0-dev \
    libxcb-xkb-dev \
    libxcb1-dev \
    libxext-dev \
    libxfixes-dev \
    libxi-dev \
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    libxrender-dev \
    wget \
    x11-apps \
    vim-tiny && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./PyReconstruct/requirements.txt /app/requirements.txt

COPY ./environment.yaml /app/environment.yaml

# CONDA_DIR is exported in base image
RUN source ${CONDA_DIR}/bin/activate \
    && conda init --all

ARG ENV_NAME=pyrecon_dev

RUN conda env create -f environment.yaml \
    && echo "conda activate ${ENV_NAME}" >> /etc/skel/.bashrc \
    && echo "conda activate ${ENV_NAME}" >> ~/.bashrc

ENV PATH=/opt/conda/envs/${ENV_NAME}/bin:$PATH

COPY ./run.sh /tapis/run.sh

RUN chmod +x /tapis/run.sh

ENTRYPOINT [ "/tapis/run.sh" ]
