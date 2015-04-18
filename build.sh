#!/bin/bash

src_dir=$(dirname $(readlink -m $0))
buildtmp="/tmp/$(id -u)/$(basename $src_dir)/"

if [ -z "$BUILD_TMP" ]; then
    BUILD_TMP="$buildtmp"
fi

if [ -z "$PREFIX" ]; then
    read -ep "PREFIX=" -i /usr/local PREFIX
fi

if [ ! -d "${BUILD_TMP:-$buildtmp}" ]; then
    read -ep "BUILD_TMP=" -i "${BUILD_TMP:-$buildtmp}" BUILD_TMP
    [ -z "$BUILD_TMP" ] && BUILD_TMP="$buildtmp"
fi

if ! mkdir -vp "$BUILD_TMP" || ! cd "$BUILD_TMP"; then
    echo "couldn't create or chdir into BUILD_TMP=\"$BUILD_TMP\""
    exit 1
fi

if [ ! -n "$src_dir" -o ! -d "$src_dir" ]; then
    echo "couldn't figure out where $0 is"
    exit 1
fi

set -e

cmake -Wno-dev "-DCMAKE_INSTALL_PREFIX=${PREFIX:-/usr/local}" "$src_dir"
make

[ -z "$NO_INSTALL" ] && \
    sudo make install

if [ -n "$*" ]; then
    "$@"
fi
