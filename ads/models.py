from django.db import models


class Announcement(models.Model):
    PUBLISH = [(True, "published"), (False, "not published")]

    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    price = models.PositiveIntegerField(blank=True)
    description = models.TextField(max_length=250, null=True)
    is_published = models.BooleanField(choices=PUBLISH, default=False)
    address = models.CharField(max_length=150)


class Categories(models.Model):
    CATEGORIES = [("Котики", "Котики"),
                  ("Песики", "Песики"),
                  ("Книги", "Книги"),
                  ("Растения", "Растения"),
                  ("Мебель и интерьер", "Мебель и интерьер")]

    name = models.CharField(max_length=20, choices=CATEGORIES)
