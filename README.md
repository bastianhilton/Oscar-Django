Alternate CMS
To get started with this project you will need the following on your system:

Project supports Windows, Linux, and Mac (tested on Windows)

Postgresql (supports Mysql, SQlite, Mongodb)

To change database, go to shop/settings.py file and update database section with database you want
You will also need Git, Text Editor such as Visual Studio Code, and Python 3

git clone https://github.com/bastianhilton/Alternate-CMS.git
cd Alternate-CMS
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Frontend is located at localhost:8000

Administration area (dashboard) is located at localhost:8000/admin/
