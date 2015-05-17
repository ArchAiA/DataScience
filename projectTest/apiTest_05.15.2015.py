# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 21:14:11 2015

@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('/home/david/projects/data/wb')
#data = pd.read_csv('wbprojects.csv', thousands=';')
awards = pd.read_csv('wbawards.csv')



'''AWARDS'''
#Strip Whitenspace
awards.columns = awards.columns.str.replace(' ', '_')
awards.columns = awards.columns.str.replace('(', '')
awards.columns = awards.columns.str.replace(')', '')
awards.columns = awards.columns.str.lower()

awards = awards.rename(columns = {'total_contract_amount_usd':'contract_amount'})
awards.contract_amount = awards.contract_amount.str.replace('$', '')

awards.contract_amount = awards.contract_amount.convert_objects(convert_numeric=True)



#What Has Project Funding Been Like Over The Years
awards.groupby(awards.fiscal_year).contract_amount.sum()




#Which Countries are Getting the Contracts?
country_contracts = awards.groupby('supplier_country').contract_amount.sum()
country_contracts.sort('contract_amount', ascending=False)
country_contracts
#It appears that China ($30B), India ($17B), Brazil ($7.6B) are the top service providers


#Are any countries dominant in a sector
awards.major_sector.value_counts()
awards.groupby(awards.major_sector).supplier_country.value_counts()
#The top major sectors are Public Administration, Health, Transport, Water, and Agriculture

#Providers of the top major sectors by country
awards[awards.major_sector == "Public Administration, Law, and Justice"].groupby(awards.supplier_country).count()
awards[awards.major_sector == "Health and other social services"].groupby(awards.supplier_country).count()
awards[awards.major_sector == "Water, sanitation and flood protection"].groupby(awards.supplier_country).count()
awards[awards.major_sector == "Transportation"].groupby(awards.supplier_country).count()
awards[awards.major_sector == "Agriculture, fishing, and forestry"].groupby(awards.supplier_country).count()

#Top major sectors average contract value
awards[awards.major_sector == "Public Administration, Law, and Justice"].contract_amount.describe()





'''AWARDS'''




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

