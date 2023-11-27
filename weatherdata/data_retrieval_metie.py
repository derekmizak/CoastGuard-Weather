import xml.etree.ElementTree as ET
import requests

# TODO: Extract the URL from the database
url = 'https://www.met.ie/Open_Data/xml/Met-Sea-area.xml'


def fetch_xml_from_url(url):
    """
    Fetch XML data from a given URL.

    Args:
        url (str): The URL to fetch the XML data from.

    Returns:
        str: The fetched XML data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code.

        # Assuming the response content is XML
        return response.text
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def xml_to_custom_dictionary(xml_data):
    """
    Convert XML data to a custom dictionary format.

    Args:
        xml_data (str): The XML data to be converted.

    Returns:
        dict: The converted dictionary containing the extracted data.
    """
    root = ET.fromstring(xml_data)

    # Initialize the dictionary with predefined keys
    data = {
        'title': '',
        'until_time': '',
        'issued_time': '',
        'gale_status': '',
        'small_craft_status': '',
        'met_sit_head': '',
        'met_sit_time': '',
        'met_sit_text': '',
        'outlook_time': '',
        'outlook_head': '',
        'outlook_text': '',
        'swell_status': ''
    }

    # Function to handle specific elements
    def handle_element(elem):
        if elem.tag == 'title':
            data['title'] = elem.text.strip() if elem.text else ''
        elif elem.tag == 'issued':
            data['issued_time'] = elem.attrib.get('issued-time', '')
        elif elem.tag == 'until':
            data['until_time'] = elem.attrib.get('until-time', '')
        elif elem.tag == 'gale':
            data['gale_status'] = elem.attrib.get('status', '')
        elif elem.tag == 'small-craft':
            data['small_craft_status'] = elem.attrib.get('status', '')
        elif elem.tag == 'Swell':
            data['swell_status'] = elem.attrib.get('status', '')
        elif elem.tag == 'met-sit':
            data['met_sit_time'] = elem.attrib.get('time', '')
            for child in elem:
                if child.tag in ['head', 'text']:
                    data[f"met_sit_{child.tag}"] = child.text.strip() if child.text else ''
        elif elem.tag == 'outlook':
            data['outlook_time'] = elem.attrib.get('outlook-time', '')
            for child in elem:
                if child.tag in ['head', 'text']:
                    data[f"outlook_{child.tag}"] = child.text.strip() if child.text else ''
        # elif elem.tag == 'coast':
        #    handle_coast(elem)

    # Function to handle coast elements
    # def handle_coast(coast_elem):
    #    coast_count = 1
    #    while f"area{coast_count}" in data:
    #        coast_count += 1
    #    for child in coast_elem:
    #        data[f"{child.tag}{coast_count}"] = child.text.strip() if child.text else ''

    # Process each element
    for child in root:
        handle_element(child)

    return data


def coast_to_dictionary(xml_data):
    """
    Convert XML data to a custom dictionary format.

    Args:
        xml_data (str): The XML data to be converted.

    Returns:
        dict: The converted dictionary containing the extracted data.
    """
    # Initialize the dictionary with predefined keys

    # Parse the XML data
    root = ET.fromstring(xml_data)

    # List to hold dictionaries of coastal area data
    coastal_areas = []

    # Iterate through each <coast> element
    for coast in root.findall('.//coast'):
        area_data = {
            'area': coast.find('area').text if coast.find('area') is not None else '',
            'wind': coast.find('wind').text if coast.find('wind') is not None else '',
            'weather': coast.find('weather').text if coast.find('weather') is not None else '',
            'visibility': coast.find('visibility').text if coast.find('visibility') is not None else ''
        }
        coastal_areas.append(area_data)

    return coastal_areas


#xml_from_url = fetch_xml_from_url(url)

#weather_metie_forecast_data = xml_to_custom_dictionary(xml_from_url)
#coast_metie_forecast_data = coast_to_dictionary(xml_from_url)

# TODO: Check if the issued_time and until_time is already in the database - if not add to the database
#for key, value in weather_metie_forecast_data.items():
#    print(f"{key}: {value}")

#for area in coast_metie_forecast_data:
#    print(area)
