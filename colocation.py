# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Using Geopy
"""
import csv
from geopy.geocoders import Nominatim


locationfile = 'locations.csv'
print (locationfile)

with open(locationfile) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        city = row['Location'] + ', Manitoba, Canada'
        location = geolocator.geocode(city, timeout = 10)
        if location is not None:
            print(city, location.latitude, location.longitude)
        else:
            print ('No location for', city)
