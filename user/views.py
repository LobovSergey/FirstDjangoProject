import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from locations.models import Location
from user.models import User


class UserView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        search_data = request.GET.get('first_name', None)
        if search_data:
            self.object_list = self.object_list.filter(first_name=search_data.title())

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)

        data_user = [
            {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'role': user.role,
                'age': user.age,
                'location': [loc.name for loc in user.location.all()]

            } for user in page_object
        ]

        result = {
            "items": data_user,
            "total": paginator.count,
            "num_pages": paginator.num_pages

        }

        return JsonResponse(result, safe=False)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            return JsonResponse(
                {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'role': user.role,
                    'age': user.age,
                    'location': [loc.name for loc in user.location.all()]
                }, status=200)

        except Exception:
            return JsonResponse({"error": "Not found"}, safe=False, status=404)


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'role', 'age', 'location_id']

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        data_location = user_data.pop("location")
        user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
            age=user_data["age"])

        for location in data_location:
            loca, _ = Location.objects.get_or_create(name=location)
            user.location.add(loca)

        return JsonResponse({"status": "created",
                             "id": user.id,
                             "username": user.username,
                             "last_name": user.last_name,
                             "location": [loc.name for loc in user.location.all()]
                             # "total_ads": Count(s)
                             },
                            safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)

        self.object.username = user_data["username"]
        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"]
        self.object.role = user_data["role"]
        self.object.age = user_data["age"]
        self.object.location.all().delete()
        for location in user_data.get('location'):
            loca, _ = Location.objects.get_or_create(name=location)
            self.object.location.add(loca)
        self.object.save()
        return JsonResponse({"status": "edited",
                             "id": self.object.id,
                             "name": self.object.username,
                             "first_name": self.object.first_name,
                             "last_name": self.object.last_name,
                             "role": self.object.role,
                             "age": self.object.age,
                             "locations": [loc.name for loc in self.object.location.all()]},
                            safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse(
            {
                "status": "deleted"
            }
        )
