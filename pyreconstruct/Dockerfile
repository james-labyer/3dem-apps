FROM python:3.11.12-bullseye

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

RUN pip install pyreconstruct

RUN chmod 777 /usr/local/lib/python3.11/site-packages/PyReconstruct/assets/welcome_series/.welcome /usr/local/lib/python3.11/site-packages/PyReconstruct/assets/welcome_series/.welcome/welcome.0.s0

RUN mkdir /app

COPY --from=taccaci/interactive-base:1.1.0 /tapis /tapis

RUN chmod +x /tapis/run.sh /app/setup.sh

CMD [ "/tapis/run.sh" ]
