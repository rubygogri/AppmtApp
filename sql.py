#This is the program to setup SQLit3 database
import sqlite3

#Thhis function creates the table and also inserts 3 rows in the table
def create_table():
	conn = sqlite3.connect('appointment/appointmentDetails.db')
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS testTable(apptDate TEXT, apptTime TEXT, description TEXT)")

	c.execute("INSERT INTO testTable(apptDate, apptTime, description) VALUES('03/27/2018','10.00AM','Meet Vice President, Mr. ABC')")
	c.execute("INSERT INTO testTable(apptDate, apptTime, description) VALUES('04/01/2018','12.15PM','Meet CEO, Mr. XYZ')")
	c.execute("INSERT INTO testTable(apptDate, apptTime, description) VALUES('03/28/2018','11.00AM','Dentist Appointment, Dr. DEF')")

	c.close()
	conn.commit()
	
	conn.close()

#This function is to select table contents
def getAllAppt():
	conn = sqlite3.connect('appointment/appointmentDetails.db')
	c = conn.cursor()

	sel=c.execute("SELECT apptDate, apptTime, description FROM testTable")

	print(sel.fetchall())

	c.close()
	conn.close()

create_table()
getAllAppt()	

