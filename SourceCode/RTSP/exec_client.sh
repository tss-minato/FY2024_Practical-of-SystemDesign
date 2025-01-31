#!/usr/bin/bash

venvPath='../venv/v11_20250131/bin/activate'

source $venvPath
python ./Client/main.py
deactivate
