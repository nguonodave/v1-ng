# Generated by Django 4.1.7 on 2023-03-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlacesOfWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'PlaceOfWork',
                'verbose_name_plural': 'PlacesOfWork',
            },
        ),
    ]
