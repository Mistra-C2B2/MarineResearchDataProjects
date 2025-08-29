# -*- coding: utf-8 -*-
# update_master.py - load results from all queries from json, appends any that do not exist in master_list.csv to master_list.csv

import pandas as pd
import os
import config
import json
import shutil

from useful import GetUnratedProjects

# read the master list
ms = pd.read_csv(config.master_list,keep_default_na=False)
knownProjects =  set(ms['projectId']) 

# read the searches

d=list()  # make a list of dict with fields "projectId", "fundingYear", "projectTitleEn"
for path in os.listdir(config.searchers_folder):
    # check if current path is a file
    f = os.path.join(config.searchers_folder, path)
    if os.path.isfile(f):
        print("loading %s..."%f)
        with open(f) as my_file:
          d.extend(json.load(my_file)['result'])

# creat set of all projectIds
allProjects = set([s['projectId'] for s in d])
# get unique set of new projectIds
newProjects = list(allProjects - knownProjects)
# dict with newProjects
nPdict = [next(item for item in d if item['projectId'] == np) for np in newProjects]
colList = ('projectId', 'fundingYear','projectTitleEn')
nPdict  =[{k: r[k] for k in colList} for r in nPdict]
 
# now create a summary that can be used for annotations

df = pd.DataFrame.from_dict(nPdict)
df.insert(2,'C2B2_comment','')
df.insert(2,'C2B2_keywords','')
df.insert(2,'C2B2_relevant','')

df.to_csv('newProjects.csv',index=False)

# make a backaup
bak = config.master_list + '.bak'
shutil.move(config.master_list, bak)

# make a new master
ms2 = pd.concat([ms,df]) 
ms2.to_csv(config.master_list,index=False)

