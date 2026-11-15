import geopandas as gpd

print(gpd.list_layers("my_data/processed/ward.gpkg"))

wards = gpd.read_file("my_data/processed/ward.gpkg", layer="ward")

print(wards.head())
print("Rows and columns:", wards.shape)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)
