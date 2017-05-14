import urllib

import csv

filename = './final_graffiti.csv'


print("# for row in csv_reader:")
count=1
with open(filename, 'r') as count_file:

    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        
	if count==100:
		break
	print count
	try:
		urllib.urlretrieve(str(row[0]), str(count)+".jpg")
	except:
		continue	
	count=count+1
	

