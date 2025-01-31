#!/usr/bin/bash

venvPath='../venv/vxx_yyyymmdd/bin/activate'

source $venvPath
python ./Client/exec_client.py
deactivate
