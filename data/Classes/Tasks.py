from data.Classes.Status import Status


class Tasks:
    def __init__(self, taskID, title, datetime, description, statusID):
        self.taskID = taskID
        self.title = title
        self.datetime = datetime.now()
        self.description = description
        self.statusID = Status.statusID