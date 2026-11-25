# univ-announcements
## Create the admin user

The admin account is not included in `db/seed.sql`, so no credentials are stored in the repository. Create it manually after running the schema and seed files.

**1. Generate a password hash** (replace `<password>` with your own demo password):

```
python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('<password>'))"
```

Copy the whole output.

**2. Insert the admin in PostgreSQL** (using `psql`):

```sql
INSERT INTO admins (username, password_hash)
VALUES ('<username>', '<password_hash>');
```

Replace `<username>` with the admin name and `<password_hash>` with the hash from step 1. Keep the single quotes.

**3. Verify** (this does not display the hash):

```sql
SELECT id, username FROM admins;
```

If the username already exists, update the hash instead:

```sql
UPDATE admins SET password_hash = '<password_hash>' WHERE username = '<username>';
