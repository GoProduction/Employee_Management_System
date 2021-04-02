from flask import Flask, render_template
import connection
# import cx_Oracle
from controllers import employees_controller

app = Flask(__name__)


@app.route("/")
def index():
    employees_controller.get_employees()
    return render_template('index.html')


@app.route("/department")
def department():
    return render_template('department.html')


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

