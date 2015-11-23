import csv
import json
import re
f = open('data_population.csv', 'r')
reader = csv.reader(f, delimiter=' ',skipinitialspace=True)

# make empty list
aList = []

# modify data
for row in reader:
        tempor = []
        print row[1]

        #re.split('\t+', row)
        countries = row[0]
        #print countries

        # sdate = ''
        # for char in date:
        #     if len(sdate) == 4 or len(sdate) == 7:
        #         sdate += '/'
        #     sdate += char
        # tempor.append(sdate)

        # # get temperature
        # temp = row[1:2][0]
        # tempor.append(temp)
        # aList.append(tempor)

with open('formatted_population.txt', 'w') as fp:
	json.dump(countries, fp)