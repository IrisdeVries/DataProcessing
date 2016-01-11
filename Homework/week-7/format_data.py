import csv
import json
import re
f = open('raw_data_HPI.txt', 'r')
reader = csv.reader(f, delimiter='\t',skipinitialspace=True)

# make empty list
aList = []

# modify data
for row in reader:
        tempor = []
        countries = row[0]
        life_expectancy = row[1]
        well_being = row[2]
        footprint = row[3]
        HPI = row[4]
        print countries
        print life_expectancy

        tempor.append(countries)
        tempor.append(life_expectancy)
        tempor.append(well_being)
        tempor.append(footprint)
        tempor.append(HPI)
        aList.append(tempor)

with open('formatted_HPI.json', 'w') as fp:
	json.dump(aList, fp)