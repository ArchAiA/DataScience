# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 21:14:11 2015

@author: David
"""

import pandas as pd
import matplotlib as plt

#The raw json data is really, really ugly, and unusable
rawdata = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&rows=10&os=0&source=IBRD&kw=N')

#data.projects.P114294['regionname']

#in order to make the raw data usable, we have to create a new dataframe
#by extracting the useful part of the raw dataframe
data = pd.DataFrame()

for item in rawdata.projects:
    data = data.append(item, ignore_index=True)

#Dealing with unicode...
data['lendprojectcost'] = data.lendprojectcost.astype(float)



data.countryshortname.value_counts()
data.groupby(data['countryshortname']).lendprojectcost.sum()
data.groupby(data['regionname']).lendprojectcost.sum() #This is having issues because unicode
data.approvalfy.value_counts()
data.lendinginstr.value_counts()
data.regionname.value_counts()
data.sectorcode.value_counts()
data.combined_practice_name.value_counts()

#Trying to get major theme...
#data.sector1[0]['Name']

