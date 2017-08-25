"""
This script runs the FlaskWebProject1 application using a development server.
"""

from os import environ
from FlaskWebProject1 import app
import socket

if __name__ == '__main__':
    #HOST = environ.get('SERVER_HOST', 'localhost')
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    print(ip)
    app.run(ip, 5555)
