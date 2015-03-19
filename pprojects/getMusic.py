# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 18:50:11 2015

@author: david
"""
'''
import requests
import pprint

r = requests.get('http://developer.echonest.com/api/v4/artist/top_hottt?api_key=KZHZLVHW61KNOZ7AP&format=json')


r.text
r.json()
type(r.json())
top = r.json()


artists = top['response']['artists']
artists_data = [artist.values() for artist in artists]
artists_header = artists[0].keys()

pprint.pprint(artists_header)
pprint.pprint(artists_data)

'''


'''
import requests
import csv
import pprint

r = requests.get('https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-ticket-prices/2014-average-ticket-price.csv')
data = [row for row in csv.reader(r.iter_lines())]

'''


import requests
from xml.etree import ElementTree
import pprint


r = requests.get('http://www.reginfo.gov/public/do/XMLViewFileAction?f=EO_RULES_UNDER_REVIEW.xml')
tree = ElementTree.fromstring(r.content)

print tree