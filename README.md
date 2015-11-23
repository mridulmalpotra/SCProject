# SCProject
## End semester project for Secure Coding<br>

### Requirements
* Install the python package installer `pip`.
* Use `pip` installer to automatically install the dependencies in the virtualenv. Command: `pip install -r requirements.txt`
(mysql_config can have some errors. Try installing with the system package manager if issues persist)
* Now, install MySQL using the system package manager as well if not present. Configure usernames and passwords, to be used later.

### Instructions to build the project

* Download `virtualenv` and create a virtual environment. More details [here](http://docs.python-guide.org/en/latest/dev/virtualenvs/).<br>
* Install all the requirements in the virtual environment.<br>
* Before running project. Create database in MYSQL. MySQL prompt: `CREATE DATABASE SC_Project_Database;<br>`
* Change the MySQL username and password in settings.py in the main directory as configured above.<br>
* Go to SCProject root directory.<br>
* Run following commands : <br>
`python manage.py migrate` (this commands create all the sql tables for you)<br>
`python manage.py runserver <optional domain name and IP address/ empty implies localhost>` (this starts a local server)<br>

* Go to browser and type the server ip and port no. (Example :  http://127.0.0.1:8000/)<br>
* App will be running now.<br>
<br>
<br>
* Since, the app will run in development mode the invalid url will throw exception.<br>

### Allowed URLs

All the allowed urls are as follows:<br>
I will assume server IP is http://127.0.0.1:8000/<br>
1) http://127.0.0.1:8000/ <br>
2) http://127.0.0.1:8000/eventsApp <br>
3) http://127.0.0.1:8000/eventsApp/signin <br>
4) http://127.0.0.1:8000/eventsApp/signup <br>
5) http://127.0.0.1:8000/eventsApp/dashboard <br>
6) http://127.0.0.1:8000/eventsApp/dashboard/create <br>
7) http://127.0.0.1:8000/eventsApp/dashboard/viewall (for both normal and admin user. admin user gets edit and delete option also) <br>
8) http://127.0.0.1:8000/eventsApp/dashboard/myevents <br>
9) http://127.0.0.1:8000/eventsApp/dashboard/profile <br>
10) http://127.0.0.1:8000/eventsApp/dashboard/logout <br>
11) http://127.0.0.1:8000/eventsApp/dashboard/viewUsers (only for admin user) <br>
12) http://127.0.0.1:8000/eventsAPI/events <br>
13) http://127.0.0.1:8000/eventsAPI/events/(username) (for API call roll no of student) <br>
14) http://127.0.0.1:8000/eventsUnsafeAPI/events/(rollno) (for API call roll no of student) (prone to sql injection) 
