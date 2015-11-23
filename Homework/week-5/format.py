import csv
import json
import re
f = open('data_population.csv', 'r')
reader = csv.reader(f, delimiter='\t',skipinitialspace=True)

# make empty list
aList = []

# modify data
for row in reader:
        tempor = []
        countries = row[0]
        values = row[1]
        print countries
        print values

        tempor.append(countries)
        tempor.append(values)
        aList.append(tempor)

with open('formatted_population.txt', 'w') as fp:
	json.dump(aList, fp)