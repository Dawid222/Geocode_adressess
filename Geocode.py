import pandas as pd
import numpy as np

import geopandas as gpd
import geopy

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

from tqdm import tqdm
from tqdm.notebook import tqdm_notebook

####################################################################
locator = Nominatim(user_agent="myGeocoder")
coordinates = "53.480837, -2.244914"
location = locator.reverse(coordinates)

csv ="test2.csv"
df = pd.read_csv(csv)

df["geocode"] =  df["ay"].map(str)  + ',' + df['ax'].map(str)

locator = Nominatim(user_agent="myGeocoder", timeout=10)
rgeocode = RateLimiter(locator.reverse, min_delay_seconds=0.001)\

tqdm.pandas()
df['address_all'] = df['geocode'].progress_apply(rgeocode)
df['nr_house'] = df['address_all'].apply(lambda x: (x.raw['address']['house_number'] if 'house_number' in x.raw['address'].keys() else None ))
df['road'] = df['address_all'].apply(lambda x: (x.raw['address']['road'] if 'road' in x.raw['address'].keys() else None ))
df['city'] = df['address_all'].apply(lambda x: (x.raw['address']['city'] if 'city' in x.raw['address'].keys() else None ))
df['country'] = df['address_all'].apply(lambda x: (x.raw['address']['country'] if 'country' in x.raw['address'].keys() else None ))
df['postcode'] = df['address_all'].apply(lambda x: (x.raw['address']['postcode'] if 'postcode' in x.raw['address'].keys() else None ))

#print(df.head())
df.to_csv("data_geocode_test2.csv")

####################################################################

