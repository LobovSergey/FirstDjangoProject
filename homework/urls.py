from django.contrib import admin
from django.urls import path
from ads.views import ADSView, AnnouncementView, CategoriesView, CategoryDetailView, AnnouncementDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ADSView.as_view()),
    path('ad/', AnnouncementView.as_view()),
    path('cat/', CategoriesView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('ad/<int:pk>/', AnnouncementDetailView.as_view()),

]
