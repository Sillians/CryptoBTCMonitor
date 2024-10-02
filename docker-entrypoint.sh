#!/bin/sh

set -e

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

echo "Starting my workflow task application..."
# MY_FILE=code/src/cryptobtcmonitor/workflow/taskflow.py
# ./code -f "${MY_FILE}"

poetry run python3 -m "code/src/cryptobtcmonitor/workflow/taskflow.py"

# CMD ["prefect deployment run 'main/exchange-data-deployment'"]

# Evaluating passed command:
# exec "$@"