import pandas as pd
import math


def distance(lat1, lon1, lat2, lon2):
    """
    This function calculates the distance between two points on the Earth's surface, given their latitude and longitude coordinates
    using the Haversine formula.
    """
    R = 6371  # radius of the earth in km
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance

#we read data from excel files
cities_df= pd.read_excel('cities.xlsx')
potential_sites_df=pd.read_excel("potential_sites.xlsx")
cities=cities_df.values
potential_sites=potential_sites_df.values




#we create two lists universe and sets in order to be used by the genetic algorithm
sets=[]
for p_city in potential_sites:
    tmp_set = []
    for city in cities:
        if distance(city[1],city[2],p_city[1],p_city[2])<270:# the coverage range
            tmp_set.append(city[0])
    tmp_set=list(set(tmp_set))
    #we sort our list tmp_set to prevent any matching issue later in the code
    sets.append(sorted(tmp_set))

universe=[city[0] for city in cities]


