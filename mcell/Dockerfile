FROM nvidia/cuda:12.8.0-cudnn-runtime-ubuntu22.04

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Downloaded MCell/CellBlender v4.1.0 bundled with Blender 4.4.3 for Debian 12 from https://mcell.org/download.html
COPY ./Blender-4.4.3-CellBlender-4.1.0-Python-3.11.11-Debian-12-x86_64-20250507.tar.gz /tmp/

RUN mkdir /app/ \ 
    && tar -xf /tmp/Blender-4.4.3-CellBlender-4.1.0-Python-3.11.11-Debian-12-x86_64-20250507.tar.gz -C /app/ \
    && rm /tmp/Blender-4.4.3-CellBlender-4.1.0-Python-3.11.11-Debian-12-x86_64-20250507.tar.gz

# modules from https://developer.blender.org/docs/handbook/building_blender/linux/#__tabbed_1_2
RUN apt update && apt install -y build-essential \
    libx11-dev \
    libxxf86vm-dev \
    libxcursor-dev \
    libxi-dev \
    libxrandr-dev \
    libxinerama-dev \
    libegl-dev \
    libwayland-dev \
    wayland-protocols \
    libxkbcommon-dev \
    libdbus-1-dev \
    linux-libc-dev \
    mesa-utils \
    libgl1-mesa-glx \
    libsm6 \
    libxext6 \
    libxrender-dev

# Downloaded from https://github.com/mcellteam/neuropil_tools/releases/tag/4.1.0
COPY ./neuropil_tools.zip /app/

COPY ./settings.py /app/Blender-4.4.3-CellBlender/4.4/scripts/startup/

ENTRYPOINT ["/app/Blender-4.4.3-CellBlender/blender", "--python", "/app/Blender-4.4.3-CellBlender/4.4/scripts/startup/settings.py"]
