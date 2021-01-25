from flask import Flask
from app import create_app
import os
import sys
import cx_Logging

app = create_app('default')

cx_Logging.Debug("stdout=%r", sys.stdout)
sys.stdout = open(os.path.join("C:\\Data\\logs\\", "stdout_console.log"), "a")
sys.stderr = open(os.path.join("C:\\Data\\logs\\", "stderr_console.log"), "a")
cx_Logging.StartLogging(os.path.join("C:\\Data\\logs\\", "teste_console.log"), cx_Logging.DEBUG)

if __name__ == "__main__":

    app.run(host="127.0.0.1",port=5123)
    
    