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
        # print row
        # # add slashes etc.
        # date = row[0:1][0]
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

#print '\n'.join(str(i) for i in aList)

# aList =[]
# for row in reader:
# 	aList.append(row)
# 	date = []
# 	temp = []
# 	xxx = []
# 	for row in aList:
# 		row_null = row[0]	
# 		date.append(row_null[0:4] + '/' + row_null[4:6] + '/' + row_null[6:8])
		
# 		date.append(int(row[1]))
# 	xxx.append(date)


with open('formatted_nieuw_weer.txt', 'w') as fp:
	json.dump(aList, fp)