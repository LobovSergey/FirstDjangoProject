import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Announcement, Categories


class ADSView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AnnouncementView(View):
    def get(self, request):
        result = Announcement.objects.all()
        response = [
            {
                "id": dictionary.id,
                "name": dictionary.name,
                "author": dictionary.author,
                "price": dictionary.price,
                "description": dictionary.description,
                "is_published": dictionary.is_published,
                "address": dictionary.address
            }
            for dictionary in result
        ]
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        data_result = json.loads(request.body)
        announcement = Announcement()
        announcement.name = data_result["name"]
        announcement.author = data_result["author"]
        announcement.price = data_result["price"]
        announcement.description = data_result["description"]
        announcement.is_published = data_result["is_published"]
        announcement.address = data_result["address"]
        announcement.save()
        return JsonResponse(data_result, safe=False, status=200)


class AnnouncementDetailView(DetailView):
    model = Announcement

    def get(self, request, *args, **kwargs):
        try:
            announcement = self.get_object()
            return JsonResponse(
                {
                    "id": announcement.id,
                    "name": announcement.name,
                    "author": announcement.author,
                    "price": announcement.price,
                    "description": announcement.description,
                    "is_published": announcement.is_published,
                    "address": announcement.address
                }, status=200)
        except Exception:
            return JsonResponse({"error": "Not found"}, status=404)


@method_decorator(csrf_exempt, name="dispatch")
class CategoriesView(View):
    def get(self, request):
        result = Categories.objects.all()
        response = [
            {
                "id": dictionary.id,
                "name": dictionary.name,
            }
            for dictionary in result
        ]
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        data_result = json.loads(request.body)
        announcement = Categories()
        announcement.name = data_result["name"]
        announcement.save()
        return JsonResponse(data_result, safe=False, status=200)


class CategoryDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
            return JsonResponse(
                {
                    "id": category.id,
                    "name": category.name,
                }, status=200)
        except Exception:
            return JsonResponse({"error": "Not found"}, status=404)
