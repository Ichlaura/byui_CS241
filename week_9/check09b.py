"""
Author: Lewis Lockhart
Assignment: check09b.py
"""


class NegativeNumberError(Exception):
    """ Raised when the value is negative. """
    pass


def get_inverse(n):
    """ """
    if n == 0:
        raise ZeroDivisionError
    elif n < 0:
        raise NegativeNumberError
    return 1 / n


def main():
    try:
        value = int(input("Enter a number: "))
        inverse = get_inverse(value)
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError:
        print("Error: The value cannot be negative")
    else:
        print(f"The result is: {inverse}")


if __name__ == "__main__":
    main()
