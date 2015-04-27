# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:42:04 2015

@author: david
"""

import requests
import json

sample_sentence = "Fuck this shit, it sucks."

url = 'http://www.datasciencetoolkit.org/text2sentiment/'
header = {'content-type':'applicatin/json'}

body = sample_sentence
response = requests.post(url, data=body, headers=header)

response.status_code