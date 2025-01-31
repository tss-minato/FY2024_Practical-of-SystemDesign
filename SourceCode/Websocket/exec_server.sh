#!/usr/bin/bash

venvPath='./venv/vxx_yyyymmdd/bin/activate'

source $venvPath
python ../server/exec_server.py
deactivate
