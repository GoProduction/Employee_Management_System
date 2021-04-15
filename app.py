import os
from flask import Flask, render_template, request, url_for, session
import connection
import cx_Oracle
from controllers import employees_controller, department_controller, tasks_controller, status_controller
from services import employee_service

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


@app.route("/directory", methods=['GET', 'POST'])
def department():
    departments = department_controller.get_departments()
    employees = employees_controller.get_employees()

    # POST is requested when sorting button is selected
    if request.method == 'POST':
        employees_sorted = employee_service.sort_employee_list(employees)
        return render_template('directory.html', departments=departments, employees=employees_sorted)

    return render_template('directory.html', departments=departments, employees=employees)


@app.route("/user-add", methods=['GET', 'POST'])
def user_add():
    message = []

    data_list = employee_service.initialize_employee_array()
    departments = department_controller.get_departments()

    if request.method == 'POST':
        message = employee_service.add_employee_event()

        if(message[0] != "Successfully created a new employee!"):
            # collect field data into list (Employee, EmployeeInfo)
            data_list = employee_service.transfer_field_state()

            #debug
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
