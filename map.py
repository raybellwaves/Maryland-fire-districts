
import geopandas as gpd
import folium

# Read the geoparquet file
gdf = gpd.read_parquet('fire_stations.parquet')

# Create a map centered around Maryland
m = folium.Map(location=[39.0458, -76.6413], zoom_start=8)

# Add points to the map
for idx, row in gdf.iterrows():
    # Check if the geometry is not None and is a point
    if row.geometry and row.geometry.geom_type == 'Point':
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=row['station_name']
        ).add_to(m)

# Save the map to an HTML file
m.save('docs/index.html')
