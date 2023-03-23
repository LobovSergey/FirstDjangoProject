from django.db import models

from locations.models import Location


class User(models.Model):
    ROLES = [('memder', 'Участник'),
             ('moderator', 'Модератор'),
             ('admin', 'Администратор')]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    role = models.CharField(max_length=30, choices=ROLES, default='member')
    age = models.PositiveIntegerField()
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
