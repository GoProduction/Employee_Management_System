from data.Classes.Department import Department


class Employee:
    def __init__(self, empID, deptID, fname, lname, title,
                 email, phone):
        self.empID = empID
        self.deptID = Department.deptID
        self.fname = fname
        self.lname = lname
        self.title = title
        self.phone = phone
        self.email = email

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)