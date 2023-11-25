import requests
import xml.etree.ElementTree as ET

def xml_to_dict(element):
    if not element:
        return element.text or ''
    return {sub.tag: xml_to_dict(sub) for sub in element}

# URL of the XML file
url = 'https://www.met.ie/Open_Data/xml/Met-Sea-area.xml'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the XML from the response content
    root = ET.fromstring(response.content)

    # Convert the root element to a dictionary
    data_dict = xml_to_dict(root)

    print(data_dict)
else:
    print(f"Failed to retrieve data: {response.status_code}")
