numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]


def add_five_to_beginning():
    numbers.insert(0, 5)
    print(numbers)


def remove_number():
    numbers.remove(2348)
    print(numbers)


def add_5_numbers_to_list():
    nums = [10, 20, 30, 40, 50]
    for i in nums:
        numbers.append(i)
    print(numbers)


def sort_the_list():
    numbers.sort()
    print(numbers)


def sort_the_list_reverse():
    numbers.sort(reverse=True)
    print(numbers)


def count_instances(num):
    a = numbers.count(num)
    print(a)


def find_index_of(num):
    i = numbers.index(num)
    print(i)


def split_list():
    print(numbers[0:len(numbers)//2])
    print(numbers[len(numbers)//2:])


def slice_with_stride():
    print(numbers[0:len(numbers):2])


def get_last_five():
    print(numbers[-5:])


def main():
    print(numbers)
    # add_five_to_beginning()
    # remove_number()
    # add_5_numbers_to_list()
    # sort_the_list()
    # sort_the_list_reverse()
    # count_instances(12)
    # find_index_of(96)
    # split_list()
    # slice_with_stride()
    get_last_five()


if __name__ == "__main__":
    main()
