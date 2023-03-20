from django.db import models


class Location(models.Model):
    name = models.TextField(max_length=50)
    lat = models.DecimalField(max_digits=8, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"


class Categories(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


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


class Announcement(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField()
    image = models.ImageField(upload_to='pic/', null=True)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
