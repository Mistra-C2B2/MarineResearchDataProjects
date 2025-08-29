import json
import requests
from datetime import datetime

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file '{file_path}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# def clean_projects(projects,json_field):
#     cleaned_project_list = []

#     for _dict in projects:
#         if _dict.get(json_field) is not None and any(char.isalpha() for char in _dict[json_field]):
#             cleaned_project_list.append(_dict)

#     return cleaned_project_list

def clean_projects(projects, json_field,cutoff_year):
    cleaned_project_list = []

    for _dict in projects:
        if (
            _dict.get(json_field) is not None
            and any(char.isalpha() for char in _dict[json_field])
            and 'projectStartDate' in _dict
        ):
            start_date_str = _dict['projectStartDate']
            try:
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                continue

            if start_date.year >= cutoff_year:
                cleaned_project_list.append(_dict)

    return cleaned_project_list


def get_projects_from_api(api_key):
    headers = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    r = requests.get('https://swecris-api.vr.se/v1.0/projects', headers=headers)

    if r.status_code == 200:
        if r.text:
            return r.text
        else:
            raise Exception("Empty response from the API")
    else:
        raise Exception(f"Failed to fetch data from the API. Status code: {r.status_code}")