#!/usr/bin/env bash

../codee/bin/pwreport ../mbedtls/library/*.c  --json > ../codee-report.json
../codee/bin/pwreport --checks --verbose --config ../mbedtls/build/compile_commands.json --json > ../proc-json/codee-checks.json
../codee/bin/pwreport ../mbedtls/build/* --screening --config ../mbedtls/build/compile_commands.json --json > ../proc-json/codee-screening.json
../codee/bin/pwreport --checks --verbose --config ../mbedtls/build/compile_commands.json --sarif > ../codee-check.sarif
