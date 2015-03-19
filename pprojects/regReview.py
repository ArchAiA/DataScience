# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:36:47 2015

@author: david
"""

import requests
from lxml import etree
import pprint

#response = requests.get('http://www.reginfo.gov/public/do/XMLViewFileAction?f=EO_RULES_UNDER_REVIEW.xml')
#tree = ET.parse('http://www.reginfo.gov/public/do/XMLViewFileAction?f=EO_RULES_UNDER_REVIEW.xml')

#root = tree.getroot()
#print root


'''BUILDING AN XML TREE

#tree = etree.parse('http://www.reginfo.gov/public/do/XMLViewFileAction?f=EO_RULES_UNDER_REVIEW.xml')

root = etree.Element("OIRA_DATA")
#print(root.tag)
child02 = etree.SubElement(root, "REGACT")
child03 = etree.SubElement(child02, "AGENCY_CODE")
child04 = etree.SubElement(child02, "RIN")
child05 = etree.SubElement(child02, "TITLE")
child06 = etree.SubElement(child02, "STAGE")
child07 = etree.SubElement(child02, "ECONOMICALLY_SIGNIFICANT")
child08 = etree.SubElement(child02, "DATE_RECEIFVED")
child09 = etree.SubElement(child02, "LEGAL_DEADLINE")
child10 = etree.SubElement(child02, "HEALTH_CARE_ACT")
child11 = etree.SubElement(child02, "INTERNATIONAL_IMPACTS")

#print(etree.tostring(root, pretty_print = True))
child = root[0]

for child in child02:
    print(child.tag)
    

#print(child.tag)
#print(len(child02))

BUILDING AN XML TREE'''










'''PARSING XML ON THE INTERNET'''

#tree = etree.parse("http://www.reginfo.gov/public/do/XMLViewFileAction?f=EO_RULES_UNDER_REVIEW.xml")
root = etree.fromstring(tree)