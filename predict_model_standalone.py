from clarifai import rest
from clarifai.rest import ClarifaiApp

app = ClarifaiApp("_28cmpzQKbtCs81uA8HcbNVJJKvtLGw-rOCszJKl", "Ui8qBkcsesBHOF6YTDUs1y4VdhSQ9pTO5_5sQfqb")
app.models.delete_all()
# import a few labeld images
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
	app.inputs.create_image_from_url(url=str(row[0]), concepts=["graffiti"], not_concepts=["notgraffiti"])
	model = app.models.create(model_id="findgraffiti", concepts=["graffiti", "notgraffiti"])
	model = model.train()
	print model.predict_by_url(url="https://samples.clarifai.com/dog3.jpeg")

model = app.models.create(model_id="findgraffiti", concepts=["graffiti", "notgraffiti"])

model = model.train()

# predict with samples
print model.predict_by_url(url="https://samples.clarifai.com/dog3.jpeg")
print model.predict_by_url(url="http://res.cloudinary.com/pubnub-hackathon/image/upload/v1486766436/GR-040_gxjbys.jpg")
