from data.Classes.Employees import Employee
from data.Classes.Tasks import Tasks


class EmployeeTaskLink:
    def __init__(self, linkID, empID, taskID):
        self.linkID = linkID
        self.empID = Employee.empID
        self.taskID = Tasks.taskID