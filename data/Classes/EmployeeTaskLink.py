
class EmployeeTaskLink:
    def __init__(self, linkID, empID, taskID):
        self.linkID = linkID
        self.empID = empID
        self.taskID = taskID

    def get_employee(self, list):
        for emp in list:
            if emp.empID == self.empID:
                return emp

    def get_task(self, list):
        for task in list:
            if task.taskID == self.taskID:
                return task