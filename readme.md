# SQL Injection Demo Application

This is a simple Flask web application demonstrating a classic SQL Injection vulnerability. The app allows users to "log in" with a username and password, but due to unsafe query construction, it is vulnerable to SQL Injection attacks.

## Features

- Vulnerable login form using string concatenation for SQL queries
- Demonstrates how attackers can bypass authentication using SQL Injection
- Simple SQLite database with example users
- Debug output showing the executed SQL query

## Getting Started

### Prerequisites

- Python 3.x
- Flask (`pip install flask`)

### Running the Application

1. Clone or download this repository.
2. Install Flask if you haven't already:
   ```bash
   pip install flask
3. Run the app
   ```bash
   python3 app.py
Open your browser and go to http://127.0.0.1:5000

Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage

To demonstrate the SQL Injection vulnerability:

Enter this into the **Username** field:

' OR '1'='1' --
Leave the Password field blank.

Submit the form.

You will bypass authentication and be logged in as the first user in the database (e.g., admin).


Leave the **Password** field blank.

Submit the form.

You will bypass authentication and be logged in as the first user in the database (e.g., admin).

## How it works

The app builds SQL queries by concatenating user input directly into the SQL statement, like this:

```sql
SELECT * FROM users WHERE username = '[input]' AND password = '[input]'


## How to fix

The vulnerability exists because the app constructs SQL queries by directly inserting user input into the query string. To fix this, **use parameterized queries (also called prepared statements)** which safely handle user input and prevent SQL injection.

Example fix in Python with SQLite:

```python
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))


