from requests import get
import json
from pprint import pprint
import harvesine as hv
from weather import Weather, Unit


weather = Weather(unit=Unit.CELSIUS)

lookup = weather.lookup(560743)
condition = lookup.condition

print(condition.text)

# my_long = 42.39
# my_lat = -71.12
#
# api_url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
# stations_list = get(api_url).json()['items']
#
#
#
# closest_station = hv.find_closest(my_long, my_lat, stations_list)
# closest_station = 255541
#
# station_url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/' + str(closest_station)
# print station_url
# station_weather = get(station_url).json()['items']
# pprint(station_weather)