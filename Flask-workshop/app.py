from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def odin_intro():
	return render_template('home.html')

@app.route('/attendee')
@app.route('/attendee/<name>')
def member(name=None):
	return render_template('attendee.html',name = name)


# make your own routes below and send pull requests 
# feel free to ask questions, we are there to help