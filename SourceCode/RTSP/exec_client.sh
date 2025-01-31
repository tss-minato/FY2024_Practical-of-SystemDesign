#!/usr/bin/bash

venvPath='../venv/vxx_yyyymmdd/bin/activate'

source $venvPath
cd ./Client
gunicorn -c ./gunicorn_conf.py main:app
cd ../
deactivate
