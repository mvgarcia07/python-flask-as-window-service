import os
import pandas as pd
from datetime import datetime
import pytz



#from dotenv import load_dotenv
#load_dotenv()

def load_env_path():
    """
     Input: 
        * your file  :  description of the inputfile
    Function: description of the function   
    Output: 
        * your file file : description of the output file
    """
    with open(os.getenv('DATA_DIR_INPUT_FILE')) as f:
        print(f)
    return f
    
def print_pt_time():
    """
     Input: 
        * your file  :  description of the inputfile
    Function: description of the function   
    Output: 
        * your file file : description of the output file
    """
    tz_pt = pytz.timezone('Europe/Lisbon')
    datetime_pt = datetime.now(tz_pt)
    text_print= datetime_pt.strftime("%H:%M:%S")
    print(text_print)
    return text_print
    

    
