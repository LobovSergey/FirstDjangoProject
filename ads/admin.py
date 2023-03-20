from django.contrib import admin

from ads.models import User, Location, Categories, Announcement

admin.site.register(User)
admin.site.register(Location)
admin.site.register(Categories)
admin.site.register(Announcement)
