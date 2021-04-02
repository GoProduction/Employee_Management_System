
class EmployeeNotes:
    def __init__(self, noteID, empID, description, datetime):
        self.noteID = noteID
        self.empID = empID
        self.description = description
        self.datetime = datetime.now()