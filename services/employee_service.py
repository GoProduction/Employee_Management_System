from flask import Flask, request
from controllers import employees_controller, employee_info_controller
from services import validation
from data.Classes.Employees import Employee
from data.Classes.EmployeeInfo import EmployeeInfo

# add employee method for the add-user page
def add_employee_event():
    try:
        message = []

        # initialize variables
        first_name = request.form['inputFirstname']
        last_name = request.form['inputLastname']
        ssn = request.form['inputSSN']
        license = request.form['inputLicense']
        email = request.form['inputEmail']
        phone = request.form['inputPhone']
        address = request.form['inputAddress']
        city = request.form['inputCity']
        state = request.form.get('inputState')
        zip = request.form['inputZip']
        title = request.form['inputTitle']
        #department = request.form['inputDepartment'].upper()

        # run validation
        # first_name
        data = validation.validate_field("first_name", first_name)
        if(data != "Pass"):
            message.append(data)
        # last_name
        data = validation.validate_field("last_name", last_name)
        if(data != "Pass"):
            message.append(data)
        # social security number
        data = validation.validate_field("ssn", ssn)
        if(data != "Pass"):
            message.append(data)
        # license
        data = validation.validate_field("license", license)
        if(data != "Pass"):
            message.append(data)
        # email
        data = validation.validate_field("email", email)
        if(data != "Pass"):
            message.append(data)
        # phone
        data = validation.validate_field("phone", phone)
        if(data != "Pass"):
            message.append(data)
        # address
        data = validation.validate_field("address", address)
        if(data != "Pass"):
            message.append(data)
        # city
        data = validation.validate_field("city", city)
        if(data != "Pass"):
            message.append(data)
        # state
        data = validation.validate_field("state", state)
        if(data != "Pass"):
            message.append(data)
        # zip
        data = validation.validate_field("zip", zip)
        if(data != "Pass"):
            message.append(data)
        # department ( leave empty for now )
        #if(validation.validate_field("department", department) == False):
         #   message.append("Invalid department")
        # title
        data = validation.validate_field("title", title)
        if(data != "Pass"):
            message.append(data)

        # SUCCESS
        else:
            message.append("Successfully created a new employee!")
        return message
    except ValueError:
        print("Must be a number.")

def transfer_field_state():
    list = []

    first_name = request.form['inputFirstname']
    last_name = request.form['inputLastname']
    ssn = request.form['inputSSN']
    email = request.form['inputEmail']
    phone = request.form['inputPhone']
    address = request.form['inputAddress']
    city = request.form['inputCity']
    state = request.form.get('inputState')
    zip = request.form['inputZip']
    department = request.form.get('inputDepartment')
    title = request.form['inputTitle']
    license = request.form['inputLicense']
    
    employee = Employee("", department, first_name, last_name, title, phone, email)
    employee_info = EmployeeInfo("", "", address, city, state, zip, license, ssn)
    
    list.append(employee)
    list.append(employee_info)

    return list

def initialize_employee_array():
    list = []
    employee = Employee("", "", "", "", "", "", "")
    employee_info = EmployeeInfo("", "", "", "", "", "", "", "")

    list.append(employee)
    list.append(employee_info)

    return list