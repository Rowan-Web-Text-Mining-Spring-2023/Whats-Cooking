import json

ingred = []
cuisines = []
train = []
num_cuisines = {}

#Loading ingredient list, cuisines, number of each cuisine, and trainfile
with open('jsons/ingredients.json') as file:
    ingred = json.load(file)
with open('jsons/cuisines.json') as file:
    cuisines = json.load(file)
with open('jsons/trainfile2.json') as file:
    train = json.load(file)
with open('jsons/num_cuisines.json') as file:
    num_cuisines = json.load(file)

#Map of cuisines mapped to 0
map_values_template = {}
for c in cuisines:
    map_values_template[c] = 0

#For each ingredient, check each recipe and keep track of how many are in line with each cuisine type
data = {}
datapercent = {}
for ingredient in ingred:
    map_v = {}
    map_p = {}
    for c in cuisines:
        map_v[c] = 0
        map_p[c] = 0
    for recipe in train:
        if ingredient in recipe['ingredients']:
            map_v[recipe['cuisine']] = map_v[recipe['cuisine']] + 1
            map_p[recipe['cuisine']] = (map_v[recipe['cuisine']])/num_cuisines[recipe['cuisine']]
    data[ingredient] = map_v
    datapercent[ingredient] = map_p

#Save files, one raw data, other included percentage of occurence
with open('datapercent.json', 'w') as f:
    json.dump(datapercent, f)
with open('data.json', 'w') as f:
    json.dump(data, f)

