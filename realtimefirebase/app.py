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

db = firebase.database()	#initialize the database.

# db.child("names").push({"name":"siddhesh"})
# db.child("names").update({"name":"siddhi"})

# users = db.child("names").child("name").get()
# print(users.val())

# db.child("another_child").push({"name":"jimkwik"})

# db.child("names").child("name").remove()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':

			name = request.form['name']
			db.child("todo").push(name)
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('index.html', t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		return render_template('index.html')
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)
