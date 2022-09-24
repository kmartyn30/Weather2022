import csv
import kdtree
import os


class City:
    '''
    City wraps up the info about a city, including its name, coordinates,
    and belonging country.
    '''
    def __init__(self, city_name, country_code):
        self.city_name = city_name
        self.country_code = country_code


# load the city data up
_current_dir, _current_filename = os.path.split(__file__)
_world_cities_csv_path = os.path.join(_current_dir, 'worldcities.csv')
_world_cities_kdtree = kdtree.create(dimensions=2)
WORLD_CITIES_DICT = {}

with open(_world_cities_csv_path, 'r') as csv_file:
    cities = csv.reader(csv_file)

    # discard the headers
    cities.__next__()

    # populate geo points into kdtree
    for city in cities:
        city_coordinate_key = (float(city[2]), float(city[3]))
        _world_cities_kdtree.add(city_coordinate_key)
        c = City(city[1], city[0])
        WORLD_CITIES_DICT[city_coordinate_key] = c


def nearest_city(latitude, longitude):
    nearest_city_coordinate = _world_cities_kdtree.search_nn((latitude, longitude, ))
    return WORLD_CITIES_DICT[nearest_city_coordinate[0].data]
from citipy import citipy
city = citipy.nearest_city(22.99,12021)
city
<city.City istance at 0x1069b6518>

city.city_name   #Tainan, my home town
'tainan'

city.country_code'tw'             #And the county is Taiwan
from citipy import citipy
for(nearest_city ()
city_name = citipy.nearest_city(coordiante[0], coordiate[1],coordinate[1]).city_name,
country_code = citipy.nearest_city(coordinate[0], coordinate[1]).couountryycodee)
# Use the print() function to display the latitude and longitude combinations.
for coordinate in coordinates:
    print(citipy.nearest_city(coordinate[0], coordinate[1]).city_name,
          citipy.nearest_city(coordinate[0], coordinate[1]).country_code)

from citipy import citipy
# Create a list for holding the cities.
cities = []
# Identify the nearest city for each latitude and longitude combination.
for coordinate in coordinates:
    city = citipy.nearest_city(co # If the city is unique, then we will add it to the cities list.
    if city not in cities:
        cities.append(city)
# Print the city count to confirm sufficient count.
len(cities)ordinate[0], coordinate[1]).city_name
