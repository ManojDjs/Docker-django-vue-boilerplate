# Generated by Django 2.2.28 on 2023-01-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aggregator', '0002_auto_20230109_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmonials',
            name='image',
            field=models.ImageField(blank=True, default='Course.png', null=True, upload_to='profile_pics'),
        ),
    ]