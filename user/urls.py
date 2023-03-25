from django.urls import path


from user.views import UserView, UserCreateView, UserDeleteView, UserUpdateView, UserDetailView

urlpatterns = [
    path('', UserView.as_view()),
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('create/', UserCreateView.as_view())

]
