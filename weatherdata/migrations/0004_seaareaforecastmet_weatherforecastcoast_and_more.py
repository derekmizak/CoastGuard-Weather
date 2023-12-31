# Generated by Django 4.2.7 on 2023-11-27 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weatherdata', '0003_sourceurl_description_alter_sourceformat_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeaAreaForecastMet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('until_time', models.CharField(max_length=250)),
                ('issued_time', models.CharField(max_length=250)),
                ('gale_status', models.CharField(max_length=10)),
                ('small_craft_status', models.CharField(max_length=10)),
                ('met_sit_head', models.TextField()),
                ('met_sit_time', models.CharField(max_length=250)),
                ('met_sit_text', models.TextField()),
                ('outlook_time', models.CharField(max_length=250)),
                ('outlook_head', models.TextField()),
                ('outlook_text', models.TextField()),
                ('swell_status', models.CharField(max_length=210)),
            ],
            options={
                'verbose_name_plural': 'sea area forecasts met ie',
            },
        ),
        migrations.CreateModel(
            name='WeatherForecastCoast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=300)),
                ('wind', models.CharField(max_length=300)),
                ('weather', models.TextField()),
                ('visibility', models.CharField(max_length=300)),
                ('sea_area_forecast_met', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weatherdata.seaareaforecastmet')),
            ],
            options={
                'verbose_name_plural': 'weather forecast coasts',
            },
        ),
        migrations.DeleteModel(
            name='SeaAreaForecastMetIe',
        ),
        migrations.DeleteModel(
            name='WeatherRecord',
        ),
    ]
