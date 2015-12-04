import csv
import json

f = open('new_data.csv', 'r')
reader = csv.reader(f, delimiter='\t',skipinitialspace=True)

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
        #print sdate
        tempor.append(sdate)

        # get temperature
        temp = row[0][15:18]
        print temp
        tempor.append(temp)
        aList.append(tempor)

f = open('weer.csv', 'wb')
writer = csv.writer(f)
for i in range(len(date)):
    writer.writerow((sdate, temp))