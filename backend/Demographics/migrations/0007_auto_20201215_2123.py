# Generated by Django 3.1.3 on 2020-12-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demographics', '0006_auto_20201215_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographic_questions',
            name='question_field',
            field=models.CharField(choices=[('Optional', 'Optional'), ('Mandatory', 'Mandatory')], default='Mandatory', max_length=10),
        ),
        migrations.AlterField(
            model_name='demographic_questions',
            name='question_type',
            field=models.CharField(choices=[('Gender', 'Gender'), ('Number', 'Number'), ('YESNO', 'YES/NO'), ('TEXT', 'TEXT')], default='TEXT', max_length=10),
        ),
    ]