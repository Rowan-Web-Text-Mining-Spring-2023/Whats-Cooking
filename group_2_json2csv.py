import json
import csv

with open('group_2_guess.json') as jsonfile:
    data = json.load(jsonfile)


with open('group_2_predictions.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['id', 'cuisine'])
    for guess in data:
        csvwriter.writerow([guess, data[guess]])
