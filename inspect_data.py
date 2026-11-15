import csv

#with open("wards_settlement.csv") as f:
 #   reader = csv.DictReader(f)
  #  rows = list(reader)
#print("Number of rows:", len(rows))
#print("Columns", list(rows[0].keys()))

#with open('wards_settlement.csv', encoding='utf-8-sig') as f:
 #   rows = list(csv.DictReader(f))

#values = []
#for row in rows:
 #   value = float(row['Area_km2'])
  #  values.append(value)

#print("Smallest:", min(values))
#print("Largest:", max(values))
#print("Count:", len(values))

#Step 5: Turn it into a function that returns  


def inspect_column(filename, column):
    with open(filename, encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == '':
           continue
        values.append(float(raw))
    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values)
    }

result = inspect_column("wards_settlement.csv", "Area_km2")
print(result)


#Step 6: Use your finction twice

area_result = inspect_column ("wards_settlement.csv","Area_km2")
building_result = inspect_column("wards_settlement.csv","building_count")

print("Area:", area_result)
print("Building Count:", building_result)
