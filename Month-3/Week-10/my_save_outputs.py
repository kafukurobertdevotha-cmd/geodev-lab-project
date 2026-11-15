import geopandas as gpd

wards = gpd.read_file("my_data/processed/ward.gpkg", layer="ward")
wards.to_file("my_data/processed/week10_outputs.gpkg", layer="ward_copy")
wards.drop(columns="geometry").to_csv("Month-3/Week-10/wards_table.csv", index=False)
print(gpd.list_layers("my_data/processed/Week10_outputs.gpkg"))