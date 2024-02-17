#!/usr/bin/env bash
#
git clone https://github.com/Mbed-TLS/mbedtls ../mbedtls
echo "Run following commands on mbdetls on git root"
echo "cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_EXPORT_COMPILE_COMMANDS=On -DCMAKE_BUILD_TYPE=Release -B build -G "Unix Makefiles" ."
echo "make -C build"
