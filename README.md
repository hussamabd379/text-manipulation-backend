# text-manipulation-backend
backend for text manipulation web app
after downloading the project in your device
apply the following commands inside the project folder :
pip install virtualenv
virtualenv venv
venv\Scripts\activate 
(only if you an error appeared after applying this line ,execute the following command )
set-executionpolicy remotesigned
pip install Flask
pip install requests

run the server with following command :
flask --app server.py  run -p 5000
(5000 is the port , its necessary to change it if you want to launch the same project twice)
