# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pprint


# request data from the Echo Nest API
r = requests.get('https://api.data.gov/gsa/fbopen/v0/opps?q=software+development&api_key=Wa82hDRABKsVxBLg0k9zIUulQDoo9Umj2lPt7PYb')
t = requests.get('https://api.data.gov/gsa/fbopen/v0/opps?q=bioinformatics&data_source=grants.gov&start=20&show_closed=true&api_key=Wa82hDRABKsVxBLg0k9zIUulQDoo9Umj2lPt7PYb')

top = r.json()
pprint.pprint(top)

