import pyrebase

config = {
	"apiKey": "AIzaSyCKbvpL90wX5VXIhOm9Td264O9Cyi0UCLE",
    "authDomain": "realtime160319.firebaseapp.com",
    "databaseURL": "https://realtime160319.firebaseio.com",
    "projectId": "realtime160319",
    "storageBucket": "realtime160319.appspot.com",
    "messagingSenderId": "177956391142"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

# storage.child("images/new.jpg").put("makeithappen.jpg")

# storage.child("images/new.jpg").download("example_makeithappen.jpg")

# url = storage.child("images/new.jpg").get_url(None)
# print(url)

from flask import *

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def basic():
	if request.method == 'POST':
		upload = request.files['upload']
		storage.child("images/new.jpg").put(upload)
		return redirect(url_for('uploads'))
	return render_template('index1.html')

@app.route('/uploads')
def uploads():
	if True:
		links = storage.child("images/new.jpg").get_url(None)
		return render_template('upload.html',l = links)
	return render_template('upload.html')


if __name__ == '__main__':
	app.run(debug=True)