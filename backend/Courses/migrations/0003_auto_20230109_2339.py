# Generated by Django 2.2.28 on 2023-01-09 23:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_auto_20210206_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='likes',
            field=models.ManyToManyField(related_name='likes_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]