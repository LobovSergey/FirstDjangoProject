import csv
import json
import os

NAME_PROJECT = 'ads.'


class Convertation:
    def __init__(self, _csv, _json):
        self.csv_file = _csv
        self.json_file = _json

    def csv_to_json(self):
        try:
            with open(self.csv_file, 'r', encoding='utf-8') as csv_data:
                reader_data = csv.DictReader(csv_data)
                name_file = self._get_filename(self.csv_file)
                data_for_write = self._correct_dict(reader_data, name_file)
                with open(self.json_file, 'w', encoding='utf-8') as json_data:
                    json.dump(data_for_write, json_data, ensure_ascii=False)

        except FileNotFoundError:
            return f'No data file'

    def _correct_dict(self, data, csv_name):
        if csv_name == 'ads':
            return [
                {
                    "model": NAME_PROJECT + "announcement",
                    "pk": int(dictionary["Id"]),
                    "fields":
                        {
                            "name": dictionary["name"],
                            "author": dictionary["author"],
                            "price": int(dictionary["price"]),
                            "description": dictionary["description"],
                            "is_published": self._bool_convertation(dictionary["is_published"]),
                            "address": dictionary["address"]
                        }
                }
                for dictionary in data
            ]
        else:
            return [
                {
                    "model": NAME_PROJECT + "categories",
                    "pk": dictionary["id"],
                    "fields":
                        {
                            "name": dictionary["name"]
                        }
                }
                for dictionary in data
            ]

    def _bool_convertation(self, _string):
        if _string == "TRUE":
            return True
        return False

    def _get_filename(self, file):
        filename = os.path.basename(file).split('.')
        return filename[0]


first_convertation = Convertation(os.path.abspath('ads.csv'), os.path.abspath('ads.json'))
first_convertation.csv_to_json()
second_convertation = Convertation(os.path.abspath('categories.csv'), os.path.abspath('categories.json'))
second_convertation.csv_to_json()
