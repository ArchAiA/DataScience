# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:47:35 2015

@author: david
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#iris = pd.read_csv('iris.data')

col_names = ['slength', 'swidth', 'plength', 'pwidth', 'irisclass']
iris = pd.read_csv('iris.data', names=col_names)


iris.shape
iris.head()
iris.describe()
iris.dtypes
iris.isnull().sum()
iris.irisclass.value_counts()

iris['ratio'] = iris.plength / iris.pwidth
iris.groupby('irisclass').mean()
iris.boxplot(by='irisclass')
iris.groupby('irisclass').min()
iris.groupby('irisclass').max()

iris.sort_index(by='plength').values
iris.sort_index(by='pwidth').values
iris.sort_index(by='slength').values
iris.sort_index(by='slength').values

iris[(iris.pwidth >= 1.4) & (iris.pwidth <= 1.8 )]



#We can clearly tell iris-setosa apart by pwidth 0.75