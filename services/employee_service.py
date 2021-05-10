import operator
from flask import Flask, request
from controllers import employees_controller, employee_info_controller
from services import validation
from data.Classes.Employees import Employee
from data.Classes.EmployeeInfo import EmployeeInfo

# retrieves employee id from field
def get_id_from_field(field_name):
    id = request.form.get(field_name)
    print("Selected ID: ", id)
    return int(id)

# retrieves and returns the value as a property from a drop-down field
def get_sort_property(field_name):
    prop = request.form.get(field_name)
    return str(prop)

# takes in list and returns sorted employee list from selected drop-down value
def sort_employee_list(list):
    prop = get_sort_property('txtCategory')
    sorted_list = sorted(list, key=operator.attrgetter(prop))

    return sorted_list

# add employee method for the add-user page
def validate_employee_fields():
    try:
        message = []

        # initialize variables
        id = request.form['idField']
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
        department = request.form.get('inputDepartment')

        # run validation
        # first_name
        data = validation.validate_field(id, "first_name", first_name)
        if(data != "Pass"):
            message.append(data)
        # last_name
        data = validation.validate_field(id, "last_name", last_name)
        if(data != "Pass"):
            message.append(data)
        # social security number
        data = validation.validate_field(id, "ssn", ssn)
        if(data != "Pass"):
            message.append(data)
        # license
        data = validation.validate_field(id, "license", license)
        if(data != "Pass"):
            message.append(data)
        # email
        data = validation.validate_field(id, "email", email)
        if(data != "Pass"):
            message.append(data)
        # phone
        data = validation.validate_field(id, "phone", phone)
        if(data != "Pass"):
            message.append(data)
        # address
        data = validation.validate_field(id, "address", address)
        if(data != "Pass"):
            message.append(data)
        # city
        data = validation.validate_field(id, "city", city)
        if(data != "Pass"):
            message.append(data)
        # state
        data = validation.validate_field(id, "state", state)
        if(data != "Pass"):
            message.append(data)
        # zip
        data = validation.validate_field(id, "zip", zip)
        if(data != "Pass"):
            message.append(data)
        data = validation.validate_field(id, "title", title)
        if(data != "Pass"):
            message.append(data)
        # department
        data = validation.validate_field(id, "department", department)
        if(data != "Pass"):
            message.append(data)

        # if message is empty at end of check, append 'Success!' to it
        if (message == []):
            message.append('Success!')
        
        return message
    except ValueError:
        print("Must be a number.")

# takes field values from add-user page
def transfer_field_state():
    list = []

    id = request.form['idField']
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
    
    employee = Employee(id, department, first_name, last_name, title, phone, email)
    employee_info = EmployeeInfo("", id, address, city, state, zip, license, ssn)

    list.append(employee)
    list.append(employee_info)
    
    return list

# initializes array to join Employee and EmployeeInfo objects
def initialize_employee_array():
    list = []
    employee = Employee("", "", "", "", "", "", "")
    employee_info = EmployeeInfo("", "", "", "", "", "", "", "")

    list.append(employee)
    list.append(employee_info)

    return list