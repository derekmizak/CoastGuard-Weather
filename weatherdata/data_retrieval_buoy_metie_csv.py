import requests
import csv
from io import StringIO
from .urlretrieval import get_source_urls
from datetime import datetime


def download_csv(url_to_download):
    try:
        response = requests.get(url_to_download)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")

def process_csv(csv_data):
    try:
        data = []
        csv_reader = csv.DictReader(StringIO(csv_data))
        for row in csv_reader:
            data.append(row)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")


source_url = get_source_urls('csv')[0]


def get_data_from_metie_buoy_in_csv(source_url: str) -> list:
    try:
        csv_data = download_csv(source_url)
        data_list = process_csv(csv_data)
        print(data_list[0])

        def update_dict(data):
            # Move 'name' value to 'stationId'
            data['station_id'] = data.pop('name')
            # Rename 'wmoID' to 'CallSign'
            data['CallSign'] = data.pop('wmoID')
            # Parse the date and time
            dt = datetime.strptime(f"{data['reportDate']} {data['reportTime']}", '%d-%m-%Y %H:%M')
            # Format into the desired format
            formatted_time = dt.strftime('%Y-%m-%dT%H:%M:%SZ')
            # Add the formatted time to the dictionary
            data['time'] = formatted_time
            data.pop('updated_At')
            data['AtmosphericPressure'] = data.pop('pressure')
            data['WindDirection'] = data.pop('windDir')
            data['WindSpeed'] = data.pop('windSpeed')
            data['Gust'] = data.pop('windGust')
            data['WaveHeight'] = data.pop('height')
            data['WavePeriod'] = data.pop('period')
            data['MeanWaveDirection'] = data.pop('waveDir')
            data['AirTemperature'] = data.pop('temp')
            data['DewPoint'] = data.pop('dewPoint')
            data['SeaTemperature'] = data.pop('seaTemp')
            data['RelativeHumidity'] = data.pop('humidity')
            data.pop('reportDate')
            data.pop('reportTime')
            data.pop('ID')
            data.pop('stationId')
            data.pop('windGustDir')
            data.pop('created_at')
            return data

        # Update each dictionary in the list
        updated_data_list = [update_dict(data) for data in data_list]

        # Print the updated list
        print(updated_data_list[0])
        return updated_data_list
    except Exception as e:
        print(f"An error occurred: {e}")
