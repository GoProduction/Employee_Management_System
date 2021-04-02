from data.Classes.Employees import Employee


class EmployeeInfo:
    def __init__(self, infoID, empID, address, city, state,
                 zipcode, licenseID, ssn):
        self.infoID = infoID
        self.empID = Employee.empID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.licenseID = licenseID
        self.ssn = ssn