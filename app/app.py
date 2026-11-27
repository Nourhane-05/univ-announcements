import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort
from werkzeug.security import check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

def get_db_connection():
   return psycopg2.connect(os.environ.get("DATABASE_URL"))

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin"):
            flash("Please log in first.")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

@app.route("/health")
def health():
    return "OK"

@app.route("/")
def home():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("SELECT title, the_content, publication_time,  updated_at FROM announcements ORDER BY publication_time DESC LIMIT 3")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("home.html", rows=rows)

@app.route("/departments")
def departments():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("SELECT name, description FROM departments ORDER BY name")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("departments.html", rows=rows)

@app.route("/announcements")
def announcements():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("SELECT id, title, the_content, publication_time, updated_at FROM announcements ORDER BY publication_time DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("news.html", rows=rows)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT password_hash FROM admins WHERE username = %s", (username,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row is not None and check_password_hash(row[0], password):
            session["admin"] = True
            flash("Logged in successfully.")
            return redirect(url_for("announcements"))
        flash("Invalid username or password.")
    return render_template("login.html")

@app.route("/admin/add", methods=["GET", "POST"])
@login_required
def add_announcement():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO announcements (title, the_content, publication_time) "
            "VALUES (%s, %s, NOW())",
            (title, content),
        )
        conn.commit()
        cur.close()
        conn.close()

        flash("Announcement added.")
        return redirect(url_for("announcements"))
    return render_template("announcement_form.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out.")
    return redirect(url_for("home"))

@app.route("/admin/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_announcement(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        cur.execute(
            "UPDATE announcements SET title = %s, the_content = %s, updated_at = NOW() WHERE id = %s",
            (title, content, id),
        )
        conn.commit()
        cur.close()
        conn.close()
        flash("Announcement updated.")
        return redirect(url_for("announcements"))

    cur.execute("SELECT id, title, the_content FROM announcements WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row is None:
        abort(404)
    return render_template("announcement_form.html", announcement=row)


@app.route("/admin/delete/<int:id>", methods=["POST"])
@login_required
def delete_announcement(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM announcements WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    flash("Announcement deleted.")
    return redirect(url_for("announcements"))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)