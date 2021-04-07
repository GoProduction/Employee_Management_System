import os
from flask import Flask, render_template, request, url_for, session
import connection
import cx_Oracle
from controllers import employees_controller, department_controller, tasks_controller, status_controller

app = Flask(__name__)

the_key = os.urandom(16)
app.secret_key = the_key


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test-data")
def test_data():
    departments = department_controller.get_departments()
    employees = employees_controller.get_employees()
    tasks = tasks_controller.get_tasks()
    status = status_controller.get_status()
    return render_template('test-data.html', employees=employees, departments=departments, tasks=tasks, status=status)


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@app.route("/report")
def report():
    return render_template('report.html')


@app.route("/directory")
def department():
    return render_template('directory.html')


@app.route("/user-add")
def user_add():
    return render_template('user-add.html')


@app.route("/user-add", methods=['POST'])
def user_add_post():
    # use message for displaying error/success
    message = ""
    return render_template("user-add.html", message=message)


@app.route("/user-remove")
def user_remove():
    return render_template('user-remove.html')


@app.route("/info-guide")
def info_guide():
    return render_template('info-guide.html')


@app.route("/settings")
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run()
