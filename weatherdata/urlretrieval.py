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

from weatherdata.models import SourceFormat, SourceURL, SeaAreaForecastMet, WeatherForecastCoast, MetOceanBuoyData


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

MetOceanBuoyData

def update_metocean_buoy_data(metocean_buoy_data, metocean_buoy_obj
    metocean_buoy_obj = MetOceanBuoyData.objects.create(
        EightHourlyID=metocean_buoy_data['EightHourlyID'],
        MMSI=metocean_buoy_data['MMSI'],
        AverageWindSpeed=metocean_buoy_data['AverageWindSpeed'],
        GustSpeed=metocean_buoy_data['GustSpeed'],
        WindDirection=metocean_buoy_data['WindDirection'],
        WindGustDirection=metocean_buoy_data['WindGustDirection'],
        AirTemperature=metocean_buoy_data['AirTemperature'],
        RelativeHumidity=metocean_buoy_data['RelativeHumidity'],
        DewPoint=metocean_buoy_data['DewPoint'],
        AirPressure=metocean_buoy_data['AirPressure'],
        PressureTendency=metocean_buoy_data['PressureTendency'],
        HorizVisibility=metocean_buoy_data['HorizVisibility'],
        WaterLevel=metocean_buoy_data['WaterLevel'],
        WaterLevelTrend=metocean_buoy_data['WaterLevelTrend'],
        SurfaceCurrentSpeed=metocean_buoy_data['SurfaceCurrentSpeed'],
        SurfaceCurrentDirection=metocean_buoy_data['SurfaceCurrentDirection'],
        CurrentSpeed2=metocean_buoy_data['CurrentSpeed2'],
        CurrentDirection2=metocean_buoy_data['CurrentDirection2'],
        MeasurementDepth2=metocean_buoy_data['MeasurementDepth2'],
        CurrentSpeed3=metocean_buoy_data['CurrentSpeed3'],
        CurrentDirection3=metocean_buoy_data['CurrentDirection3'],
        MeasurementDepth3=metocean_buoy_data['MeasurementDepth3'],
        WaveHeight=metocean_buoy_data['WaveHeight'],
        WavePeriod=metocean_buoy_data['WavePeriod'],
        WaveDirection=metocean_buoy_data['WaveDirection'],
        SwellHeight=metocean_buoy_data['SwellHeight'],
        SwellPeriod = metocean_buoy_data['SwellPeriod'],
        SwellDirection = metocean_buoy_data['SwellDirection'],
        SeaState = metocean_buoy_data['SeaState'],
        WaterTemperature = metocean_buoy_data['WaterTemperature'],
        Precipitation = metocean_buoy_data['Precipitation'],
        Salinity = metocean_buoy_data['Salinity'],
        Ice = metocean_buoy_data['Ice'],
        DateTransmitted = metocean_buoy_data['DateTransmitted']
    )

