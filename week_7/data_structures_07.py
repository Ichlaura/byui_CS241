"""
Assignment: Week 07 Data Structures
Author: Lewis Lockhart
"""


def fib(_index, count=1, num_zero=0, num_one=1):
    """
    Calculates the Fibonacci number based on an index.
    :param _index: number passed by the user.
    :param count: number of times the function has been run.
    :param num_zero: the first index to be added.
    :param num_one: the second index to be added.
    :return: fib() until one of the exit conditions are met
    """
    # exit conditions
    if _index == 0:
        return 0
    # if the count equals the index entered
    elif count == _index:
        # returns the last number calculated
        return num_one

    # combines last numbers in the sequence
    next_num = num_zero + num_one
    # updates sequence
    num_zero = num_one
    num_one = next_num

    # return the function call if exit condition is not met
    return fib(_index, count + 1, num_zero, num_one)


def main():
    index = int(input("Enter a Fibonacci index: "))
    print(f"The Fibonacci number is: {fib(index)}")


if __name__ == "__main__":
    main()
