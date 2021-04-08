# This class is intended to be used to traverse field data through requests.
    # EX: Submitting a new user will erase all fields on POST. This object will be used 
    # to save the field values in the case of an invalid field being entered, giving
    # the user a chance to fix the changes without having to fill out the entire field again

class EmployeePageObject:
    def __init__(self, deptID, fname, lname, title,
                 phone, email, address, city, state,
                 zipcode, licenseID, ssn):
        self.department_id = deptID
        self.first_name = fname
        self.last_name = lname
        self.title = title
        self.phone = phone
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.license_id = licenseID
        self.ssn = ssn