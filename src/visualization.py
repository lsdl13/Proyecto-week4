import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import pandas as pd
import requests
import json
import geopy
from pandas import json_normalize

def geocode(city):
    data = requests.get(f"https://geocode.xyz/{city}?json=1").json()
    try:
        return {
            "type":"Point",
            "coordinates":[float(data["longt"]),float(data["latt"])]}
    except:
        return data

def map_it(df, lattitude, longitude): 
    map_city= Map(location=[lattitude,longitude],zoom_start=15)
    for i, row in df.iterrows():
        name = {"location":[row["lat"], row["long"]],"tooltip" : row["name"]}

        if row["category"] == "Starbucks":
            icon = Icon(color = "black",
                        prefix = "fa",
                        icon = "coffee",
                        icon_color = "white")
        
        elif row["category"] == "Preschool":
            icon = Icon(color = "red",
                        prefix = "fa",
                        icon = "child",
                        icon_color = "white")

        elif row["category"] == "Vegan_Restaurant":
            icon = Icon(color = "green",
                        prefix = "fa",
                        icon = "leaf",
                        icon_color = "white")

        else:
            icon = Icon(color = "lightblue",
                        prefix = "fa",
                        icon = "futbol-o",
                        icon_color = "black")
        Marker(**name,icon = icon ).add_to(map_city)
    return map_city

def get_zipcode(df, geolocator, lat, long):
    location = geolocator.reverse((df[lat], df[long]))
    return location.raw['address']['postcode']