"""
A simple setup script for creating a Windows service.
See the comments in the Config.py and ServiceHandler.py files for more
information on how to set this up.
Installing the service is done with the option --install <Name> and
uninstalling the service is done with the option --uninstall <Name>. The
value for <Name> is intended to differentiate between different invocations
of the same service code -- for example for accessing different databases or
using different configuration files.
"""

from cx_Freeze import setup, Executable
import sys

options = {
    "build_exe": {
        "includes": ["ServiceHandler","cx_Logging","jinja2.ext"],
        "excludes": ["tkinter"],
         "packages": ["app"],
         "path": sys.path,
    }
}

executables = [
    Executable(
        "Configws.py",
        base="Win32Service",
        target_name="FlaskService_modules.exe",
    ),
    
    Executable(
        "init.py",
        base="Console",
        target_name="FlaskService_modules_console.exe",
    )
]

setup(
    name="FlaskService",
    version="0.1",
    description="Sample cx_Freeze Windows service",
    executables=executables,
    options=options,
)