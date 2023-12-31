# Generated by Django 4.2.8 on 2023-12-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherdata', '0011_rename_gustspeed_metiebuoydata_gust'),
    ]

    operations = [
        migrations.AddField(
            model_name='seaareaforecastmet',
            name='swell_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='gale_status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='issued_time',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='met_sit_head',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='met_sit_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='outlook_head',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='outlook_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='outlook_time',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='small_craft_status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='swell_status',
            field=models.CharField(blank=True, max_length=210, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='seaareaforecastmet',
            name='until_time',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
