# Generated by Django 4.2.7 on 2023-12-03 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherdata', '0007_weatherbuoy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourceurl',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
