# Lewis Lockhart :: CS-241
"""
File: check03b.py
Purpose: Practice classes with Complex numbers.
"""


class Complex:
    """
    Holds values for real and imaginary numbers, has prompt() and display()
    """
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def prompt(self):
        self.real = int(input('Please enter the real part: '))
        self.imaginary = int(input('Please enter the imaginary part: '))

    def display(self):
        print(f'{self.real} + {self.imaginary}i')


def main():
    """
    This function tests your Complex class. It should have a prompt
    and a display member function to be called.

    You should not need to change this main function at all.
    """
    c1 = Complex()
    c2 = Complex()

    print("The values are:")
    c1.display()
    c2.display()

    print()
    c1.prompt()

    print()
    c2.prompt()

    print("\nThe values are:")
    c1.display()
    c2.display()


# If this is the main program being run, call our main function above
if __name__ == "__main__":
    main()
