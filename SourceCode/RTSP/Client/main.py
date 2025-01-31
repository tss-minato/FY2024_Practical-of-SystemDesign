import socket
import subprocess

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/DeviceInfo')
def device_info():
    return {
        'hostname': socket.gethostname()
    }