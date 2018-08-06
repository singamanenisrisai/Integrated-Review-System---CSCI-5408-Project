#!/usr/bin/env python3

import xml.etree.ElementTree as ET
from xml.dom import minidom
import pandas as pd
import csv

df = pd.DataFrame(columns=['SentimentText'])

xmldoc = minidom.parse('goole_reveiws_file.xml')
itemslist = xmldoc.getElementsByTagName('text')

print("*********************Reviews************************")
for review in itemslist:
    df = df.append({'SentimentText':review.childNodes[0].nodeValue}, ignore_index=True)
    print(review.childNodes[0].nodeValue)

print("****************************************************")
df
df.to_csv('reviews.csv', sep=',',index=False, encoding='utf-8')
