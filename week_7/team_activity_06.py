"""
Author: Lewis Lockhart
"""

from abc import ABC
from abc import abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_paycheck(self):
        pass

    @abstractmethod
    def display(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, wage, hours):
        super().__init__(name)
        self.hourly_wage = wage
        self.hours = hours

    def get_paycheck(self):
        return self.hourly_wage * self.hours

    def display(self):
        print("{0} - ${1}/hour".format(self.name, self.hourly_wage))


class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_paycheck(self):
        return self.salary / 24

    def display(self):
        print("{0} - ${1}/year".format(self.name, self.salary))


def display_employee_data(_employee):
    print()
    _employee.display()
    print(f"Paycheck: ${_employee.get_paycheck()}")


def main():
    employees = []
    command = str()

    while command != "q":
        command = input("Enter 'h' (hourly employee), 's', (salary employee) or 'q': ")

        if command == "h":
            name = input("Enter employee name: ")
            wage = float(input("Enter employee wage: "))
            hours = float(input("Enter hours worked: "))

            ew = HourlyEmployee(name, wage, hours)
            employees.append(ew)

        elif command == "s":
            name = input("Enter name: ")
            salary = int(input("Enter salary: "))

            es = SalaryEmployee(name, salary)
            employees.append(es)

    for e in employees:
        display_employee_data(e)


if __name__ == "__main__":
    main()
