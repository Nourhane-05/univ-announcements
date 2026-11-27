# NBM Academia: University Announcements 
a small dynamic web app (fictional) built for a cloud computing project. students, teachers and visitors can find departments and announcements. an administartor can login to add, edit and delete announcements.

Stack: python, flask, gunicorn, psycopg2, postgreSQL.

Project structure:

app/ : flask application(app.py, templates/, static/)
db/ : schema.sql and seed.sql
deploy/ : deployment files (Docker, Rander)
docs/ : troubleshooting log, decisions log, screenshotes 
requirements.txt

Environment variables:
the app reads its configuration from the evironment. never commit real values.
DATABASE_URL: postgresql://<user>:<password>@<host>:5432/<database> (it's required variable)
SECRET_KEY:long random text used to login sessions. use a different value for each environment. (it's required variable)
PORT : port the app listens on (default 8000). the app binds to 0.0.0.0 .

Generate a secret key:
python -c "import secrets; prints(secrets.token_hex(32))"

Database setup : (database password:cloud)
 Run these in order on an empty database:
 1. db/schema.sql (creates the "departments", "announcements" and "admins" tables)
 2. db/seed.sql (sample data (fictional), run once)
 3. for the admin account creation it's not in db/seed.sql for securety reasons (no credentials are stord in the repository). to create the admin user do as follow:

 1) Generate a password hash : (password: cloudp)
 in anaconda_prompt(do the RUN locally part first)
 python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('cloudp'))"

 2) Insert the admin:
in postgreSQL :  
INSERT INTO admins (username, password_hash)
VALUES ('<username>', '<password_hash>');

3) Verify (do not display the hash):
in postgreSQL :
SELECT id, username FROM admins;

## Run locally (Windows, Anacond Prompt):

conda create -n univ-app python=3.12
conda activate univ-app
pip install -r requirements.txt
### (you can generate the password hash now)
set DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<database>
set SECRET_KEY=<random-text>
python app\app.py

Open http://localhost:8000 

Note: environment variables set with "set" are temporary they last only for that terminal window, restart the app after any change in "app.py"

## Run with gunicorn (production):
gunicorn --chdir app app:app --bind 0.0.0.0:8000

on rander use "$PORT" instead of 8000

# Routes:
"/" : univ predentation and the latest 3 announcements.
 (access: public)
"/departments" : departments and there description from the database. (access: public)
"/announcements" : all the announcements. (access: public)
"/health" : Returns OK (health check). (access: public)
"/login","/logout" : Admin login and logout pages (access: public)
"/admin/add" : add an announcement. (access: admin)
"/admin/edit/<id>" : edit an announcement. (access: admin)
"/admin/delete/<id>" : delete an announcement. (access: admin)

Notes for deployment:
- the databes must not be exposed outside the private network (Docker network, or Render's internal connection).
- use persistent storage for the database (a Docker volume, or Render's managed PostgerSQL).
