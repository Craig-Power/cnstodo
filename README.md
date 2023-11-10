# cnstodo
Demo 'Task Management/Todo List' application for the Province of Nova Scotia Cyber Security &amp; Digital Solutions department

This project was created as a demonstration application for a position with the CSNS, and was created using Python 3.10 and django. A full list of required packages may be found in requirements.txt.

Required Software:

- Python 3.10 (for local build/run)
- Docker

Instructions:

1. Clone the repository to a directory of your choosing.
2. Copy .env.example to .env
3. It is highly recommended that the secret key in .env be changed to a secure value greater than 50 characters.
4. If desired, further modify the .env file to indicate whether DEBUG mode should be True or False, or to indicate a Phase (0=Alpha, 1=Beta, 2=Release).
5. By default the project is configured to run using SQLite3, a database which will be stored in ./store/db.sqlite3. The application may be modified using cnstodo/settings.py to use a mysql, postgresql, or other database.
6. Once configured as needed, run 'docker compose build' to build the container.
7. To launch, run the command 'docker compose up' to start the application.
8. By default, the application will be available at 127.0.0.1:8000. The allowed hosts may be modified using .env, and the port may be changed in docker-compose.yml
9. On first launch, a single new user is created with username 'admin' and password 'admin'. To change this, navigate to http://127.0.0.1:8000/admin, and log in with the default credentials. At this time, new users must also be added by an administrator.
10. To use the application, open http://127.0.0.1:8000 and log in with valid credentials.
