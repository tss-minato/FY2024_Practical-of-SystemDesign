#!/usr/bin/bash

venvPath='../venv/20250124/bin/activate'

source $venvPath
python ./exec_client.py
deactivate
