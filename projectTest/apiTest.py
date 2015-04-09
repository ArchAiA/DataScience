# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 21:14:11 2015

@author: David
"""

import pandas as pd

data = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&source=IBRD&kw=N')

data.projects.P150064['regionname']
