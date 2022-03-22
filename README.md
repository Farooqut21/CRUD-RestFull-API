# CRUD-RestFull-API
technical challenge (Auxin Security)
 
 steps required to run the project:
 
 1) install all the dependencies in requirements.txt using pip 
 2) after installing them you can the run the project by using the command python manage.py runserver in cfehome folder 

APIS end points are as follows:

create/view list:  http://127.0.0.1:8000/api/covid/

detail view : http://127.0.0.1:8000/api/covid/4/

update :http://127.0.0.1:8000/api/covid/4/update/

delete :http://127.0.0.1:8000/api/covid/4/delete/

for admin:
http://127.0.0.1:8000/admin/ #to give permission or create user 

Authorized users :
superuser: 
username : farooq
password : farooq

for clients:
username : staff #have all the permissions to perform CRUD

password : test12345

username : staff-2  # can only view

password : test12345

please check py_client folder to where you can directly use the endpoint without the need of browser
also i have performed only 2 tests one will be return ok(creating of user) the other will false(due to no token for authentication) 
