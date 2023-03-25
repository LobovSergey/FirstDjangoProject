from django.db import models

from categories.models import Categories
from locations.models import Location
from user.models import User


class Announcement(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField(blank=True, null=True)
    image = models.ImageField(upload_to='pic/', blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['price']

    def __str__(self):
        return f'{self.category}/{self.name} - {self.price}'
