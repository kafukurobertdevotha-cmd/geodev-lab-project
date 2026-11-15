import pandas as pd

pop = pd.read_csv("my_data/raw/wards_population.csv")

big = pop[pop["Population_2022"] > 3000]
print(big)
print("Wards over 3,000:", len(big))

ranked = pop.sort_values("Population_2022", ascending=False)
print(ranked.head(3))

pop["population_thousands"] = pop["Population_2022"] / 1000
print(pop.head(3))
print("Total population:", pop["Population_2022"].sum())