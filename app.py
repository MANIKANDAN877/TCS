from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect("students.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            register_no TEXT,
            contact_no TEXT,
            mail_id TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        register_no = request.form['register_no']
        contact_no = request.form['contact_no']
        mail_id = request.form['mail_id']

        conn = sqlite3.connect("students.db")
        c = conn.cursor()
        c.execute("INSERT INTO students(name, register_no, contact_no, mail_id) VALUES (?, ?, ?, ?)",
                  (name, register_no, contact_no, mail_id))
        conn.commit()
        conn.close()

        return "Form submitted successfully!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
