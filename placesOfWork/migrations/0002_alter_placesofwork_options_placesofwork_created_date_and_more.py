# Generated by Django 4.1.7 on 2023-03-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placesOfWork', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placesofwork',
            options={'ordering': ('created_date',), 'verbose_name': 'PlaceOfWork', 'verbose_name_plural': 'PlacesOfWork'},
        ),
        migrations.AddField(
            model_name='placesofwork',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='placesofwork',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]