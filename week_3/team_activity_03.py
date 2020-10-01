# Lewis Lockhart :: CS-241
from fractions import Fraction
"""
A Python 3 program to hold rational numbers (i.e., fractions). The rational number
class contains an integer for the numerator and denominator.
"""


class RationalNumbers:
    """

    """
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def display(self):
        if self.numerator == self.denominator:
            print(1)
        elif self.numerator > self.denominator:
            whole_num = int(self.numerator / self.denominator)
            mod = int(self.numerator % self.denominator)
            print(f'{whole_num} {mod}/{self.denominator}')
        else:
            print(f"{self.numerator}/{self.denominator}")

    def prompt(self):
        self.numerator = int(input('Enter the numerator: '))
        self.denominator = int(input('Enter the denominator: '))

    def display_decimal(self):
        decimal = float(self.numerator / self.denominator)
        print(decimal)

    def reduce_fraction(self):
        reduced = Fraction(self.numerator, self.denominator)
        print(reduced)


def multiply_by():
    pass


def main():
    rn = RationalNumbers()
    rn.display()
    rn.prompt()
    rn.display()
    rn.display_decimal()
    rn.reduce_fraction()


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
