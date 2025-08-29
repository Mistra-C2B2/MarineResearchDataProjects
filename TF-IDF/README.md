# TF-IDF(C2B2)

## Overview

This project focuses on extracting and ranking research projects based on their relevance to a given query. The primary components include:

- main.py: The main script that orchestrates the data loading, processing, and ranking of documents.
- data_loader.py: Module for loading and cleaning project data.
- tfidf.py: Module containing functions for calculating TF-IDF scores.
- normalizer.py: Module for normalizing and tokenizing text data.

## Usage

### Requirements

Make sure you have the required dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```

### Configuration
Adjust the configuration parameters in main.py to suit your needs:

- json_field: The JSON field to be considered for analysis (e.g., 'projectTitleEn' or 'projectAbstractEn').
- input_file_path: Path to the input JSON file containing all project data.
- output_file_path: Path to the output JSON file where the file will be stored.
- nr_results: Number of top ranked documents to retrieve.
- cutoff_year: The year from which projects should be considered.
- api_key: Your API key for accessing project data (change to a permanent key if applicable).
- api_enabled: Set to True if using an API to fetch project data.
- verbose: Set to True for verbose output during processing.
- operation type: which can be set 'and' or 'or'. 'and' operation makes sure the whole query is a subset of the document. 'or' is less constrained and documents can be scored even though all tokens of the query may not be present in the docuemnt.  
### Execution

Run the main script:

```bash
python3 main.py
```

## Modules

### data_loader.py

- load_json_file(file_path: str) -> dict: Load project data from a JSON file.
- clean_projects(projects: dict, json_field: str, cutoff_year: int) -> list: Clean and filter projects based on the specified JSON field and cutoff year.
- get_projects_from_api(api_key: str) -> str: Fetch project data from an API using the provided API key.

### tfidf.py

- calculate_idf(all_documents: list) -> dict: Calculate the Inverse Document Frequency (IDF) values for terms in the corpus.
- score(query: list, document: list, operation_type: str, all_documents: list, idf_values: dict) -> float: Calculate the TF-IDF score for a document given a query.
- tf(token: str, document: list) -> float: Calculate the Term Frequency (TF) for a token in a document.

### normalizer.py

- tokenize(all_text: list, verbose: bool) -> list: Tokenize and normalize text data, removing stopwords, punctuation, and stemming.

## Examples

Adjust the example queries in main.py based on your specific requirements. Run the script to see the ranked documents based on these queries.

## Future Development

Consider the following ideas for future development:

1. **Weighted Tokens in TF-IDF:** Allow users to assign weights to tokens used in TF-IDF calculations to obtain more accurate search results.

2. **Contextual Token Analysis:** Include the notion that some tokens together may hold more significance than individual token analysis, improving contextual understanding.

3. **Network Analysis:** Consider that researchers in a specific field may be connected in a network, influencing the relevance of a project. Explore network-based approaches for better contextualization.

Check out the [docs folder](docs/) where papers regarding these ideas are included.

## License

This project is licensed under the [MIT] - see the [LICENSE.md](LICENSE.md) file for details.
