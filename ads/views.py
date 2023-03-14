import os

from django.http import JsonResponse, HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from datasets.stretch_data import read_files

from ads.models import Announcement, Categories

ADS_FILE = os.path.abspath('../datasets/ads.csv')
CATEGORIES_FILE = os.path.abspath('../datasets/categories.csv')


class ADSView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


class DataView(View):
    def get(self, request):
        announcement_object = Announcement()
        category_object = Categories()
        announcement_data = read_files(ADS_FILE)
        category_data = read_files(CATEGORIES_FILE)
        for announcement in announcement_data:
            announcement_object.name = announcement["name"]
            announcement_object.author = announcement['author']
            announcement_object.price = announcement['price']
            announcement_object.is_published = announcement['is_published']
            announcement_object.address = announcement['address']
            announcement_object.save()
        for category in category_data:
            category_object.name = category['name']
            category_object.save()
        return HttpResponse('Data added')
