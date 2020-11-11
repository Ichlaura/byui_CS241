"""
Assignment: check08a.py
Author: Lewis Lockhart
"""


class GradePointAverage:
    def __init__(self):
        self.__gpa = 0.0

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        if gpa < 0:
            self.__gpa = 0
        elif gpa > 4:
            self.__gpa = 4
        else:
            self.__gpa = gpa

    def get_letter(self):
        if 0.0 <= self.__gpa <= 0.99:
            return "F"
        elif 1 <= self.__gpa <= 1.99:
            return "D"
        elif 2 <= self.__gpa <= 2.99:
            return "C"
        elif 3 <= self.__gpa <= 3.99:
            return "B"
        else:
            return "A"

    def set_letter(self, letter):
        if letter == "F" or letter == "f":
            self.__gpa = 0.0
        elif letter == "D" or letter == "d":
            self.__gpa = 1.0
        elif letter == "C" or letter == "c":
            self.__gpa = 2.0
        elif letter == "B" or letter == "b":
            self.__gpa = 3.0
        elif letter == "A" or letter == "a":
            self.__gpa = 4.0


def main():
    student = GradePointAverage()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))


if __name__ == "__main__":
    main()
