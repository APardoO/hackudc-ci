#!/usr/bin/env bash

#codee/bin/pwreport ../mbedtls/library/*.c --config ../mbedtls/build/compile_commands.json --json > ../codee-report.json
#codee/bin/pwreport --checks --verbose --config ../mbedtls/build/compile_commands.json --json > ../proc-json/codee-checks.json

#cd mbedtls
#cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_EXPORT_COMPILE_COMMANDS=On -DCMAKE_BUILD_TYPE=Release -B build -G "Unix Makefiles" .
#make -C build
#cd ..

CODEE_ACCEPT_EULA=yes && pwreport mbedtls/library/*.c --config mbedtls/build/compile_commands.json --json > codee-report.json
CODEE_ACCEPT_EULA=yes && pwreport --checks --verbose --config mbedtls/build/compile_commands.json --json > proc-json/codee-checks.json

CODEE_ACCEPT_EULA=yes && codee/bin/pwreport ../mbedtls/build/* --screening --config ../mbedtls/build/compile_commands.json --json > ../proc-json/codee-screening.json
CODEE_ACCEPT_EULA=yes && codee/bin/pwreport --checks --verbose --config ../mbedtls/build/compile_commands.json --sarif > ../codee-check.sarif
sarif html ../codee-check.sarif -o ../html/
python3 ../proc-json/order.py
python3 ../proc-json/autofix.py

