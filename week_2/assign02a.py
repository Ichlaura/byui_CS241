# Lewis Lockhart :: CS-241

def prompt_number():
    # prompt user for the number
    num_entered = int(input('Enter a positive number: '))

    # ensures value is positive before returning the value
    while num_entered < 0:
        print('Invalid entry. The number must be positive.')
        num_entered = int(input('Enter a positive number: '))

    print("")
    return num_entered


def compute_sum(passed_list):
    total = 0
    # adds each value in the list
    for n in passed_list:
        total += n

    print(f'The sum is: {total}')


def main():
    # holds number to be summed
    num_list = []
    # loops and fills num_list based on range
    for n in range(3):
        # appends the valid input from the user
        num_list.append(prompt_number())

    # sums and outputs the total of num_list
    compute_sum(num_list)


if __name__ == "__main__":
    main()
