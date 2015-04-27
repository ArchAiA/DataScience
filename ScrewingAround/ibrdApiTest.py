# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:37:31 2015

@author: david
"""

import pandas as pd
import json

data = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&source=IBRD&kw=N')

data.to_csv('testData.csv')

