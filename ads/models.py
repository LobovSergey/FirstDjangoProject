from django.db import models


class Announcement(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    price = models.PositiveIntegerField(blank=True)
    description = models.CharField(max_length=250)
    is_published = models.BooleanField()
    address = models.CharField(max_length=150)


class Categories(models.Model):
    CATEGORIES = [("Котики", "Котики"),
                  ("Песики", "Песики"),
                  ("Книги", "Книги"),
                  ("Растения", "Растения"),
                  ("Мебель и интерьер", "Мебель и интерьер")]

    name = models.CharField(max_length=20, choices=CATEGORIES)


