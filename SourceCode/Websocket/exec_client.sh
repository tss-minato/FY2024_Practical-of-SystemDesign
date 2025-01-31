#!/usr/bin/bash

venvPath='../venv/vxx_yyyymmdd/bin/activate'

source $venvPath
python ./client/exec_client.py
deactivate
