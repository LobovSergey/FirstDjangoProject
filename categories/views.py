import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from categories.models import Categories


class CategoriesView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_data = request.GET.get('name', None)
        if search_data:
            self.object_list = self.object_list.filter(price=search_data)
        result = [
            {
                'id': category.id,
                'name': category.name
            } for category in self.object_list
        ]
        return JsonResponse(result, safe=False)


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


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreateView(CreateView):
    model = Categories
    fields = ['name']

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)
        announcement = Categories.objects.create(
            name=cat_data["name"]
        )
        return JsonResponse({
            "status": "created",
            "id": announcement.id,
            "name": announcement.name
        }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdateView(UpdateView):
    model = Categories
    fields = ['name']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)
        self.object.name = cat_data["name"]
        self.object.save()
        return JsonResponse({
            "status": "edited",
            "id": self.object.id,
            "name": self.object.name
        }, safe=False)

@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse(
            {
                "status": "deleted"
            }
        )
