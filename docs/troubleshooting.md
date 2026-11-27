# Troubleshooting log

## 1. Internal Server Error on /dbtest
- **Problem:** `/dbtest` returned HTTP 500.
- **Cause:** `permission denied for table departments`. `univ_user` could not read tables created by `postgres`.
- **Fix:** granted privileges on tables and sequences to `univ_user` in the pgAdmin Query Tool.
- **Screenshots:** screenshots/error1.png, screenshots/fix1.png, screenshots/result1.png

## 2. Credentials committed by mistake
- **Problem:** the admin password hash was written in `db/seed.sql` and pushed to GitHub.
- **Cause:** the admin insert was included in the seed file.
- **Fix:** changed the admin password, removed the insert from the seed, and documented the manual admin creation in the README.
- **Lesson:** never store credentials in the repository.

## 3. UnicodeDecodeError when opening the home page
- **Problem:** `/` returned HTTP 500 with `UnicodeDecodeError`.
- **Cause:** the database password in `DATABASE_URL` was wrong (confused with the admin password). PostgreSQL's French error message could not be decoded by psycopg2 on Windows, which hid the real error.
- **Fix:** checked the credentials with SQL Shell and set the correct `DATABASE_URL`.

## 4. Internal Server Error on /login
- **Problem:** submitting the login form returned HTTP 500.
- **Cause:** `RuntimeError: no secret key was set`. `SECRET_KEY` was not set in the terminal that started the app, so `os.environ.get("SECRET_KEY")` returned `None`.
- **Fix:** set `SECRET_KEY`, stopped old Python processes, and restarted the app.
- **Screenshots:** screenshots/error3.png, screenshots/login-page.png, screenshots/login-success.png, screenshots/login-wrong-password.png

## 5. New route returned 404
- **Problem:** `/admin/add` returned "Not Found".
- **Cause:** debug mode is off, so the running app did not load the new route.
- **Fix:** restarted the app.