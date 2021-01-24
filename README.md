# mysite
Tutorial website
Set up the Python development environment. We recommend using a Python virtual environment.
Assuming you have Python setup, run the following commands:
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # Create a superuser
python manage.py runserver
Open a browser to http://127.0.0.1:8000/admin/ to open the admin site
Create a few test objects of each type.
Open tab to http://127.0.0.1:8000 to see the main site, with your new objects.
