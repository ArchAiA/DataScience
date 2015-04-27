# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 21:14:11 2015

@author: David
"""

import pandas as pd
import matplotlib as plt

#The raw json data is really, really ugly, and unusable
#rawdata = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&rows=10&os=0&source=IBRD&kw=N')
#rawdata = pd.read_csv('jsonOutput3.txt')
rawdata = pd.read_csv('wbprojects.csv', thousands=';')
data = rawdata
#data.projects.P114294['regionname']

#in order to make the raw data usable, we have to create a new dataframe
#by extracting the useful part of the raw dataframe
data = pd.DataFrame()

for item in rawdata.projects:
    data = data.append(item, ignore_index=True)

#Dealing with unicode...
data['lendprojectcost'] = data.lendprojectcost.astype(float)

'''USING CSV'''
data.countryname.value_counts().head(10)
data.groupby(data.countryname).lendprojectcost.mean().head()

#Top Recipients of World Bank Aid
tempLend = data.groupby(data.countryname).lendprojectcost.sum()
tempLend.sort('lendprojectcost', ascending=False)
tempLend.head(10)
#Top Recipients of World Bank Aid

data.groupby(data['regionname']).lendprojectcost.sum() #This is having issues because unicode
#data.boardapprovaldate.value_counts()
data.lendinginstr.value_counts()
data.regionname.value_counts()
data.sector1.value_counts().head(10)
data.theme1.value_counts().head(10)

'''USING CSV'''

'''USING API'''
data.countryshortname.value_counts()
data.groupby(data['countryshortname']).lendprojectcost.sum()
data.groupby(data['regionname']).lendprojectcost.sum() #This is having issues because unicode
data.approvalfy.value_counts()
data.lendinginstr.value_counts()
data.regionname.value_counts()
data.sectorcode.value_counts()
data.combined_practice_name.value_counts()
'''USING API'''

#Trying to get major theme...
#data.sector1[0]['Name']

