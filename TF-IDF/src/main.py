import json
from data_loader import load_json_file,clean_projects,get_projects_from_api
from normalizer import tokenize
from tf_idf import calculate_idf,score,tf

json_field = 'projectAbstractEn'
#json_field = 'projectTitleEn'

input_file_path = '../data/all-projects.json'
output_file_path = '../data/top_documents.json'
nr_results = 100
cutoff_year = 2019
api_key = 'VRSwecrisAPI2023-2' #Change this to permanent api_key
api_enabled = False
verbose = True

# ChatGPT keywords prompt for words associated with offshore marine data collection
# operation_type = 'or'
# query = "marine data collection offshore Oceanographers and hydrographers employ various techniques, including seabed mapping, bathymetry, sonar, and seismic surveys, to collect data offshore; they utilize instruments such as CTD profilers, drifting buoys, and underwater vehicles for tasks like current profiling, water sampling, and environmental sensing, while oceanographic research vessels equipped with specialized tools facilitate the collection of meteorological data and the deployment of GIS for spatial analysis, enabling comprehensive analysis and transmission of valuable marine data"

# Summary words for ODF project
# operation_type = 'or'
# query = "Ocean Data Factory Sweden Blue Economy UN decade for ocean sustainable development marine data data lab innovation data from the sea collaboration industry academia authorities invasive species underwater images artificial intelligence ethical legal aspects AI"

# Very specific search on marine data collection where every words has to be in the project abstract
operation_type = 'and'
query = "Marine data collection"

# Keywords extracted from C2B2 project using YAKE(yet another keyword extractor) algorithm. 
# operation_type = 'or'
#query = "sustainable blue economy marine spatial planning ocean governance Marine Sweden blue economy participatory ocean governance Swedish National Data Marine data Data Data Factory Sweden Marine data stewardship ocean Baltic Sea marine research data Swedish governance marine spatial sustainable blue Marine Citizen Science"


if api_enabled:
	projects = json.loads(get_projects_from_api(api_key))
else:
	projects = load_json_file(input_file_path)


#projects_clean = clean_projects(projects["result"])
projects_clean = clean_projects(projects,json_field,cutoff_year)


docs = [element[json_field] for element in projects_clean]
ids = [element['projectId'] for element in projects_clean]

if(verbose):
	print("Tokenizing documents")
docs_tokenized = tokenize(docs,verbose)

if(verbose):
	print("Calculating idf scores")	
idf_values = calculate_idf(docs_tokenized)


scores={}

query = tokenize([query],verbose)
query = query[0]

doc_scores = [(i, score(query, doc, operation_type, docs_tokenized, idf_values)) 
			  	for i, doc in enumerate(docs_tokenized) 
				if score(query, doc, operation_type, docs_tokenized, idf_values) != 0]

doc_scores.sort(key=lambda x: x[1], reverse=True)

if(verbose):
	for i, (index, score) in enumerate(doc_scores[:nr_results], start=1):
	    print(f"RANK {i}: DOCUMENT {ids[index]} - SCORE: {score}")
	    print(docs[index].strip())
	    print("-----------------------------------------------")


top_documents = []

for i, (index, score) in enumerate(doc_scores[:nr_results], start=1):
    projects_clean[index]['score'] = score
    top_documents.append(projects_clean[index])


top_documents_json = json.dumps(top_documents, indent=4)
with open(output_file_path, 'w') as json_file:
    json.dump(top_documents, json_file, indent=4)



