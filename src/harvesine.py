from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    r_earth = 6371  # km
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    distance = 2 * asin(sqrt(a)) * r_earth

    return distance

def find_closest(lon1, lat1, stations_list):
    smallest_dist = 10000
    closest_station = 'None'
    for station in stations_list:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        calc_dist = haversine(lon1, lat1, station_lon, station_lat)
        if calc_dist < smallest_dist:
            # smallest_dist = calc_dist
            # print smallest_dist
            closest_station = station['weather_stn_id']
    return closest_station

def day_status(temperature):
    if temperature <= 20:
        status = "frigid"
    elif 20 < temperature < 40:
        status = "cold"
    elif 40 < temperature < 80:
        status = "nice"
    else:
        status = "hot"

    return status

def fetch_weather(x):
    # Now x contains list of nested dictionaries
    if x["cod"] != "404":

        # store the value of "main"
        y = x["main"]

        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print(" Temperature (in kelvin unit) = " +
        #       str(current_temperature) +
        #       "\n atmospheric pressure (in hPa unit) = " +
        #       str(current_pressure) +
        #       "\n humidity (in percentage) = " +
        #       str(current_humidiy) +
        #       "\n description = " +
        #       str(weather_description))
    else:
        print(" City Not Found ")

def center_cursor(message, lcd_length):
    '''Finds the cursor position to center message in LCD screen'''
    msg_length = len(message)
    print'len'
    print msg_length
    cursor_pos = int((lcd_length - msg_length) / 2)
    return cursor_pos