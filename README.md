# Barcelona, Paris or Munich?

The objective is to find a city that more or less covers all the following requirements :

- 1. Designers like to go to 'tech' talks and share knowledge. There must be some nearby 'tech' companies.
- 2. 30% of the company staff have at least 1 child. Kindergarden is priority. 
- 3. Executives like Starbucks A LOT. Ensure there's a starbucks not too far.
- 4. Account managers need to travel a lot.
- 5. The CEO is vegan.
- 6. If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.


![Image text](![Image text](https://media-cdn.tripadvisor.com/media/photo-b/2560x500/15/4d/45/49/province-of-barcelona.jpg)


## Table of Contents
1. [General Info](#general-info)
2. [Data treatment](#Data-treatment)
3. [Libraries](#Libraries)
4. [Technology](#Technology)
5. [Methodology](#Methodology)

### General Info

In this analysis we intend, by choosing three cities that meet certain requirements, to extract those neighborhoods ( zip codes ) from the cities that best meet the requirements set forth in the intro section. 

### Data treatment

The realization of the project is divided into up to 3 parts: 
1. MongoDB queries to meet 1,2,4 requirements. 
2. Getting Data from Foursquare API requests' and cleaning data for visualization and distance purposes(to meet ). 
3. Visualization of the data obtained in section 2 by using the folium and seaborn library. 

## Libraries

***
A little about libraries
```
import requests
import json
import os
import pandas as pd
import src.apis as sr
from functools import reduce
import operator
from pandas import json_normalize
from dotenv import load_dotenv

```

## Technology: 

A list of technologies used within the project:
* [Jupyter Notebook](https://jupyter.org/) : Version 6.1.4
* [Python](https://www.python.org/): Version 3.8
* [Visual Studio Code](https://code.visualstudio.com/)

## Methodology: 

The realization of the project is divided into up to 3 parts: 
1. MongoDB queries to meet 1,2,4 requirements: 
    - At this part of the project I decided to choose three cities in which there are companies dedicated   to the technology sector which also are medium-sized companies like ours:
        - The first filter we will apply then will be the "web" category in order to stay with companies that are dedicated to a "Tech" sector. 
        - The second filter that i have choosed was to find 3 cosmopolitan European cities (that facilitate the travels of Account Managers) and of different sizes (1.5M Munich, 5M Barcelona, 10M Paris) to make a sample according to the size of each city. This is also my own criteria that could be easily switched.
        - We also applied a number of employees filter  to match medium sized companies like ours. 
        - Finally, we create some dirty Dataframes from the MongoDB queries for possible future usages/cleaning.
    
2. Getting Data from Foursquare API requests' and cleaning data for visualization and distance purposes.
    - For this part of the project I consider the following conditions as important for the satisfaction of the staff:
        - 30% of the company staff have at least 1 child. In this section we will only consider kindergartens as a priority. The process could be repeated with older schools.  
        - Executives like Starbucks A LOT.
        - The CEO is vegan.
        - To make the maintenance guy happy, a basketball stadium must be around 10 Km. Put some respect on maintenance staff.
    - To extract data and sort data as DF i did:
        - create a request function to get geocode locations for the cities. 
        - create a request function to foursquare API to get venues. 
        - create a create dataframe function to set and sor the data.
3. Visualization of the data obtained in section 2 by using the folium and seaborn library.
    - Usage of folium map to point out all the places found in part 2 with personalized icons and colours:
        - create a function that points out the said places en a map.
    - Creation of a function that, with the help of geopy librarie and API, transforms lattitude and longitude parameters of a Dataframe in a Zipcode. 
    - Usage of seaborn library to show some insides about the criteria filtered in the previous section


## Authors

* **Luis Sánchez de León** - *to complete work* - (https://github.com/lsdl3)