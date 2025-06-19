from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Create test users
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS users")
    c.execute("CREATE TABLE users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES ('admin', 'admin123')")
    c.execute("INSERT INTO users VALUES ('user', 'user123')")
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    message = ''
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # 🚨 VULNERABLE TO SQL INJECTION 🚨
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("[DEBUG] Executing SQL:", query)

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            message = f"✅ Logged in as: {result[0]}"
        else:
            message = "❌ Login failed!"

    return render_template_string('''
        <h2>Login</h2>
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
        <p>{{message}}</p>
    ''', message=message)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

