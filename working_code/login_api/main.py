from flask import Flask, render_template, redirect, url_for, session, request
from flask_mysqldb import MySQL
import MySQLdb
from config import USER, PASSWORD, HOST, DATABASE


app = Flask(__name__)
app.secret_key = "123456789"


app.config["MySQL_HOST"] = HOST
app.config["MYSQL_USER"] = USER
app.config["MYSQL_PASSWORD"] = PASSWORD
app.config["MYSQL_DB"] = DATABASE


database = MySQL(app)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/profile', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = database.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM login_info WHERE username=%s AND password=%s", (username, password))
            info = cursor.fetchone()
            if info is not None:
                if info['username'] == username and info['password'] == password:
                    session['loginsuccess'] = True
                    return redirect(url_for("profile"))

        return redirect(url_for("failed_login"))


@app.route('/new', methods=['GET', 'POST'])
def new_user():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            name = request.form['one']
            username = request.form['two']
            password = request.form['three']
            cursor = database.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("INSERT INTO login.login_info(name, username, password) VALUES (%s, %s, %s)", (name, username, password))
            database.connection.commit()
            return redirect(url_for('index'))
    return render_template("register.html")


@app.route('/new/profile')
def profile():
    if session['loginsuccess']:
        return render_template("profile.html")


@app.route('/new/homepage')
def homepage():
    if session['loginsuccess']:
        return render_template("homepage.html")


@app.route('/failed_login')
def failed_login():
    return render_template("failed_login.html")


@app.route('/new/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for('index'))


@app.route('/unavailable')
def unavailable():
    return render_template('unavailable.html')


if __name__ == '__main__':
    app.run(debug=True)
