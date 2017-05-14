from __future__ import print_function # In python 2.7
import os
import json
from clarifai import rest
from clarifai.rest import ClarifaiApp
app1 = ClarifaiApp("fXY39wieIcnVwRxNlu4d2HbKGupLzHXrvF1rYPMZ", "y6-0qljij7SOOVC1FuRylVhKh7lgeLDu-TIbfkCW")
from clarifai.rest import Image as CImage
import csv

# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

import sys

# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
	
	model = app1.models.get('graffiti')
	image = CImage(file_obj=open('/home/karan/flaskapp/uploads/'+str(filename), 'rb'))
	z=model.predict([image])
	values=[]
	print(z,file=sys.stderr)
	results=z['outputs'][0]['data']['concepts']
        for tag in results:
		print (tag['name'], file=sys.stderr)
		print(tag['value'], file=sys.stderr)
		values.append(tag['name'])
		values.append(tag['name'])
	#print (len(results), file=sys.stderr)
	#print i['name']
		
	print (str(z['outputs'][0]['data']['concepts'][0]),file=sys.stderr)
	
	
        return app.send_static_file('finalview.html')
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("803"),
        debug=True
    )

