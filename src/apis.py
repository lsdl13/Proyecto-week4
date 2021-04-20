import pandas as pd
import requests
import json
import os
from pandas import json_normalize
import operator
from functools import reduce
from dotenv import load_dotenv
load_dotenv()


def geocode(city):
    data = requests.get(f"https://geocode.xyz/{city}?json=1").json()
    try:
        return {
            "type":"Point",
            "coordinates":[float(data["longt"]),float(data["latt"])]}
    except:
        return data

def data(lat, lon, query):
    tok1 = os.getenv("token1")
    tok2 = os.getenv("token2")
    url_query = 'https://api.foursquare.com/v2/venues/explore'
     
    parameters = {"client_id" : tok1,
                "client_secret" : tok2,
                "v": "20180323",
                "ll": f"{lat}, {lon}",
                "query":query,
                "limit": 100,
                "radius": 10000}  
    resp = requests.get(url= url_query, params=parameters).json()
        
    return resp

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def create_dataframe (*args):

    mapa_nombre =  ["venue", "name"]
    mapa_latitud = ["venue", "location", "lat"]
    mapa_longitud = ["venue", "location", "lng"]
    
    results = []

    for i in args:
        for dic in i:            
            paralista = {}
            paralista["name"] = getFromDict(dic,mapa_nombre)
            paralista["latitud"] = getFromDict(dic,mapa_latitud)
            paralista["longitud"] = getFromDict(dic,mapa_longitud)
            results.append(paralista)
    df = pd.DataFrame(results)

    return df
