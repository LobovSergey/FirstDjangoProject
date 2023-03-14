import json


def read_files(data_file):
    try:
        with open(data_file, 'r', encoding='utf-8') as file:
            return json.load(file)

    except FileNotFoundError:
        return f'No data file {data_file}'
