# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 21:14:11 2015

@author: David
"""

import pandas as pd
import json


'''Loop until all data has been downloaded, and then write to file'''
data = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&source=IBRD&rows=1&os=0&kw=N')
tempData = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&source=IBRD&rows=500&os=0&kw=N')
tempCount = 0

while len(tempData) > 0:
    data = data.append(tempData, ignore_index=True)
    tempCount += 500
    tempData = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&source=IBRD&rows=', tempCount, '&os=0&kw=N')
    
#data.to_json('jsonOutput.txt')

#test = pd.read_json('jsonOutput.txt')

#data01 = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&source=IBRD&rows=500&os=0&kw=N')
#data01 = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&source=IBRD&rows=500&os=16800&kw=N')
'''Loop until all data has been downloaded, and then write to file'''














'''INITIAL TRY USING FACTED DATA'''
'''
#data = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&source=IBRD&kw=N')
#data.projects.P150064['regionname']


data1 = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&fct=docty_exact,regionname_exact,countryname_exact,lendinginstr_exact,borrower_exact,supplementprojectflg_exact,impagency_exact,status_exact,mjsector_exact,sector_exact,goal_exact,theme_exact,boardapprovaldate_exact,countryshortname_exact,mjsectorcode_exact,board_approval_year_exact,fiscalyear,projectfinancialtype_exact,lang_exact,mjtheme_exact,sector_namecode_exact,mjsector_namecode_exact,theme_namecode_exact,mjtheme_namecode_exact,country_namecode_exact,countryname_mdk_exact,goalname_mdk_exact,lendinginstr_mdk_exact,lendinginstrtype_mdk_exact,mjsectorname_mdk_exact,sectorname_mdk_exact,themename_mdk_exact,mjthemename_mdk_exact,mtthemename_mdk_exact,project_name_mdk_exact,prodlinetext_mdk_exact,envassesmentcategorycode,combined_practice_code,combined_practice_name,ccsa_practice_code_exact,ccsa_practice_name_exact,teamleadname_exact,prodline_exact&source=IBRD&rows=500&os=0&kw=N')
data2 = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&fct=docty_exact,regionname_exact,countryname_exact,lendinginstr_exact,borrower_exact,supplementprojectflg_exact,impagency_exact,status_exact,mjsector_exact,sector_exact,goal_exact,theme_exact,boardapprovaldate_exact,countryshortname_exact,mjsectorcode_exact,board_approval_year_exact,fiscalyear,projectfinancialtype_exact,lang_exact,mjtheme_exact,sector_namecode_exact,mjsector_namecode_exact,theme_namecode_exact,mjtheme_namecode_exact,country_namecode_exact,countryname_mdk_exact,goalname_mdk_exact,lendinginstr_mdk_exact,lendinginstrtype_mdk_exact,mjsectorname_mdk_exact,sectorname_mdk_exact,themename_mdk_exact,mjthemename_mdk_exact,mtthemename_mdk_exact,project_name_mdk_exact,prodlinetext_mdk_exact,envassesmentcategorycode,combined_practice_code,combined_practice_name,ccsa_practice_code_exact,ccsa_practice_name_exact,teamleadname_exact,prodline_exact&source=IBRD&rows=500&os=500&kw=N')
#data.append(pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&fct=docty_exact,regionname_exact,countryname_exact,lendinginstr_exact,borrower_exact,supplementprojectflg_exact,impagency_exact,status_exact,mjsector_exact,sector_exact,goal_exact,theme_exact,boardapprovaldate_exact,countryshortname_exact,mjsectorcode_exact,board_approval_year_exact,fiscalyear,projectfinancialtype_exact,lang_exact,mjtheme_exact,sector_namecode_exact,mjsector_namecode_exact,theme_namecode_exact,mjtheme_namecode_exact,country_namecode_exact,countryname_mdk_exact,goalname_mdk_exact,lendinginstr_mdk_exact,lendinginstrtype_mdk_exact,mjsectorname_mdk_exact,sectorname_mdk_exact,themename_mdk_exact,mjthemename_mdk_exact,mtthemename_mdk_exact,project_name_mdk_exact,prodlinetext_mdk_exact,envassesmentcategorycode,combined_practice_code,combined_practice_name,ccsa_practice_code_exact,ccsa_practice_name_exact,teamleadname_exact,prodline_exact&source=IBRD&rows=500&os=500&kw=N'))
datax = pd.read_json('http://search.worldbank.org/api/v2/projects?format=json&fct=docty_exact,regionname_exact,countryname_exact,lendinginstr_exact,borrower_exact,supplementprojectflg_exact,impagency_exact,status_exact,mjsector_exact,sector_exact,goal_exact,theme_exact,boardapprovaldate_exact,countryshortname_exact,mjsectorcode_exact,board_approval_year_exact,fiscalyear,projectfinancialtype_exact,lang_exact,mjtheme_exact,sector_namecode_exact,mjsector_namecode_exact,theme_namecode_exact,mjtheme_namecode_exact,country_namecode_exact,countryname_mdk_exact,goalname_mdk_exact,lendinginstr_mdk_exact,lendinginstrtype_mdk_exact,mjsectorname_mdk_exact,sectorname_mdk_exact,themename_mdk_exact,mjthemename_mdk_exact,mtthemename_mdk_exact,project_name_mdk_exact,prodlinetext_mdk_exact,envassesmentcategorycode,combined_practice_code,combined_practice_name,ccsa_practice_code_exact,ccsa_practice_name_exact,teamleadname_exact,prodline_exact&source=IBRD&rows=500&os=18000&kw=N')


data = data1.append(data2)
'''
'''INITIAL TRY USING FACTED DATA'''
=======
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

>>>>>>> 058288cec2f5a71f9c1f651a31a3b712ff7981ef
