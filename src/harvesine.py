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
