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

# Now you can import your models
from weatherdata.models import SourceFormat, SourceURL

def get_xml_source_urls():
    # Retrieve the SourceFormat instance for 'xml'
    xml_format = SourceFormat.objects.get(name='xml')


    # Retrieve all SourceURL instances that have the 'xml' format
    xml_urls = SourceURL.objects.filter(format=xml_format)

    # Extract the URL strings from the queryset
    url_list = [source_url.url for source_url in xml_urls]

    return url_list

print(get_xml_source_urls())
