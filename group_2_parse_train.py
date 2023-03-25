import json
import re

#Regex filter
reg = re.compile('[^a-zA-Z\s\']')

#load train file
cuisines = []
ingredients = []
food = []
with open('jsons/trainfile2.json') as f:
    food = json.load(f)

#for each line in trainfile, add ingredients and cuisine type if not already being tracked
for i in food:
    if i['cuisine'] not in cuisines:
        cuisines.append(i['cuisine'])
    for e in i['ingredients']:
        tmp = reg.sub('', e)
        if tmp not in ingredients:
            ingredients.append(tmp)

#Save cuisines and ingredients lists
with open('jsons/group_2_cuisines.json', 'w') as f:
    json.dump(cuisines, f)

with open('jsons/group_2_ingredients.json', 'w') as f:
    json.dump(ingredients, f)

#Calculate occurences of each cuisine
num_cuisines = {}
for c in cuisines:
    num_cuisines[c] = 0

for i in food:
    num_cuisines[i['cuisine']] = num_cuisines[i['cuisine']] + 1

#Save occurrences of each cuisine
with open('jsons/group_2_num_cuisines.json', 'w') as f:
    json.dump(num_cuisines, f)