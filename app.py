import os
from functools import wraps

from flask import Flask, render_template, request, url_for, session
from werkzeug.utils import redirect

import connection
import cx_Oracle
from controllers import employees_controller, department_controller, tasks_controller, status_controller
from services import employee_service, user_service

app = Flask(__name__)

the_key = os.urandom(16)
app.secret_key = the_key


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/testindex")
def testindex():
    return render_template('testindex.html')


@app.route("/login", methods=["POST"])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            if (user_service.validate_user() == True):
                # if true assigns username to session
                session['username'] = username
                return redirect(url_for('dashboard'))
            return redirect(url_for('index'))
    except Exception:
        return redirect(url_for('index'))


@app.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/test-data")
@login_required
def test_data():
    departments = department_controller.get_departments()
    employees = employees_controller.get_employees()
    tasks = tasks_controller.get_tasks()
    status = status_controller.get_status()
    return render_template('test-data.html', employees=employees, departments=departments, tasks=tasks, status=status)


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route("/report", methods=["GET", "POST"])
@login_required
def report():
    departments = department_controller.get_departments()
    employees = employees_controller.get_employees_short()
    employee = employee_service.initialize_employee_array()
    return render_template('report.html', employees=employees, employee=employee, departments=departments)

@app.route("/get-user-info", methods=['POST'])
def get_user_info():
    id = employee_service.get_id_from_field("selectUser")
    departments = department_controller.get_departments()
    employee = employees_controller.get_employee(id)
    employees = employees_controller.get_employees_short()
    return render_template('report.html', employees=employees, employee=employee, departments=departments)


@app.route("/directory", methods=['GET', 'POST'])
@login_required
def directory():
    departments = department_controller.get_departments()
    employees = employees_controller.get_employees()

    # POST is requested when sorting button is selected
    if request.method == 'POST':
        employees_sorted = employee_service.sort_employee_list(employees)
        return render_template('directory.html', departments=departments, employees=employees_sorted)

    return render_template('directory.html', departments=departments, employees=employees)


@app.route("/user-add", methods=['GET', 'POST'])
@login_required
def user_add():
    message = []

    data_list = employee_service.initialize_employee_array()
    departments = department_controller.get_departments()

    if request.method == 'POST':
        message = employee_service.add_employee_event()

        if (message[0] != "Successfully created a new employee!"):
            # collect field data into list (Employee, EmployeeInfo)
            data_list = employee_service.transfer_field_state()

            # debug
            for val in data_list:
                print(val)

            # call add_employee method from controller
            employees_controller.add_employee(data_list)

            # return render template
            return render_template('user-add.html', message=message, departments=departments, data_list=data_list)
        else:
            return render_template('user-add.html', message=message, departments=departments, data_list=data_list)
    else:
        return render_template('user-add.html', message=message, departments=departments, data_list=data_list)


@app.route("/user-remove", methods=['GET', 'POST'])
@login_required
def user_remove():
    users = employees_controller.get_employees()
    if request.method == 'POST':
        id = employee_service.get_id_from_field('selectField')
        employees_controller.remove_employee(id)
        #reinstantiate user list to reflect removed user
        users = employees_controller.get_employees()
        return render_template('user-remove.html', users=users)
    return render_template('user-remove.html', users=users)


@app.route("/info-guide")
@login_required
def info_guide():
    return render_template('info-guide.html')


@app.route("/settings")
@login_required
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run()
