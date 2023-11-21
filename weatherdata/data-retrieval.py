import xml.etree.ElementTree as ET
import requests

url = 'https://www.met.ie/Open_Data/xml/Met-Sea-area.xml'

import xml.etree.ElementTree as ET

def xml_to_custom_dictionary(xml_data):
    root = ET.fromstring(xml_data)

    # Initialize the dictionary with predefined keys
    data = {
        'title': '',
        'until-time': '',
        'issued-time': '',
        'gale-status': '',
        'small-craft-status': '',
        'met-sit-head': '',
        'met-sit-time': '',
        'met-sit-text': '',
        'outlook-time': '',
        'outlook-head': '',
        'outlook-text': '',
        'swell-status': ''
    }

    # Function to handle specific elements
    def handle_element(elem):
        if elem.tag == 'title':
            data['title'] = elem.text.strip() if elem.text else ''
        elif elem.tag in ['until', 'issued']:
            data[f"{elem.tag}-time"] = elem.attrib.get('issued-time') if elem.tag == 'issued' else elem.attrib.get('until-time')
        elif elem.tag in ['gale', 'small-craft', 'Swell']:
            data[f"{elem.tag}-status"] = elem.attrib.get('status', '')
        elif elem.tag == 'met-sit':
            data['met-sit-time'] = elem.attrib.get('time', '')
            for child in elem:
                if child.tag in ['head', 'text']:
                    data[f"met-sit-{child.tag}"] = child.text.strip() if child.text else ''
        elif elem.tag == 'outlook':
            data['outlook-time'] = elem.attrib.get('outlook-time', '')
            for child in elem:
                if child.tag in ['head', 'text']:
                    data[f"outlook-{child.tag}"] = child.text.strip() if child.text else ''
        elif elem.tag == 'coast':
            handle_coast(elem)

    # Function to handle coast elements
    def handle_coast(coast_elem):
        coast_count = 1
        while f"area{coast_count}" in data:
            coast_count += 1
        for child in coast_elem:
            data[f"{child.tag}{coast_count}"] = child.text.strip() if child.text else ''

    # Process each element
    for child in root:
        handle_element(child)

    return data



def fetch_xml_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.

        # Assuming the response content is XML
        return response.text
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


weather_data = xml_to_custom_dictionary(fetch_xml_from_url(url))
print(weather_data)