from django.urls import path

from categories.views import CategoriesView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('<int:pk>/', CategoryDetailView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('<int:pk>/update/', CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', CategoryDeleteView.as_view()),
]
