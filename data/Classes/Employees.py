
class Employee:
    def __init__(self, empID, deptID, fname, lname, title,
                 phone, email):
        self.empID = empID
        self.deptID = deptID
        self.fname = fname
        self.lname = lname
        self.title = title
        self.phone = phone
        self.email = email

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def get_department_title(self, list):
        for val in list:
            if val.deptID == self.deptID:
                return val.deptTitle