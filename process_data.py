
import geopandas as gpd
import re
from bs4 import BeautifulSoup

# Read the KML file
gdf = gpd.read_file('fire_stations.kml', driver='KML')

def extract_station_name(description):
    if description is None:
        return None
    soup = BeautifulSoup(description, 'html.parser')
    station_name_td = soup.find('td', string='StationName')
    if station_name_td:
        return station_name_td.find_next_sibling('td').text
    return None

def extract_station_number(station_name):
    if station_name is None:
        return None
    match = re.search(r'(\d+)$', station_name)
    if match:
        return int(match.group(1))

    match = re.search(r'Sta (\d+)', station_name)
    if match:
        return int(match.group(1))

    return None

gdf['station_name'] = gdf['Description'].apply(extract_station_name)
gdf['station_number'] = gdf['station_name'].apply(extract_station_number)

# Select and rename columns
gdf = gdf[['station_name', 'station_number', 'geometry']]

# Save to geoparquet
gdf.to_parquet('fire_stations.parquet', index=False)
