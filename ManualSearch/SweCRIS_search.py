import requests
import json
import os
import pandas as pd

# local config, tex passwords
import config
import useful

def SweCrisSingleSearch(search_id, payload):
# the interface is described at https://swecris-api.vr.se/index.html
    allProjects  = list()  # to get the final list of projects from
    foundProjects=set()
    for p in payload:
      searchList = useful.ApiSearch(p)  # this as list
      if (len(searchList)==0):
        continue

      allProjects.extend(searchList)   # all as list

      df = pd.DataFrame.from_dict(searchList)
      searchedProjects =  set(df['projectId']) 
      
      if (len(foundProjects)==0):
        foundProjects=searchedProjects
      else:
        foundProjects=foundProjects.intersection(searchedProjects)


    print('... combining to %i unqiue projects...'%(len(foundProjects)))


    # report how many new
    ms = pd.read_csv(config.master_list,keep_default_na=False)
    knownProjects =  set(ms['projectId']) 

    newProjects = list(foundProjects - knownProjects)

    summary = [next(item for item in allProjects if item['projectId'] == np) for np in newProjects]


    print('... of which %i are new projects (ie do not exist in %s'%(len(summary),config.master_list))

    try:
        os.makedirs(config.searchers_folder)
        print("Created folder " + config.searchers_folder)
    except:
        pass

    filename=os.path.join(config.searchers_folder,search_id+'.json')
    print('... output to: '+filename)

    summary = {'query':payload,'result':summary}
    with open(filename, 'w') as fp:
        json.dump(summary, fp)

with open(config.payload, 'r') as file:
    searchList = json.load(file)
    
for search in searchList:
    print("Search_id: " + search["search_id"])
    SweCrisSingleSearch(search["search_id"], search["payload"])
