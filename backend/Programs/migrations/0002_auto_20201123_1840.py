# Generated by Django 3.1.3 on 2020-11-23 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initial_isq',
            name='Answered_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, to_field='username', unique=True),
        ),
    ]