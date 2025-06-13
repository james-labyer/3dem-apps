#!/bin/sh

BIN_DIR="/ff/bin"
FF_LINK="https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US"

# download firefox tarball and grab filename
echo "Downloading firefox..."
ff_file_name=$(wget -nv -t 20 --content-disposition "$FF_LINK"  2>&1 | cut -d\" -f2)

# extract tarball into HOME/bin directory
echo "Extracting firefox to $BIN_DIR..."
tar -xf $ff_file_name --directory $BIN_DIR
