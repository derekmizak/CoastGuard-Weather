#TODO: URGENT - entire met.ie buoy data retrieval needs to be re-written to use correct model fields

from datetime import datetime, timedelta
import urllib.parse, requests, json




def create_url_for_metie_buoy_data(url):
    # Calculate the current time minus 60 minutes
    time_threshold = datetime.utcnow() - timedelta(minutes=360)

    # Format the time in the required format (ISO 8601 format)
    formatted_time = time_threshold.strftime('%Y-%m-%dT%H:%M:%SZ')
    #print(formatted_time)
    # Base URL without the time parameter
    base_url = url
    final_url = base_url + urllib.parse.quote(formatted_time)

    return final_url


def get_data_from_metie_buoy(url):
    final_url = create_url_for_metie_buoy_data(url)
    response = requests.get(final_url)
    if response.status_code == 200:
        json_file = response.json()
        column_names = json_file["table"]["columnNames"]
        rows = json_file["table"]["rows"]

        #print(column_names)
        # Convert rows to list of dictionaries
        list_of_dicts = [dict(zip(column_names, row)) for row in rows]
        return list_of_dicts
    else:
        return None