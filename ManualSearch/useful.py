# -*- coding: utf-8 -*-

import config
import pandas as pd
import requests
import json
from dateutil.parser import parse

def GetUnratedProjects():
  '''
  Return a dataframe with unrated projects from file config.master_list
  '''
  ms = pd.read_csv(config.master_list,keep_default_na=False)
  # convert multiple spaces to single spaces
  ms = ms.applymap(lambda x: '' if isinstance(x, str) and x.isspace() else x)
  # get only the unrated rows
  unrated = ms.iloc[ms[ms['C2B2_relevant'] == ''].index]
  return unrated

  
def GetRatedProjects(minimum_rating=1):
  '''
  Return a dataframe with rated projects from file config.master_list
  Projects minimum_rating or above are returned
  '''
  ms = pd.read_csv(config.master_list,keep_default_na=False)
  # convert multiple/spaces to zeros
  ms = ms.applymap(lambda x: ' ' if isinstance(x, str) and x.isspace() else x)
  ms['C2B2_relevant'] = pd.to_numeric(ms['C2B2_relevant']).fillna(0) 
  # get only the unrated rows
  rated = ms.iloc[ms[ms['C2B2_relevant'] >= minimum_rating].index]
  return rated
  



def ApiSearch(payload):
  ''' 
  execute a search
  return list of dict with fields 'projectId', 'fundingYear','projectTitleEn'
  '''

  headers = {
      'accept': 'application/json',
      'Authorization': 'Bearer ' + config.API_KEY
  }

  r = requests.get('https://swecris-api.vr.se/v1.0/scp/search', headers=headers, params=payload)
  r.status_code

  searchResult = json.loads(r.text)

  result = searchResult['result']

  # now create a summary that can be used for annotations

  colList = ('projectId', 'fundingYear','projectTitleEn')
  summary  =[{k: r[k] for k in colList} for r in result]
  print('Query: %s ' %payload)
  print('... returned %i records'%len(summary))
  return summary

def SimplifyDate(inDate):
  '''
  Remove months, days, times from dates
  '''

  d = parse(inDate)
  return(d.strftime("%Y"))

  