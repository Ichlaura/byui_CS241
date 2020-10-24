"""
File: Week 6 - data structures
Author: Lewis Lockhart
"""

from collections import deque


class Student:
    """ Has: name and course. Can prompt and display. """
    def __init__(self):
        self.name = ""
        self.course = ""

    def prompt(self):
        """ Prompts for student name and course. """
        self.name = input("\nEnter name: ")
        self.course = input("Enter course: ")
        print("")

    def display(self):
        """ Displays student information when being helped. """
        print("\nNow helping {} with {}\n".format(self.name, self.course))


class HelpSystem:
    """  """
    def __init__(self):
        self.waiting_list = deque()

    def is_student_waiting(self):
        """
        Returns True if there are currently students in the waiting_list,
        and false if not.
        """
        if len(self.waiting_list) == 0:
            return False
        else:
            return True

    def add_to_waiting_list(self, student):
        """
        Receives a Student as a parameter and adds them to the waiting list.
        """
        self.waiting_list.append(student)

    def help_next_student(self):
        """
        Checks if there is a student waiting and if not, displays "No one to help".
        If there is a student waiting then it removes them from the waiting_list
        and displays their information.
        """
        # check to see if the deque is empty
        waiting = self.is_student_waiting()
        if waiting:
            # if a student is in the list, remove student and display info
            student = self.waiting_list.popleft()
            student.display()
        else:
            print("\nNo one to help.\n")


def options():
    """ Gets user selection and returns it. """
    print("Options:\n"
          "1. Add a new student\n"
          "2. Help next student\n"
          "3. Quit")
    selection = int(input("Enter selection: "))
    return selection


def process_user_input(_help_system):
    """ Call methods based on user selection. """
    o = options()
    if o == 1:
        # if Add a new student
        new_student = Student()
        new_student.prompt()
        _help_system.add_to_waiting_list(new_student)
        process_user_input(_help_system)
    elif o == 2:
        # if Help next student
        _help_system.help_next_student()
        process_user_input(_help_system)
    elif o == 3:
        # if Quit
        pass


def main():
    """ Instantiates HelpSystem and Student. Calls process_user_input(). """
    help_system = HelpSystem()
    process_user_input(help_system)


if __name__ == '__main__':
    main()


"""
__main__:

waitlist = deque()
quit = False

while not quit:
    selected_option = get_input()
    quit = process_input(selected_option, waitlist)
"""
