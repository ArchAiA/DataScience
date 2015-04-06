# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:09:30 2015

@author: david
"""
'''
import pandas as pd


data = pd.read_table('SMSSpamCollection', sep='\t')
'''

'''THIS IS ALL TO BE DONE IN A TERMINAL'''

wc SMSSpamCollection #5574 Total messages (in this case lines)

There are 92,479 words, and 5,574 messages, so there is an average of 
16.59 words per message


[grep 'spam' SMSSpamCollection | wc] yields 747 lines (messages) that are
spam

[grep 'ham' SMSSpamCollection | wc] yields 4,831 lines (messages) that are
ham

73,979 total words for 4,831 messages yields 15.31 words per ham message
18,609 total words for 747 messages yields 24.91 words per spam message

[grep 'spam' SMSSpamCollection > spam.txt]
[grep 'ham' SMSSpamCollection > ham.txt]
