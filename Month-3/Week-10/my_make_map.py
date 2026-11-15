import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("my_data/processed/ward.gpkg", layer="ward")
facilities = gpd.read_file("my_data/processed/facilities.gpkg", layer="facilities")

fig, ax = plt.subplots(figsize=(7 , 8))
wards.plot(ax=ax, color="#331CE2", edgecolor="#FC4A0A")
facilities.plot(ax=ax, color="#EFF703", markersize=4)
ax.set_title("Building Facilities in Pamba, Mirongo, and Mbugani Wards")
ax.set_axis_off()

fig.savefig("my_data/processed/Pamba_Mirongo_Mbugani_map.png", dpi=150, bbox_inches="tight")
print("Map saved")