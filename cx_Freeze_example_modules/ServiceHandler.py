  
"""
Implements a simple service using cx_Freeze.
See below for more information on what methods must be implemented and how they
are called.
"""

import threading
import os
import sys
import cx_Logging

from init import app


class Handler:

    # no parameters are permitted; all configuration should be placed in the
    # configuration file and handled in the Initialize() method
    def __init__(self):
        self.stopEvent = threading.Event()
        self.stopRequestedEvent = threading.Event()

    # called when the service is starting
    def initialize(self, configFileName):
        self.directory = os.path.dirname(sys.executable)
        #cx_Logging.StartLogging(os.path.join(self.directory, "teste.log"), cx_Logging.DEBUG)
        cx_Logging.StartLogging(os.path.join("C:\\Data\\logs\\", "teste.log"), cx_Logging.DEBUG)
        #pass

    # called when the service is starting immediately after Initialize()
    # use this to perform the work of the service; don't forget to set or check
    # for the stop event or the service GUI will not respond to requests to
    # stop the service
    def run(self):
        cx_Logging.Debug("stdout=%r", sys.stdout)
        #sys.stdout = open(os.path.join(self.directory, "stdout.log"), "a")
        #sys.stderr = open(os.path.join(self.directory, "stderr.log"), "a")
        sys.stdout = open(os.path.join("C:\\Data\\logs\\", "stdout.log"), "a")
        sys.stderr = open(os.path.join("C:\\Data\\logs\\", "stderr.log"), "a")
        app.run(host="127.0.0.1",port=5123)
        self.stopRequestedEvent.wait()
        self.stopEvent.set()

    # called when the service is being stopped by the service manager GUI
    def stop(self):
        self.stopRequestedEvent.set()
        self.stopEvent.wait()
