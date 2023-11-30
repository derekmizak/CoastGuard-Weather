from scrapy import Selector
import requests
import json
import pandas as pd

#url = "https://cilpublic.cil.ie/metocean/MetOcean.aspx"
#html = requests.get(url).content
#sel = Selector(text=html)

#test = sel.xpath("//div[@id='tabs-1x']/input/@value").get()

#dict = json.loads(test)

#dict_list = list(dict.values())[0]

# TODO: Retrieval of data from the Irish Lights system to be completed here


def get_data_from_irishlights(url):
    html = requests.get(url).content
    sel = Selector(text=html)
    source_selector = sel.xpath("//div[@id='tabs-1x']/input/@value")
    dict = json.loads(source_selector.get())
    dict_list = list(dict.values())[0]
    return dict_list


#for dictionary in dict_list:
#    print("***************************************")
#    for key, value in dictionary.items():
#        print(key + " : " + value)
#    print("***************************************")

#dict_count = len(dict_list)
#df = pd.DataFrame(dict_list[0], index=[0])
#for i in range(1, dict_count - 1):
#    # df = df.append(dict_list[i], ignore_index=True)
#    df = pd.concat([df, pd.DataFrame(dict_list[i], index=[i])], ignore_index=True)
#select_clumns = ['EightHourlyID', 'MMSI', 'GustSpeed', 'AverageWindSpeed', 'WindDirection', 'WindGustDirection',
#                 'WaveHeight', 'WavePeriod', 'AirTemperature', 'WaterTemperature', 'DewPoint', 'AirPressure',
#                 'DateTransmitted']

#df[select_clumns].to_csv("buoy.csv")

