# dictionary
myDict = {'Brand': 'Toyota', 'model': 'Camry', 'Year': 2020}
print (myDict)

getDict = dict (Brand='APSONIC', Model='Aloba',  Year=2023)
print (getDict)

print (getDict.keys())
print (getDict.values())
print (getDict.items())

print (getDict["Brand"])

getDict["Colour"]="Black"
print (getDict)

for x in getDict.keys():
    print (x)


