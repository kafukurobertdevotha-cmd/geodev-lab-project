with open('wards.csv') as f:
    lines = f.readlines()

#for line in lines:
    #print(line.strip())

#print("Number of lines:", len(lines))

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
   # area = parts[1]
    #print(ward, "has area", area)
    area_km2 = int(parts[1])
    if area_km2 > 9:
        size = "large"  
    else:
        size = "small"  
    print(ward, "is", size)
   