from celery import shared_task
from weatherdata.data_retrieval_metie import fetch_xml_from_url, xml_to_custom_dictionary, coast_to_dictionary
from weatherdata.urlretrieval import get_source_urls, update_forecast_met, update_coastal_areas


@shared_task
def update_metie_forecast():
    list_of_urls = get_source_urls('xml')
    xml_records = fetch_xml_from_url(list_of_urls[0])

    forecast_data = xml_to_custom_dictionary(xml_records)

    coastal_areas = coast_to_dictionary(xml_records)

    forecast_obj, forecast_created = update_forecast_met(forecast_data)


    if forecast_created:
        for coastal_area in coastal_areas:
            update_coastal_areas(coastal_area, forecast_obj)




# TODO: Add tasks for updating the other forecast sources
def update_irishlights_data():
    pass
