from django.contrib import admin
from django.urls import path, include

from ads.views import ADSView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ADSView.as_view()),
    path('ad/', include('ads.urls')),
    path('cat/', include('categories.urls')),

]
