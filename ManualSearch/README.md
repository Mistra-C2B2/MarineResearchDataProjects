# README.md

This is the code for creating the project catalog using manual search. Just some notes!! 

Note that this code cannot be simply re-run to re-create the final output! It was run iteratively, with manual editing of master_list.csv, and code development along the way!

## preview the results
 - Previewer.html - javascript to read the output.json and preview in web browser.
 - arrow_down.png, arrow-right-01-512.png - just files used in outputPreviewer.html for the collapsibles. 
 - config_RENAME.py - config file, rename to config.py with your own folders etc.
 - Count_Keywords.py - utility program to list key-word counts. Useful for avoiding related terms.

## Current procedure:
 - SweCRIS_search.py - base query function simply return list of returned projectIDs  and saves as json files. The query and a search_id tag are specified in the payload.json. The output json files are saved to location specified in config.searchers_folder (currently "Searches"). Gives a summary of how many new projects were found to command line.

- master_list.csv of projectIDs/titles and manual ratings as csv. Actually, file name is specified in config.master_list. The fields in master_list.csv are:
    - projectId - Swecris projectID
    - fundingYear - Swecris fundingYear
    - C2B2_relevant - qualitative rating of C2B2 relevance, 0=low 5=high.
    - C2B2_keywords - a list of keywords that characterized the project and contributed to the rating. 
    - C2B2_comment - notes particularly about uncertainties in what the project would do.
    - projectTitleEn - Swecris title of the project in English, for reference.

- update_master.py - load results from all queries from json files in Searches, appends any that do not exist in master_list.csv to master_list.csv. Duplicate new projects (those found in multiple searchers) are only added once.

- prepare_preview.py - review function - download data for the projects in master_list.csv that are unrated,  so can be reviewed in html. Writes output.json

- Previewer.html - reads output.json and displays a summary, so you can add a rating in master_list.csv. Note that you don't view Preview.html directly, you view it in a web server (see below)

- create_final.html - make a dataset with all info for the projects in the final dataset (ie C2B2_relevant >=3). Outputs to top_documents.json! 

- top_documents.json needs to be copied manually to ../FrontEnd/

## What criteria were used? Some thoughts...

fishing;  aquaculture, seaweed farming "tång"; offshore wind, maritime transport, sea bed minerals, recreational fisheries = +

* note fishing used for eg trawling, curstaceans...

Land-based aquaculture = 0; Inshore "coast" = +, Offshore "ocean" =++

Scandinavian| Nordic = +

"blue economy" = +

"sustainable blue economy" = +

"hållbar livsmedel" but only in combination with other marine = +

"multiple sectors" eg tångodlare och sillprocessföretag = +

Qualitative: interested in projects that appear to be collecting *data* that could be of use to C2B2 LLs, which is a much smaller set of projects than those for which the project results could be of interest.  

### How to make a preview of a query:

Run a [local web server](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Tools_and_setup/set_up_a_local_testing_server). I used 
```sh
python3 -m http.server
```
in Windows Subsystem for Linux.
Then just load the file as localhost:8000/Previewer.html



