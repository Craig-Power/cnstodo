# cnstodo
Demo 'Task Management/Todo List' application for the Province of Nova Scotia Cyber Security &amp; Digital Solutions department

This project was created as a demonstration application for a position with the CSNS, and was created using Python 3.10 and django. A full list of required packages may be found in requirements.txt.

Required Software:

- Docker
- Python 3.10, pip (to run outside of container), venv recommended

Instructions:

1. Clone the repository to a directory of your choosing.
2. Copy .env.example to .env
3. It is highly recommended that the secret key in .env be changed to a secure value greater than 50 characters.
4. If desired, further modify the .env file to indicate whether DEBUG mode should be True or False, or to indicate a Phase (0=Alpha, 1=Beta, 2=Release).
5. By default the project is configured to run using SQLite3 for demo purposes, a database which will be stored in ./store/db.sqlite3. The application may be modified using cnstodo/settings.py to use a mysql, postgresql, or other database.
6. Once configured as needed, run 'docker compose build' to build the container.
7. To launch, run the command 'docker compose up' to start the application.
8. By default, the application will be available at 127.0.0.1:8000. The allowed hosts may be modified using .env, and the port may be changed in docker-compose.yml
9. On first launch, a single new user is created with username 'admin' and password 'admin'. To change this, navigate to http://127.0.0.1:8000/admin, and log in with the default credentials. At this time, new users must also be added by an administrator using this panel.
10. To use the application, open http://127.0.0.1:8000 and log in with valid credentials.

Instructions for Local Deployment:
1. Clone the repository to a directory of your choosing.
2. By default, debug mode is enabled for local deployment. If you need to disable this, set an environment variable "DEBUG='False'" or modify line 41 to change the default value from 'True' to 'False'.
3. If desired, other settings that may be altered this way are PHASE (0=Alpha, 1=Beta, 2=Release), and SECRET_KEY
4. By default the project is configured to run using SQLite3 for demo purposes, a database which will be stored in ./store/db.sqlite3. The application may be modified using cnstodo/settings.py to use a mysql, postgresql, or other database.
5. Run 'python -m venv env' to create a new virtual environment and activate it ('source env/bin/activate' on linux, '.\env\Scripts\activate' on Windows)
6. Run 'pip install --upgrade pip'
7. Run 'pip install -r requirements.txt' to install necessary Python Dependencies
8. Run 'python manage.py migrate' to initialize the database (default store/db.sqlite3).
9. Run 'python manage.py initial' to load seed data and create the default admin user
10. Run 'python manage.py runserver' to start the development server. 
11. On first launch, a single new user is created with username 'admin' and password 'admin'. To change this, navigate to http://127.0.0.1:8000/admin, and log in with the default credentials. At this time, new users must also be added by an administrator using this panel.
12. To use the application, open http://127.0.0.1:8000 and log in with valid credentials.
