from functools import reduce
import seaborn as sns


def get_part1_list():
    """
    Filters a list to return even numbers greater than 33.
    """
    numbers = [x for x in range(100)]

    # TODO: Write a line here that uses filter and a lambda function to filter
    even_over_33 = list(filter(lambda x: 33 < x and x % 2 == 0, numbers))
    # the list so that it only contains even numbers greater than 33.
    new_numbers = [even_over_33]

    return new_numbers


def get_part2_list():
    """
    Maps a lambda function to a list to square each number and add one.
    """
    numbers = [x for x in range(100)]

    # TODO: Write a line here than uses map and a lambda function to go through
    m = list(map(lambda x: (x*x) + 1, numbers))
    # each number in the list, square it and then add one to the result
    new_numbers = [m]

    return new_numbers


def get_part3_list():
    """
    Reduces a list to its product
    """
    numbers = [x for x in range(1, 100)]

    # TODO: Write a line here that uses reduce and a lambda function to
    k = reduce(lambda x, y: x*y, numbers)
    # multiply all the numbers in the list together and return the product
    product = k

    return product


def main():
    """
    This function calls the above functions and displays their result.
    """
    print(get_part1_list())
    print(get_part2_list())
    print(get_part3_list())


if __name__ == "__main__":
    main()
