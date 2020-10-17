# Lewis Lockhart :: CS-241

def prompt_for_file_name():
    file_name = input("Please enter the data file: ")
    print('')
    return file_name


def write_data():

    my_dict = {
        "value_1": 10,
        "value_2": 20,
        "value_3": 30
    }

    with open(prompt_for_file_name(), "a+") as file_to_write:

        file_to_write.write(str(f"\n{my_dict}"))


def main():
    write_data()


if __name__ == "__main__":
    main()
