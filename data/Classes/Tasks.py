
class Tasks:
    def __init__(self, taskID, title, datetime, description, statusID):
        self.taskID = taskID
        self.title = title
        self.datetime = datetime
        self.description = description
        self.statusID = statusID

    def get_status_name(self, list):
        for val in list:
            if val.statusID == self.statusID:
                return val.name