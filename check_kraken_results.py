import os
import pandas as pd
import datetime


def check_file(file):
    print('Checking file...')
    print(file)
    df = pd.read_excel(file)
    print(df)
    

def _getToday():
        return datetime.date.today().strftime("%Y%m%d")
    

    