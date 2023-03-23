from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from ads.views import AnnouncementDetailView, AnnouncementView, AnnouncementCreateView, AnnouncementUpdateView, \
    AnnouncementDeleteView, AnnouncementUploadImageView

urlpatterns = [
                  path('', AnnouncementView.as_view()),
                  path('<int:pk>/', AnnouncementDetailView.as_view()),
                  path('<int:pk>/update/', AnnouncementUpdateView.as_view()),
                  path('<int:pk>/delete/', AnnouncementDeleteView.as_view()),
                  path('create/', AnnouncementCreateView.as_view()),
                  path('<int:pk>/upload_image/', AnnouncementUploadImageView.as_view()),
              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
