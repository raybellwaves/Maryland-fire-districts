
import geopandas as gpd
import os

def test_geoparquet_file():
    # Check if the file exists
    assert os.path.exists('fire_stations.parquet'), "The geoparquet file does not exist."

    # Read the geoparquet file
    gdf = gpd.read_parquet('fire_stations.parquet')

    # Check if the dataframe is not empty
    assert not gdf.empty, "The geoparquet file is empty."

    # Check for the required columns
    expected_columns = ['station_name', 'station_number', 'geometry']
    for col in expected_columns:
        assert col in gdf.columns, f"The column '{col}' is missing from the geoparquet file."
