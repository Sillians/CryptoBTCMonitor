#!/bin/sh
set -e

# Activate the virtual environment, allowing the use of the installed dependencies.
. /opt/pysetup/.venv/bin/activate

# Set the code directory path
CODE_DIR="/code/src/cryptobtcmonitor/workflow"

# Get the file name to run (default: taskflow.py)
MY_FILE=${1:-taskflow.py}

echo "Starting my workflow task application: $MY_FILE"

# Run the Python script
python3 "$CODE_DIR/$MY_FILE"
