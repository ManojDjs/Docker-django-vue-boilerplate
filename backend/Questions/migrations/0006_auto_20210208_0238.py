# Generated by Django 3.1.3 on 2021-02-08 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0005_auto_20210208_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intial_baseline_answer',
            name='Course_initial',
        ),
        migrations.AlterField(
            model_name='intial_baseline_answer',
            name='Initial_question_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Initial_question', to='Questions.questions'),
        ),
    ]
