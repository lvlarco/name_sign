import requests, json
from pprint import pprint

api_key = "19c2e8d2c714c0c7423d8126fe94224f"
base_url = "https://api.openweathermap.org/data/2.5/weather?q="
city_name = 'boston'
units = 'imperial'

complete_url = base_url + city_name + "&units=" + units + "&appid=" + api_key

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()
pprint(x)
def fetch_weather(x):
    # Now x contains list of nested dictionaries
    if x["cod"] != "404":

        # store the value of "main"
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        print(" Temperature (in kelvin unit) = " +
              str(current_temperature) +
              "\n atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n humidity (in percentage) = " +
              str(current_humidiy) +
              "\n description = " +
              str(weather_description))

    else:
        print(" City Not Found ")
    return current_temperature