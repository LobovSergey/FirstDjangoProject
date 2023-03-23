# Generated by Django 4.1.7 on 2023-03-23 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(choices=[('memder', 'Участник'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='member', max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('location_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
