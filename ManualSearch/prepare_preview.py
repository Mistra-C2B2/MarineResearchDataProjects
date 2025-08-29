# -*- coding: utf-8 -*-
# prepare_preview.py - review function - download data for the projects in master_list.csv that are unrated,  so can be reviewed in html. writes output.json

import requests
#import json
import pandas as pd 
import useful

# local config, tex passwords
import config
#from payload import payload
#from payload import search_id

unrated = useful.GetUnratedProjects()

# uses public token from https://www.vr.se/english/swecris/swecris-api.html
# the interface is described at https://swecris-api.vr.se/index.html

# simple script to get all projects for a "scb" subject

#API_KEY = 'VRSwecrisAPI2023-1'  # public token, check https://www.vr.se/english/swecris/swecris-api.html to get the latest

headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + config.API_KEY
}

# loop over the unrated, get project into
output=""
for index, row in unrated.iterrows():
  projectId = row['projectId']
  r = requests.get('https://swecris-api.vr.se/v1.0/projects/%s'%projectId, headers=headers)
  if (r.status_code==200):
    print("retrieved %s"%projectId)
    if (output==""):
      output = r.text
    else:
     output = ", ".join([output, r.text])
  else:
    print("ERROR loading project %s: status_code:%i"%(projectId,r.status_code))

output = "[" + output + "]"

# write out the output
with open('output.json', 'w', encoding='utf-8') as f:
    f.write(output)


    