# Generated by Django 4.1.7 on 2023-03-27 19:59

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('placesOfWork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50, unique=True)),
                ('tasks', ckeditor_uploader.fields.RichTextUploadingField(max_length=200, null=True)),
                ('period', models.TextField(max_length=20, null=True)),
                ('place_of_Work', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='placesOfWork.placesofwork')),
            ],
            options={
                'verbose_name': 'WorkExperience',
                'verbose_name_plural': 'WorkExperiences',
            },
        ),
    ]