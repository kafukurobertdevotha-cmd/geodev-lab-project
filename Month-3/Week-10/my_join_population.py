import pandas as pd
import geopandas as gpd

wards = gpd.read_file("my_data/processed/ward.gpkg", layer="ward")
pop = pd.read_csv("my_data/raw/wards_population.csv")

first_try = wards.merge(pop, on="ward_name", how="left")
matched = first_try["Population_2022"].notna() .sum()
print("Matched on first try:", matched, "of", len(wards))

def clean_name(name):
    return name.strip().upper().replace("-", " ")

wards["join_key"] = wards["ward_name"].apply(clean_name)
pop["join_key"] = pop["ward_name"].apply(clean_name)

joined = wards.merge(pop, on="join_key", how="left")
matched = joined["Population_2022"].notna().sum()
print("Matched after cleaning:", matched, "of", len(wards))
print(joined[["ward_name_x", "Population_2022"]])