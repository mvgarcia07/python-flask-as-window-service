# python-flask-as-window-service using cx_freeze
These are the steps to create a flask applications as window services in windows 10 and python 3.8 uning pyinstaller

Based on [https://github.com/marcelotduarte/cx_Freeze/tree/master/cx_Freeze/samples/service]


It is required to install all the libraries in virtual enviroment to be able to work

# Requierments
It required to install also the vs_buildtools and after that installed you need to restart the machine
[https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=buildtools]


# Install Requierment in enviroment 
```sh
pip install virtualenv 
python -m venv venv
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

# OPTION 1: Compile the application as window service executable
The following commannd will generate a .exe in  buils directory
```sh
python setup.py build
```

## Test the .exe  
```sh
cd build\exe.win-amd64-3.8\
.\cx_Freeze_Flask_Service.exe debug
```

# OPTION 2: Compile the application as window console executable
The following commannd will generate a .exe in  buils directory
```sh
python setup_console.py build
```

## Test the .exe  
```sh
cd build\win32_service.exe
.\cx_Freeze_Flask_Service.exe debug
```

Check in browser http://localhost:8000/ to find the "hellow world" 

Ctrl C to kill the application, close the terminal windows because it kept running

# Install the application
Open a new powershell with **admin priviliges** 
```sh
.\cx_Freeze_Flask_Service.exe install
```
# Start the application
Now, open the “Services” msc snap in
```sh
mmc Services.msc
```

Look for the service names  "FlaskAppTest" and run it manually

# Verify is working 
Check in browser http://localhost:8000/ to find the hellow world 
