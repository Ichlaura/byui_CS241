class BalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)


class OutOfChecksError(Exception):
    def __init__(self, message):
        super().__init__(message)


class CheckingAccount:
    def __init__(self, starting_balance, num_checks):
        self.__balance = starting_balance
        self.check_count = num_checks
        self.credit_amount = 0
        self.overage_amount = 0

        if starting_balance < 0:
            raise BalanceError("The start balance cannot be negative.")

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("The balance cannot be negative.")
        self.__balance += amount

    def display(self):
        print("Checks remaining: {}, Balance remaining: ${:.2f}"
              .format(self.check_count, self.__balance))

    def apply_for_credit(self, amount):
        self.credit_amount = amount
        raise NotImplementedError("Service not implemented yet.")

    def write_check(self, amount):
        if (self.__balance - amount) < 0:
            self.overage_amount = abs(self.__balance - amount)
            raise BalanceError(f"The check amount exceeds the balance by "
                               f"{self.overage_amount}.")
        if self.check_count <= 0:
            raise OutOfChecksError("You're out of checks.")

        self.__balance -= amount
        self.check_count -= 1


def get_more_checks(account):
    order_checks = input("Order more checks (yes / no)?")
    if order_checks == "yes":
        account.balance -= 5
        account.check_count += 25
    else:
        pass


def display_menu():
    """
    Displays the available commands.
    """
    print()
    print("Commands:")
    print("  quit - Quit")
    print("  new - Create new account")
    print("  display - Display account information")
    print("  deposit - Deposit money")
    print("  check - Write a check")
    print("  credit - Apply for credit")


def main():
    """
    Used to test the CheckingAccount class.
    """
    acc = None
    command = ""

    while command != "quit":
        display_menu()
        command = input("Enter a command: ")

        if command == "new":
            try:
                balance = float(input("Starting balance: "))
                num_checks = int(input("Numbers of checks: "))
                acc = CheckingAccount(balance, num_checks)
            except BalanceError as e:
                print("Error: {}".format(str(e)))

        elif command == "display":
            acc.display()

        elif command == "deposit":
            try:
                amount = float(input("Amount: "))
                acc.deposit(amount)
            except ValueError as e:
                print("Error: {}".format(str(e)))

        elif command == "check":
            try:
                amount = float(input("Amount: "))
                acc.write_check(amount)
            except BalanceError as e:
                print("Error: {}".format(str(e)))
            except OutOfChecksError as e:
                print("Error: {}".format(str(e)))
                get_more_checks(acc)

        elif command == "credit":
            try:
                amount = float(input("Amount: "))
                acc.apply_for_credit(amount)
            except NotImplementedError as e:
                print("Error: {}".format(str(e)))


if __name__ == "__main__":
    main()
