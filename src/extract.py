import pandas as pd 
from config.config import Raw_Data

def extract():
    return pd.read_csv(Raw_Data)
