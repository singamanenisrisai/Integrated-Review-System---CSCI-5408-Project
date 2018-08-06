
#!/usr/bin/env python3

import json
import requests
import urllib
import csv
import flatten_json
import pandas as pd
from flatten_json import flatten
from pandas.io.json import json_normalize
import xml.etree.ElementTree as ET

r = requests.get("https://maps.googleapis.com/maps/api/place/details/xml?placeid=ChIJkaHLhCMiWksRHFVtgYtes4s&key=AIzaSyDaNdJ3K-mheI7m9B6NO3BdvOYomL_pSzE")
root = ET.fromstring(r.text)
tree = ET.ElementTree(root)
tree.write("goole_reveiws_file.xml")
