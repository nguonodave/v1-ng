# Generated by Django 4.1.7 on 2023-05-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workExperience', '0004_workexperience_place_of_work_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='job_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='place_of_Work_link',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
