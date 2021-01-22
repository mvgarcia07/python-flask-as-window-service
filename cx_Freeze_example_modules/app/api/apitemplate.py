from flask import jsonify, request, g, url_for, current_app
from . import api
from .functions.func_gral import *

import pandas as pd
import ssl

#from flask import current_app


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

@api.route('/hello', methods=['GET']) # OR GET We need to decide this!
def api_template(): 
    """

     Input: 
        * your file  :  description of the inputfile
    Function: description of the function   
    Output: 
        * your file file : description of the output file
    """
    pt_hora = print_pt_time()
        
    return "Hello from Portugal! our time is " + pt_hora
    
