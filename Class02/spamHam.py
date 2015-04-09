# -*- coding: utf-8 -*-
"""
Created on Sun Apr 05 21:38:39 2015

@author: David
"""

import pandas as pd


data = pd.read_table('SMSSpamCollection', sep='\t')

data.count() #5,571 messages

