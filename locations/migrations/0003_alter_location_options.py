# Generated by Django 4.1.7 on 2023-03-25 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_alter_location_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Местоположение', 'verbose_name_plural': 'Местоположения'},
        ),
    ]
