# Generated by Django 4.1.7 on 2023-03-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_alter_location_name'),
        ('user', '0002_alter_user_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location_id',
        ),
        migrations.AddField(
            model_name='user',
            name='location_id',
            field=models.ManyToManyField(to='locations.location'),
        ),
    ]
