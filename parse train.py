import json
import re

reg = re.compile('[^a-zA-Z\s\']')

cuisines = []
ingredients = []
food = []
with open('jsons/trainfile2.json') as f:
    food = json.load(f)

for i in food:
    if i['cuisine'] not in cuisines:
        cuisines.append(i['cuisine'])
    for e in i['ingredients']:
        tmp = reg.sub('', e)
        if tmp not in ingredients:
            ingredients.append(tmp)

with open('jsons/cuisines.json', 'w') as f:
    json.dump(cuisines, f)

with open('jsons/ingredients.json', 'w') as f:
    json.dump(ingredients, f)

num_cuisines = {}
for c in cuisines:
    num_cuisines[c] = 0

for i in food:
    num_cuisines[i['cuisine']] = num_cuisines[i['cuisine']] + 1

with open('jsons/num_cuisines.json', 'w') as f:
    json.dump(num_cuisines, f)