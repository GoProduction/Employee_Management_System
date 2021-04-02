import os
from flask import Flask, render_template, request, url_for, session
import connection
import cx_Oracle
from controllers import employees_controller

app = Flask(__name__)

the_key = os.urandom(16)
app.secret_key = the_key


@app.route("/")
def index():
    employees_controller.get_employees()
    return render_template('index.html')


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@app.route("/directory")
def department():
    return render_template('directory.html')


@app.route("/user-add")
def user_add():
    return render_template('user-add.html')


@app.route("/user-remove")
def user_remove():
    return render_template('user-remove.html')


@app.route("/settings")
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run()
