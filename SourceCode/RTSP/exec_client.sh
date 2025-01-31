#!/usr/bin/bash

venvPath='../venv/vxx_yyyymmdd/bin/activate'

source $venvPath
gunicorn -c ./Client/gunicorn_conf.py main:app 
deactivate
