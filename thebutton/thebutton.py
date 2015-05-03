# -*- coding: utf-8 -*-
"""
Created on Sat May 02 10:09:08 2015

@author: David
"""

import pandas as pd

data = pd.read_csv('http://tcial.org/the-button/button_clicks.csv', parse_dates=[[1,2]])