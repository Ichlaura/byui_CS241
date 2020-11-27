"""
Assignment check10a.py
Completed by: Lewis Lockhart
"""


def sort(numbers):
    """ Fill in this method to sort the list of numbers. """
    for n in range(len(numbers)-1, 0, -1):
        max_position = 0
        for location in range(1, n + 1):
            if numbers[location] > numbers[max_position]:
                max_position = location
        temp = numbers[n]
        numbers[n] = numbers[max_position]
        numbers[max_position] = temp


def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers


def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)


def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)


if __name__ == "__main__":
    main()
