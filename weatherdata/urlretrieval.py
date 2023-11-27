import os
import django
import sys

# Set up the Django environment
# Get the directory of the current script
current_script_path = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the current script
parent_directory = os.path.dirname(current_script_path)

# Add the parent directory to sys.path
sys.path.append(parent_directory)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from weatherdata.models import SourceFormat, SourceURL, SeaAreaForecastMet, WeatherForecastCoast


def get_source_urls(format_of_source_urls):
    # Retrieve the SourceFormat instance for 'xml'
    xml_format = SourceFormat.objects.get(name=format_of_source_urls)
    # Retrieve all SourceURL instances that have the 'xml' format
    xml_urls = SourceURL.objects.filter(format=xml_format)
    # Extract the URL strings from the queryset
    url_list = [source_url.url for source_url in xml_urls]

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


