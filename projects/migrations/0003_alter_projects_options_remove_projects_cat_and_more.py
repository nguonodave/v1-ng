# Generated by Django 4.1.7 on 2023-03-29 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projects_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.RemoveField(
            model_name='projects',
            name='cat',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='category',
        ),
    ]