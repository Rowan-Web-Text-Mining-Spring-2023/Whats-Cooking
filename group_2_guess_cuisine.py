import json
import re
import math

#regex filter
reg = re.compile('[^a-zA-Z\s\']')

#load occurrence percentage, trainfile2(FILE TO MAKE GUESSES ON), and list of cuisines
data = {}
with open('group_2_datapercent.json') as file:
    data = json.load(file)
testfoo = []
with open('jsons/testfile2a.json') as file:
    testfoo = json.load(file)
cuisines = []
with open('jsons/group_2_cuisines.json') as file:
    cuisines = json.load(file)

#Would strip the cuisine type from the original file, but was testing with the trainfile, so not needed in practice
testfood = []
for line in testfoo:
    temp = []
    for i in line['ingredients']:
        temp.append(reg.sub('', i))
    line = {"id": line['id'], "cuisine": line['cuisine'], "ingredients": temp}
    testfood.append(line)

#Of each list of ingredients given, returns the statistically highest match of cuisine type
def check(list):
    f = {}
    for c in cuisines:
        f[c] = []
    
    for ingredient in list:
        for value in f:
            tmp = f[value]
            if ingredient in data:
                tmp.append(data[ingredient][value])
            f[value] = tmp
    
    p = {}
    for value in f:
        tmp = f[value]
        n = 0
        for i in tmp:
            if i != 0:
                n+=i
        le = len(tmp)
        if le == 0:
            le+=1
        av = n / le
        p[value] = av


    high_str = ''
    high = 0.0
    for value in p:
        if float(p[value]) > float(high):
            high = p[value]
            high_str = value

    return high_str

#Calculate guesses for each list of ingredients
out = {}
for recipe in testfood:
    out[recipe['id']] = check(recipe['ingredients'])

#For calculating accuracy, not needed in real scenario
real = {}
for recipe in testfoo:
    real[recipe['id']] = recipe['cuisine']

total = len(testfoo)
success = 0
for key in out:
    if out[key] == real[key]:
        success+=1

perce = success/total *100
strp = str(perce) + '%'
print(strp)

#Save guesses
with open('group_2_guess.json', 'w') as file:
    json.dump(out, file)

#print(check(['rice', 'diced red onions', 'pork', 'black pepper', 'black beans']))