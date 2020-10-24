"""
File: check05a.py
By: Lewis Lockhart
"""


class Phone:
    """ Phone class - prompts and displays. """
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        """ Prompts for phone number. """
        self.area_code = input("Area Code: ")
        self.prefix = input("Prefix: ")
        self.suffix = input("Suffix: ")

    def phone_display(self):
        """ Displays phone number. """
        print("Phone info:")
        print(f"({self.area_code}){self.prefix}-{self.suffix}")


class SmartPhone(Phone):
    def __init__(self):
        # Extends the Phone class
        self.email = ""
        super().__init__()

    def prompt(self):
        """ Prompts for phone number and email. """
        self.prompt_number()
        self.email = input("Email: ")

    def smart_phone_display(self):
        """ Displays phone number and the email. """
        self.phone_display()
        print(f"{self.email}")


def main():
    # Base Phone class check
    p = Phone()
    print("Phone:")
    p.prompt_number()
    print('')
    p.phone_display()
    print('')

    # Smart phone class check
    s = SmartPhone()
    print("Smart phone:")
    s.prompt()
    print('')
    s.smart_phone_display()


if __name__ == '__main__':
    main()
