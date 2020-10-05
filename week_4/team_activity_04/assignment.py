# Lewis Lockhart :: CS-241
from date import Date


class Assignment:
    def __init__(self):
        self.name = "Untitled"
        self.start_date = Date()
        self.due_date = Date()
        self.end_date = Date()

    def prompt(self):
        self.name = input("Name: ")
        print("")
        print("Start Date:")
        self.start_date.prompt()
        print("")
        print("Due Date:")
        self.due_date.prompt()
        print("")
        print("End Date:")
        self.end_date.prompt()

    def display(self):
        print("")
        print(f"Assignment: {self.name}")
        print(f"Start Date: ")
        print(self.start_date.display())
        print("Due Date:")
        print(self.due_date.display())
        print(f"End Date:")
        print(self.end_date.display())
