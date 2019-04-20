import pyrebase

config = {
	"apiKey": "YOUR_API_KEY",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": ""
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
