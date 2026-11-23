import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
   return psycopg2.connect(os.environ.get("DATABASE_URL"))

@app.route("/health")
def health():
    return "OK"

@app.route("/dbtest")
def dbtest():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("SELECT COUNT(*) FROM departments")
    total=cur.fetchone()[0]
    cur.close()
    conn.close()
    return str(total)

@app.route("/departments")
def departments():
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("SELECT name, description FROM departments ORDER BY name")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("departments.html", rows=rows)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)