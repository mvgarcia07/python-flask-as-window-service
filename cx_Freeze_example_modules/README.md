# API Template with modules to deploy as window service using cx_freeze 
Flask application with modules that give Portugal time as output

These are the steps to create a flask applications as window services in windows 10 and python 3.8 uning cx_freeze

Based on [https://github.com/marcelotduarte/cx_Freeze/tree/master/cx_Freeze/samples/service]


It is required to install all the libraries in virtual enviroment to be able to work

# Requierments
It required to install also the vs_buildtools and after that installed you need to restart the machine
[https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=buildtools]


# Install Requierment in enviroment 
```sh
pip install virtualenv 
pip instal
.\venv\Scripts\Activate
pip install -r requirements.txt
```

# If Error in cx-Logging library for python 3.8
cx_Logging hasn't wheels/binary for py38+ and has to be compiled. It needs a C compiler, or you can get a compiled wheel at https://www.lfd.uci.edu/~gohlke/pythonlibs/#cx_logging

Donwload the corresponding whell to your operating system and inside the virtual enviroments 
```sh
py -m pip install cx_Logging-2.2-cp38-cp38-win_amd64.whl
```
or
```sh
pip whell install cx_Logging-2.2-cp38-cp38-win_amd64.whl
```
# Build the application
The following commannd will generate a .exe in  'build' directory

```sh
python setup.py build
```
## OPTION 1: run the application as console
```sh
cd build\exe.win-amd64-3.8\
.\FlaskService_modules_console.exe
```
## OPTION 2: run the application as window service executable 
#### UPDATE JAN 2021 It is having issues starting the services with error 1053 

### install the .exe  
Open a powershell with admin priviliges 
```sh
cd build\exe.win-amd64-3.8\
.\FlaskService_modules.exe --install test
```
or to uninstall
```sh
.\FlaskService_modules.exe --uninstall test
```
# Test the .exe  
Check in browser http://127.0.0.1:5123/api/v1/hello to find the "hello from Portugal" 
