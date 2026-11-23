# Troubleshooting log

# Trouble 1: Internal server error on /dbtast
- Problem: opening /dbtest returned "Internal Server Error" (HTTP 500)
- Cause: permission denied for table departments. univ_user could not read tables created by postgers.
- Fix: run GRANT ALL PRIVILEGES on tables and sequences to univ_user in the pgAdmin Query Tool.
- Screenshots: screenshots/error1.png, screenshots/fix1.png, screenshots/result1.png