import pandas as pd
import numpy as np
import glob


def load_data(path):
    '''
    arguments:
    - path: file directory where .csv files are saved
    returns: dictionary of {'file_name': pd.DataFrame}
    '''
    if path[-1]!='/': 
        path += '/'
    jpx_data = {}
    for file in glob.glob(path+"*.csv"):
        jpx_data[file.replace(path,"").split('.csv')[0]] = pd.read_csv(file)
    return jpx_data
