import time 
import csv

filename = './graffiti.csv'


print("# for row in csv_reader:")
t0 = time.time()
count = 0
check=0
with open(filename, 'r') as count_file:

    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        count += 1
	
	
	if (row[0]==0):
		check=1
	else:
		check=0
	a=row[0]
	fields=[a]
	if(check==0):
		with open('final_graffiti.csv', 'a') as f:
    			writer = csv.writer(f)
    			writer.writerow(fields)
print('Elapsed time : ', time.time() - t0)
print('count = ', count)
print('\n')
