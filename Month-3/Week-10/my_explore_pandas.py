import pandas as pd

pop = pd.read_csv("my_data/raw/wards_population.csv")

print(pop.head())
print("Shape:", pop.shape)
print("Columns:", list(pop.columns))
print(pop.dtypes)
print(pop["Population_2022"].describe())
