# MarineResearchDataProjects

The C2B2-relevant list of research projects
-------------------------------------------

### Background

This project list has been compiled as part of Mistra Co-Creating Better Blue ([C2B2](c2b2.se)), Task 2.5 Marine data stewardship – FAIR & Open data management and integration into existing aggregators. C2B2 envisions a more sustainable, open and democratic, multi-sector and multi-actor blue economy and sustainable society. The generation of new data sources about the ocean and their combination with existing data is accelerating the need to coordinate, integrate and soundly manage such data using the FAIR data principles. Yet many research institutions and/or groups collecting marine data are too small to afford a Data Steward. All Swedish universities can obtain advice on data management from [SND](snd.se), but subject- specific support to ensure the availability of marine data is not yet available and there is no direct support yet with file management, which in many cases is needed to maximize data utilization. Data stewardship is also recognized by SIME as critical for effective environmental monitoring (Emmerson et al., 2018). This task will keep track of and provide direct support to C2B2 and other projects that collect marine research data. This will ensure that new data streams will be integrated into major existing data environments (such as [Copernicus](https://www.copernicus.eu/en)) in order to maximize their uptake and utilisation. C2B2 till be available to help them with their data management plan, and during the project lifetime to help them publish their data using the FAIR data principles.

### The C2B2-relevant list of research projects

Information about marine research projects has been sourced from the Swecris national research project database for participating research funding bodies that have distributed their funds to researchers in Sweden. The database contains data from both governmental and private research funding bodies. 

Information was obtained from the Swecris public API https://swecris-api.vr.se/index.html. Project selection was restricted to 2019 onwards. 

The final list of selected research projects is contained in FrontEnd/top_documents.json. 

### Folder structure

Each Folder contains it's own README.md with more information.

- **FrontEnd** - The final list of selected research projects, as well as a html/css/js viewer. The top_documents.json file is a combination of projects selected by the TF-IDF algorithm and the ManualSearch process. 
- **TF-IDF** -  a *term frequency-inverse document frequency* based code set to select relevant documents. Was used to create the first list of projects for review.
- **ManualSearch** - code for creating the project catalog using manually-specified searches. Most of the searches used are listed in payload.py. The search/preview/rate procedure was to eliminate having to re-rate the same projects many times if they were selected by multiple searches. 

Initial project selection was a combination of text-based and subject-based searches, followed by subjective assessment of the relevance of the project for C2B2. Interesting projects were selected manually as those that appear to be collecting data or developing models that could be of use to C2B2 Living Labs (LLs). This is a much smaller set of projects than those for which the project results (eg books, reports) could be of interest. 

The objective of this activity is to identify research projects which may be collecting relevant data, but where there is a risk that the data does not become accessible. Projects that might be relevant to LL particular actors but which lacked a clear geographic connection to the LLs (eg research on marine propulsion or wind turbines) were not selected. 

A list of all projects selected by the search algorithms, and then manually evaluated is provided in the [master\_list.csv](master_list.csv) file on Github. All codes used in the list selection are provided on the Github MarineResearchDataProjects repository: https://github.com/Mistra-C2B2/MarineResearchDataProjects

### Environment

The included python [environment.yml](environment.yml) is sufficient for FrontEnd and ManualSearch.

### Questions

For more information about the C2B2-relevant list of research projects, please contact [David Rayner](mailto: David.Rayner@gu.se), Swedish National Data service.

## Authors and acknowledgment
This project was developed by the C2B2 WP2 team. Primary contributors were [David Rayner](mailto: David.Rayner@gu.se), Swedish National Data service and Iman Shahmari (Chalmers).
Profile icon supplied by [www.flaticon.com](https://www.flaticon.com/free-icons/catalogue).

Mistra Co-Creating Better Blue (C2B2) is supported by Mistra, The Swedish foundation for strategic environmental research.

## License
MIT

