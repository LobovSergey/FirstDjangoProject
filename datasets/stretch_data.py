import csv
import json
import os

NAME_PROJECT = {
    "ad": "ads.",
    "category": "categories.",
    "location": "locations.",
    "user": "user."
}
AD_CSV = os.path.abspath('ad.csv')
AD_JSON = os.path.abspath('ad.json')
CATEGORY_CSV = os.path.abspath('category.csv')
CATEGORY_JSON = os.path.abspath('category.json')
LOCATION_CSV = os.path.abspath('location.csv')
LOCATION_JSON = os.path.abspath('location.json')
USER_CSV = os.path.abspath('user.csv')
USER_JSON = os.path.abspath('user.json')
FILES_FOR_CONVERTATION = [(AD_CSV, AD_JSON), (CATEGORY_CSV, CATEGORY_JSON), (LOCATION_CSV, LOCATION_JSON),
                          (USER_CSV, USER_JSON)]


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
        if csv_name == 'ad':
            return [
                {
                    "model": NAME_PROJECT[csv_name] + "announcement",
                    "pk": int(dictionary["Id"]),
                    "fields":
                        {
                            "name": dictionary["name"],
                            "author_id": dictionary["author_id"],
                            "price": int(dictionary["price"]),
                            "description": dictionary["description"],
                            "is_published": self._bool_convertation(dictionary["is_published"]),
                            "image": dictionary["image"],
                            "category_id": dictionary["category_id"]

                        }
                }
                for dictionary in data
            ]
        elif csv_name == 'category':
            return [
                {
                    "model": NAME_PROJECT[csv_name] + "categories",
                    "pk": dictionary["id"],
                    "fields":
                        {
                            "name": dictionary["name"]
                        }
                }
                for dictionary in data
            ]
        elif csv_name == 'location':
            return [
                {
                    "model": NAME_PROJECT[csv_name] + "location",
                    "pk": dictionary["id"],
                    "fields":
                        {
                            "name": dictionary["name"],
                            "lat": dictionary["lat"],
                            "lng": dictionary["lng"]
                        }
                }
                for dictionary in data
            ]
        else:
            return [
                {
                    "model": NAME_PROJECT[csv_name] + "user",
                    "pk": dictionary["id"],
                    "fields":
                        {
                            "first_name": dictionary["first_name"],
                            "last_name": dictionary["last_name"],
                            "username": dictionary["username"],
                            "password": dictionary["password"],
                            "role": dictionary["role"],
                            "age": dictionary["age"],
                            "location": [dictionary["location_id"]]
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


for pair in FILES_FOR_CONVERTATION:
    convertation = Convertation(pair[0], pair[1])
    convertation.csv_to_json()
