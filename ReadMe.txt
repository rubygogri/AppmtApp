Technologies Used : 

## Python - 3.6.1
## JSON
## Sql Lite - 3
## JQUERY
## HTML - 5
## BootStrap
## Flask

PROJECT REQUIREMENTS : 

This project uses 
	- Python as Back end (appmtApp.py)
	- Flask for connectivity
	- SQLit3 as Database (appointmentDetails.db and testTable.tbl as tablename)
		 The table includes three fields - Appointment Date, Appointment Time and Appointment Description
	- HTML page with JSON, JQUERY and CSS (appt.html)

Use http://127.0.0.1:5000/appt to View / Add Appointment Details

http://127.0.0.1:5000 is the base page which displays a 'Welcome Page'

1. If no parameters are passed to Python, then it renders HTML document
2. If AJAX paaremters are passed then JSON docuemnt is rendered
3. If appointment details are added on the screen data is added in the Database
4. If apoointment are viewed using 'Search' query, data is retrieved from the Database and displayed

	=============================================
	=  +---+
	=  |NEW|
	=  +---+
	=  
	=  +-------------------+  +------+
	=  |                   |  |SEARCH|
	=  +-------------------+  +------+
	=
	=  <appointments table will be here>
	=============================================


	==============================================
	=  
	=  +---+
	=  |NEW|
	=  +---+
	=  
	=  +-------------------+  +------+
	=  |                   |  |SEARCH|
	=  +-------------------+  +------+
	=  
	=  +-------+---------+----------------+
	=  | DATE  | TIME    | DESCRIPTION    |
	=  +-------+---------+----------------+
	=  | May 2 | 11:00am | Something      |
	=  | May 2 | 12:00pm | Something else |
	=  | May 4 |  8:00am | Meet foo       |
	=  +-------+---------+----------------+
	=  
	==============================================


	==============================================
	=  
	=  +---+
	=  |NEW|
	=  +---+
	=  
	=  +-------------------+  +------+
	=  | Something         |  |SEARCH|
	=  +-------------------+  +------+
	=  
	=  +-------+---------+----------------+
	=  | DATE  | TIME    | DESCRIPTION    |
	=  +-------+---------+----------------+
	=  | May 2 | 11:00am | Something      |
	=  | May 2 | 12:00pm | Something else |
	=  +-------+---------+----------------+
	=  <notice only the rows containing "Something" appear>
	==============================================


	==============================================
	=  
	=  +---+ +------+
	=  |ADD| |CANCEL|
	=  +---+ +------+
	=  
	=       +--------------------+
	=  DATE |                    |
	=       +--------------------+
	=       +--------------------+
	=  TIME |                    |
	=       +--------------------+
	=       +--------------------+
	=  DESC |                    |
	=       +--------------------+ 
	=  
	=  +-------------------+  +------+
	=  |                   |  |SEARCH|
	=  +-------------------+  +------+
	=  
	=  +-------+---------+----------------+
	=  | DATE  | TIME    | DESCRIPTION    |
	=  +-------+---------+----------------+
	=  | May 2 | 11:00am | Something      |
	=  | May 2 | 12:00pm | Something else |
	=  | May 4 |  8:00am | Meet foo       |
	=  +-------+---------+----------------+
	=  
	==============================================
