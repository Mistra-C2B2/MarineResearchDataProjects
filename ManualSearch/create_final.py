# -*- coding: utf-8 -*-
# prepare_preview.py - review function - download data for the projects in master_list.csv that are unrated,  so can be reviewed in html. writes top_documents.json

import requests
#import json
import pandas as pd 
import useful
import json

import config


rated = useful.GetRatedProjects(3)

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
for index, row in rated.iterrows():
  projectId = row['projectId']
  projectId = projectId.replace(r'/', '%2F') 
  r = requests.get('https://swecris-api.vr.se/v1.0/projects/%s'%projectId, headers=headers)
  if (r.status_code==200):
    print("retrieved %s"%projectId)
    # remomove personal information!
    jsonData = json.loads(r.text)
    del jsonData['peopleList']
    #print(jsonData['fundingStartDate'])
    jsonData['fundingStartDate']=useful.SimplifyDate(jsonData['fundingStartDate'])
    #print(jsonData['fundingStartDate'])
    jsonData['fundingEndDate']=useful.SimplifyDate(jsonData['fundingEndDate'])
    textData = json.dumps(jsonData, ensure_ascii=False)
    if (output==""):
      output = textData
    else:
     output = ", ".join([output, textData])
  else:
    print("ERROR loading project %s: status_code:%i"%(projectId,r.status_code))

output = "[" + output + "]"

# write out the output
with open('top_documents.json', 'w') as f:
    f.write(output)


    