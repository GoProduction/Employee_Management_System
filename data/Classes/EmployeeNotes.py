from data.Classes.Employees import Employee


class EmployeeNotes:
    def __init__(self, noteID, empID, description, datetime):
        self.noteID = noteID
        self.empID = Employee.empID
        self.description = description
        self.datetime = datetime.now()