# Generated by Django 4.2.7 on 2023-11-30 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherdata', '0005_metoceanbuoydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='AirPressure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='AirTemperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='AverageWindSpeed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='CurrentDirection2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='CurrentDirection3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='CurrentSpeed2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='CurrentSpeed3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='DewPoint',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='GustSpeed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='HorizVisibility',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='Ice',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='MeasurementDepth2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='MeasurementDepth3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='Precipitation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='PressureTendency',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='RelativeHumidity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='Salinity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='SeaState',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='SurfaceCurrentDirection',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='SurfaceCurrentSpeed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='SwellDirection',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='SwellHeight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='SwellPeriod',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='WaterLevel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='WaterLevelTrend',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='WaterTemperature',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='WaveDirection',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='WaveHeight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='WavePeriod',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='WindDirection',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metoceanbuoydata',
            name='WindGustDirection',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]