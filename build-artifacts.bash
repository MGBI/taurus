#!/bin/bash -xe
apt-get install -y --force-yes gcc-mingw-w64-x86-64 nsis
pip3 install "pynsist<2"

# build source distribution
./build-sdist.sh

# build a windows installer
./build-windows-installer.sh ./dist/bzt-*.tar.gz
