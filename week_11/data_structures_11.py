
"""
Purpose: This file is a starting point to help you practice list comprehensions.
"""


def get_part1_list():
    """
    Returns a list of the squares of the numbers [0-99], e.g., 0, 1, 4, 9, 16, 25 ...]
    """
    numbers = [x**2 for x in range(99)]

    return numbers


def get_part2_list():
    """
    Returns a list of the the numbers [0-99] that are divisible by either 5 or 7
    """
    numbers = [x for x in range(99) if (x % 5 == 0) or (x % 7 == 0)]

    return numbers


def get_part3_list():
    """
    Filters a list of words to return only those that are at least 4 letters long and contain an 'e'
    """
    old_words = ["tacos", "knowledge", "water", "on", "the", "I", "is", "hilarious", "tie", "coat", "white", "covenants", "phone", "rubric", "send", "restrictions"]

    new_words = [old_words[x] for x in range(len(old_words)) if (len(old_words[x]) > 3) for y in old_words[x] if y == "e"]

    return new_words


def main():
    """
    This function calls the above functions and displays their result.
    """
    print(get_part1_list())
    print(get_part2_list())
    print(get_part3_list())


if __name__ == "__main__":
    main()
