from cx_Freeze import setup, Executable

#AG-comment: to run 'python setup.py build'

#include_files = [ 'app/templates/',
#                  'app/static/',]
include_files = []
# Note: without 'jinja2.ext' in this list, we won't get the templates working. 

#include = [ 'jinja2', 'jinja2.ext',]
include =['win32timezone']
flaskapp = Executable('ServiceHandler.py',base='Console') #is not working with'Win32Service 
                       
                  
setup(
    name="Flask-App-Test-cx-freeze",
    version="1.0",
    author="Angie garcia",
    description="Flask-App-Test-cx-freeze app Console",
    options={
        'build_exe': {
            'include_files': include_files,
            'includes': include,
            'build_exe': "build",
            "excludes": ["tkinter"]
        }
    },
    executables=[flaskapp]
)