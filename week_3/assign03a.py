# Lewis Lockhart :: CS-241
class Student:
    """
    Student class - takes first name, last name, and student id number.
    """
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id


def prompt_student():
    """
    Creates a new student object, then prompts the user for a first name, last name, and id.
    """
    # user prompts
    f_name = input('Please enter your first name: ')
    l_name = input('Please enter your last name: ')
    s_id = int(input('Please enter your id number: '))

    # creates a new Student object
    student = Student(f_name, l_name, s_id)

    return student


def display_student(s_info):
    """
    Accepts a student object, and displays its information.
    """
    print('')
    print('Your information:')
    print(f'{s_info.student_id} - {s_info.first_name} {s_info.last_name}')


def main():
    """
    Calls the prompt_student and display_student functions.
    """
    student_info = prompt_student()
    display_student(student_info)


if __name__ == "__main__":
    main()
