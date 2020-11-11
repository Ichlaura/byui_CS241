"""
Assignment: check08b.py
Author: Lewis Lockhart
"""


class GradePointAverage:
    def __init__(self):
        self._gpa = 0.0

    def _get_gpa(self):
        return self._gpa

    def _set_gpa(self, gpa):
        if gpa < 0:
            self._gpa = 0
        elif gpa > 4:
            self._gpa = 4
        else:
            self._gpa = gpa

    gpa = property(_get_gpa, _set_gpa)

    def _get_letter(self):
        if 0.0 <= self._gpa <= 0.99:
            return "F"
        elif 1 <= self._gpa <= 1.99:
            return "D"
        elif 2 <= self._gpa <= 2.99:
            return "C"
        elif 3 <= self._gpa <= 3.99:
            return "B"
        else:
            return "A"

    def _set_letter(self, letter):
        if letter == "F" or letter == "f":
            self._gpa = 0.0
        elif letter == "D" or letter == "d":
            self._gpa = 1.0
        elif letter == "C" or letter == "c":
            self._gpa = 2.0
        elif letter == "B" or letter == "b":
            self._gpa = 3.0
        elif letter == "A" or letter == "a":
            self._gpa = 4.0

    @property
    def letter(self):
        return self._get_letter()

    @letter.setter
    def letter(self, letter):
        self._set_letter(letter)


def main():
    student = GradePointAverage()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))


if __name__ == "__main__":
    main()
