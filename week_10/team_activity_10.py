from random import randint
MAX_NUM = 100


def merge_sort(items):
    """
    Sorts the items in the list
    :param items: The list to sort
    """

    # if there is only one number - return
    if len(items) <= 1:
        return

    middle = len(items) // 2
    first_half = items[:middle]
    second_half = items[middle:]

    # recursion on first half
    merge_sort(first_half)
    # recursion on second half
    merge_sort(second_half)

    g_i = 0
    g_j = 0
    g_k = 0

    while g_i < len(first_half) and g_j < len(second_half):
        if first_half[g_i] < second_half[g_j]:
            items[g_k] = first_half[g_i]
            g_i += 1
            g_k += 1
        else:
            items[g_k] = second_half[g_j]
            g_j += 1
            g_k += 1

    while g_i < len(first_half):
        items[g_k] = first_half[g_i]
        g_i += 1
        g_k += 1

    while g_j < len(second_half):
        items[g_k] = second_half[g_j]
        g_j += 1
        g_k += 1


def quick_sort(items):

    first = 0
    last = len(items) - 1

    if first < last:
        split_point = partition(items, first, last)
        quick_sort_helper(items, first, splitpoint - 1)
        quickSortHelper(items, splitpoint + 1, last)


def partition(items, first, last):
    pivotvalue = items[first]


def generate_list(size):
    """
    Generates a list of random numbers.
    """
    items = [randint(0, MAX_NUM) for i in range(size)]
    return items


def display_list(items):
    """
    Displays a list
    """
    for item in items:
        print(item)


def main():
    """
    Tests the merge sort
    """
    size = int(input("Enter size: "))

    items = generate_list(size)
    merge_sort(items)

    print("\nThe Sorted list is:")
    display_list(items)


if __name__ == "__main__":
    main()
