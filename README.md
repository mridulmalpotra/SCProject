# SCProject
End semester project for Secure Coding<br>
Download virtualenv and create a virtual environment.<br>
Install all the requirements in the virtual environment.<br>
Before running project. Create database in MYSQL.<br>
Use following commands :<br>
create database SC_Project_Database;<br>
Change the MYSQL password in settings.py in SCProject/SCProject directory.<br>
Commands to run project : <br>
Go to SCProject root directory.<br>
Run following commands : <br>
python manage.py migrate (this commands create all the sql tables for you)<br>
python manage.py runserver (this starts a local server)<br>
go to browser and type the server ip and port no. (Example :  http://127.0.0.1:8000/)<br>
App is running now.<br>
<br>
<br>
Since, the app will run in development mode the invalid url will throw exception.<br>
All the allowed urls are as follows:<br>
I will assume server IP is http://127.0.0.1:8000/<br>
1) http://127.0.0.1:8000/
2) http://127.0.0.1:8000/eventsApp
4) http://127.0.0.1:8000/eventsApp/signin
5) http://127.0.0.1:8000/eventsApp/signup
6) http://127.0.0.1:8000/eventsApp/dashboard
7) http://127.0.0.1:8000/eventsApp/dashboard/create
8) http://127.0.0.1:8000/eventsApp/dashboard/viewall (for both normal and admin user. admin user gets edit and delete option also)
9) http://127.0.0.1:8000/eventsApp/dashboard/myevents
10) http://127.0.0.1:8000/eventsApp/dashboard/profile
11) http://127.0.0.1:8000/eventsApp/dashboard/logout
12) http://127.0.0.1:8000/eventsApp/dashboard/viewUsers (only for admin user)
13) http://127.0.0.1:8000/eventsAPI/events
14) http://127.0.0.1:8000/eventsAPI/events/<username> (for API call roll no of student)
15) http://127.0.0.1:8000/eventsUnsafeAPI/events/<rollno> (for API call roll no of student) (prone to sql injection) 