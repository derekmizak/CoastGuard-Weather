import os
import django
import sys
from django.utils import timezone
from datetime import datetime

# Set up the Django environment
# Get the directory of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current script
parent_directory = os.path.dirname(current_script_path)

# Add the parent directory to sys.path
sys.path.append(parent_directory)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from weatherdata.models import (SourceFormat, SourceURL, SeaAreaForecastMet, WeatherForecastCoast,
                                MetOceanBuoyData, MetIeBuoyData)


def get_source_urls(format_of_source_urls):
    # Retrieve the SourceFormat instance of given format - 'xml' or 'html' or 'csv' etc.
    data_format = SourceFormat.objects.get(name=format_of_source_urls)
    # Retrieve all SourceURL instances that have the 'xml' format
    source_data_urls = SourceURL.objects.filter(format=data_format)
    # Extract the URL strings from the queryset
    url_list = [source_url.url for source_url in source_data_urls]

    return url_list


def update_forecast_met(forecast_data):
    forecast_obj, created = SeaAreaForecastMet.objects.get_or_create(
        until_time=forecast_data['until_time'],
        issued_time=forecast_data['issued_time'],
        defaults=forecast_data
    )
    print(forecast_obj.id, forecast_obj.title)
    return forecast_obj, created


def update_coastal_areas(coastal_areas_data, obj):
    coast_obj = WeatherForecastCoast.objects.create(
        area=coastal_areas_data['area'],
        wind=coastal_areas_data['wind'],
        weather=coastal_areas_data['weather'],
        visibility=coastal_areas_data['visibility'],
        sea_area_forecast_met=obj
    )
    print(coast_obj.id, coast_obj.area)
    return coast_obj


def update_metocean_buoy_data(metocean_buoy_data):
    # Ensure MMSI, EightHourlyID, and DateTransmitted contain data and are not null or empty
    required_fields = ['MMSI', 'EightHourlyID', 'DateTransmitted']
    if not all(metocean_buoy_data.get(field) for field in required_fields):
        print("Required fields are missing data.")
        return None, False

    # Convert empty strings to None for all fields
    for key, value in metocean_buoy_data.items():
        if value == '':
            metocean_buoy_data[key] = None

    # Handle datetime field
    date_str = metocean_buoy_data['DateTransmitted']
    naive_datetime = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
    aware_datetime = timezone.make_aware(naive_datetime, timezone.get_default_timezone())
    metocean_buoy_data['DateTransmitted'] = aware_datetime

    # Create or update the MetOceanBuoyData object
    metocean_buoy_obj, created = MetOceanBuoyData.objects.get_or_create(
        DateTransmitted=metocean_buoy_data['DateTransmitted'],
        MMSI=metocean_buoy_data['MMSI'],
        EightHourlyID=metocean_buoy_data['EightHourlyID'],
        defaults=metocean_buoy_data
    )

    if created:
        print(metocean_buoy_obj.id, metocean_buoy_obj.MMSI)

    return metocean_buoy_obj, created


def update_metie_buoy_data(metie_buoy_data):
    # Ensure station_id, CallSign, and time contain data and are not null or empty
    required_fields = ['station_id', 'CallSign', 'time']
    if not all(metie_buoy_data.get(field) for field in required_fields):
        print("Required fields are missing data.")
        return None, False

    # Convert empty strings to None for all fields
    for key, value in metie_buoy_data.items():
        if value == '':
            metie_buoy_data[key] = None

    # Handle datetime field
    date_str = metie_buoy_data['time']
    naive_datetime = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    aware_datetime = timezone.make_aware(naive_datetime, timezone.get_default_timezone())
    metie_buoy_data['time'] = aware_datetime

    # Create or update the MetIeBuoyData object
    metie_buoy_obj, created = MetIeBuoyData.objects.get_or_create(
        time=metie_buoy_data['time'],
        station_id=metie_buoy_data['station_id'],
        CallSign=metie_buoy_data['CallSign'],
        defaults=metie_buoy_data
    )

    if created:
        print(metie_buoy_obj.id, metie_buoy_obj.station_id)

    return metie_buoy_obj, created