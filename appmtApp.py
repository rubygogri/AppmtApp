# This program deals with the Appointment details to be reminded by a calendar once the data is retrieved 
# The table includes three fields - Appointment Date, Appointment Time and Appointment Description
# The technologies used for this program is Python, JSON, Bootstrap, JQuery, Javascript, Flask
#
# The Python version used for this program is 3.6.1
# The programs used are -appmtApp.py,sql.py, appt.html, appointmentDeatils.db, testTable.tbl
#
from flask import Flask, render_template, jsonify, request, Response
from flask import redirect
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

import sqlite3, json, random, sys

app = Flask(__name__)
app.secret_key = 'Pvt key'

@app.route('/')
def hello():
	return "Hello User!\n Your Appointment Details are on the 'appt.html' page"

# This seach form lets you search for a String in SEARCH BAR and then return results according to the data entered
# --If NO data is entered i.e. the string is EMPTY then ALL the results from the table are returned on the page
# --If data is entered then the string is searched in the table using LIKE for string match (not exact)
# --    Search string is NOT case sensitive
# --    String is searched as a PART of search in the table
#
class searchForm(Form):
	searchAppt = TextField("Search String")
	submit = SubmitField("Search")

# Search string is NOT case sensitive
@app.route('/appt/',methods=['GET', 'POST'])
def search():
	form = searchForm()
	if request.method=='POST':
		conn = sqlite3.connect('appointment/appointmentDetails.db')
		c = conn.cursor()

		text = request.form['searchAppt']
		print(text)

		# data = request.get_json()
		if not text:
			sel=c.execute("SELECT apptDate, apptTime, description FROM testTable")
		else:
			text='%'+text+'%'
			print(text)
			sel=c.execute("SELECT apptDate, apptTime, description FROM testTable where description LIKE ?",(text,))

		return render_template('appt.html',form=form,users=sel.fetchall())

	else:
		return render_template('appt.html',form=form)

if __name__ == "__main__":
	app.run()
	c.close()
	conn.close()
