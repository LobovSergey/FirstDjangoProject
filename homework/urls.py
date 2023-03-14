
from django.contrib import admin
from django.urls import path
from ads.views import ADSView, DataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ADSView.as_view()),
    path('db/', DataView.as_view()),
]
