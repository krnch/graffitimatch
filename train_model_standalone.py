from clarifai import rest
from clarifai.rest import ClarifaiApp
app1 = ClarifaiApp("fXY39wieIcnVwRxNlu4d2HbKGupLzHXrvF1rYPMZ", "y6-0qljij7SOOVC1FuRylVhKh7lgeLDu-TIbfkCW")
from clarifai.rest import Image as CImage
import csv

filename = './final_graffiti.csv'


print("# for row in csv_reader:")
count=0
with open(filename, 'r') as count_file:

    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        count += 1
	if count==100:
		break
	print count
	model = app1.models.get('nsfw-v1.0')
	image = CImage(url=str(row[0]))	
	print(model.predict([image]))
