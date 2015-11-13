import csv

f = open('data.csv', 'r')
reader = csv.reader(f, delimiter=' ',skipinitialspace=True)
aList =[]
for row in reader:
	aList.append(row)

date = []
temp = []
for row in aList:
	iets = row[0]	
	date.append(iets[0:4] + '/' + iets[4:6] + '/' + iets[6:8])
	temp.append(int(row[1]) / 10.0)

	print temp

f = open('formatted_weer.csv', 'wb')
writer = csv.writer(f)
for i in range(len(date)):
	writer.writerow((date[i], temp[i]))