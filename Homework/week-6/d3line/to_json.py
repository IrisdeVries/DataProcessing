import csv
import json

f = open('new_data.csv', 'r')
reader = csv.reader(f, delimiter=' ',skipinitialspace=True)

# make empty list
aList = []

# modify data
for row in reader:
        tempor = []
        date = row[0][4:13]
        sdate = ''
        for char in date:
            if len(sdate) == 4 or len(sdate) == 7:
                sdate += '/'
            sdate += char
        tempor.append(sdate)

        # get temperature
        temp = row[1:2][0]
        tempor.append(temp)
        aList.append(tempor)

with open('formatted_nieuw_weer.json', 'w') as fp:
	json.dump(aList, fp)