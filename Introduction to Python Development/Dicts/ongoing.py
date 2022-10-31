ages = { ' kevin ' : 29 , ' alex ' : 30 , ' bob ' : 40 }
agesv2 = dict(pedro=29, cano=30, losa=40)
claves=list(ages.values())
print(agesv2)
print(claves)
ages[' adrian ']=22
print(ages[' adrian '])
ages.pop(' kevin ')
print(ages)
