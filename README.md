# python-flask-as-window-service
These are the steps to create a flask applications as window services in windows 10 and python 3.8

Based on [https://stackoverflow.com/questions/55677165/python-flask-as-windows-service]


It is required to install all the libraries in virtual enviroment to be able to work

# Install Requierment in enviroment 
```sh
pip install virtualenv 
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

# Compile the application as window execuatble
The following commannd will generate a .exe in  dist directory
```sh
pyinstaller --onefile --hidden-import win32timezone win32_service.py
```

# Test the .exe  
```sh
cd dist
cd .\win32_service.exe debug
```

Check in browser http://localhost:8000/ to find the "hellow world" 

Ctrl C to kill the application, close the terminal windows because it kept running

# Install the application
Open a new powershell with **admin priviliges** 
```sh
cd dist
.\win32_service.exe install
```
# Start the application
Now, open the “Services” msc snap in
```sh
mmc Services.msc
```

Look for the service names  "FlaskAppTest" and run it manually

# Verify is working 
Check in browser http://localhost:8000/ to find the hellow world 
